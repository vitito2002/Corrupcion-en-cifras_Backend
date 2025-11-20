import { useState, useMemo } from 'react';
import Tabs, { type Tab } from '@/components/ui/Tabs';
import StatsCard from '@/components/ui/StatsCard';
import {
  CasosPorEstadoChart,
  JuecesMayorDemoraChart,
  CausasIniciadasPorAnoChart,
  DelitosMasFrecuentesChart,
  CausasEnTramitePorJuzgadoChart,
  PersonasMasDenunciadasChart,
  PersonasQueMasDenunciaronChart,
  CausasPorFiscalChart,
  CausasPorFueroChart,
  DuracionOutliersChart,
} from '@/components/analytics/visualizations';
import { downloadBaseZip, fetchCasosPorEstado, fetchDuracionInstruccion } from '@/services/analytics';
import { useAnalytics } from '@/hooks/useAnalytics';
import type { CasosPorEstadoResponse, DuracionInstruccionResponse } from '@/types/analytics';

type TabId = 'general' | 'personas' | 'fiscales' | 'juzgados' | 'otros' | 'exportacion';

/**
 * Componente para la sección de KPIs
 * Obtiene datos reales del backend para mostrar estadísticas
 */
const KPIsSection = () => {
  const { data: casosData } = useAnalytics<CasosPorEstadoResponse>(
    fetchCasosPorEstado,
    []
  );
  const { data: duracionData } = useAnalytics<DuracionInstruccionResponse>(
    () => fetchDuracionInstruccion(1),
    []
  );

  const kpis = useMemo(() => {
    const totalCausas = casosData?.datos_grafico?.total || 0;
    
    // Calcular porcentaje de terminadas
    let porcentajeTerminadas = '0%';
    if (casosData?.datos_grafico) {
      const labels = casosData.datos_grafico.labels;
      const data = casosData.datos_grafico.data;
      const indexTerminada = labels.findIndex((label) => 
        label.toLowerCase().includes('terminada')
      );
      if (indexTerminada !== -1 && totalCausas > 0) {
        const cantidadTerminadas = data[indexTerminada];
        const porcentaje = (cantidadTerminadas / totalCausas) * 100;
        porcentajeTerminadas = `${porcentaje.toFixed(1)}%`;
      }
    }

    // Duración promedio
    const duracionPromedio = duracionData?.datos_grafico?.duracion_promedio_dias || 0;
    const duracionTexto = duracionPromedio > 0 
      ? `${Math.round(duracionPromedio)} días`
      : 'N/A';

    return {
      totalCausas: totalCausas.toLocaleString(),
      porcentajeTerminadas,
      duracionPromedio: duracionTexto,
    };
  }, [casosData, duracionData]);

  return (
    <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
      <StatsCard title="Total de causas" value={kpis.totalCausas} />
      <StatsCard title="% Terminadas" value={kpis.porcentajeTerminadas} />
      <StatsCard title="Duración promedio" value={kpis.duracionPromedio} />
    </div>
  );
};

const AnalyticsPage = () => {
  const [activeTab, setActiveTab] = useState<TabId>('general');

  const tabs: Tab[] = [
    { id: 'general', label: 'General' },
    { id: 'personas', label: 'Personas' },
    { id: 'fiscales', label: 'Fiscales' },
    { id: 'juzgados', label: 'Juzgados' },
    { id: 'otros', label: 'Otros' },
    { id: 'exportacion', label: 'Exportación' },
  ];

  return (
    <div className="py-12">
      <div className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
        <h1 className="text-6xl md:text-7xl font-bold text-[#1E3A8A] mb-4 tracking-tight leading-tight" style={{ fontFamily: "'Playfair Display', Georgia, serif" }}>
          Corrupción en Cifras
        </h1>
        <p className="text-gray-600 mb-8 leading-relaxed">
          Visualización de datos sobre casos de corrupción en el sistema judicial
        </p>

        {/* Sección de KPIs */}
        <KPIsSection />

        {/* Sistema de Pestañas */}
        <Tabs
          tabs={tabs}
          activeTab={activeTab}
          onTabChange={(tabId) => setActiveTab(tabId as TabId)}
          className="mb-8"
        />

        {/* Contenido de las Pestañas */}
        <div className="mt-8 space-y-12">
          {/* Pestaña: General */}
          {activeTab === 'general' && (
            <div className="space-y-12 fade-in">
              <CausasIniciadasPorAnoChart />
              <CasosPorEstadoChart />
              <DelitosMasFrecuentesChart limit={10} />
              <DuracionOutliersChart limit={5} />
            </div>
          )}

          {/* Pestaña: Personas */}
          {activeTab === 'personas' && (
            <div className="space-y-12 fade-in">
              <PersonasMasDenunciadasChart limit={20} />
              <PersonasQueMasDenunciaronChart limit={20} />
            </div>
          )}

          {/* Pestaña: Fiscales */}
          {activeTab === 'fiscales' && (
            <div className="space-y-12 fade-in">
              <CausasPorFiscalChart limit={20} />
            </div>
          )}

          {/* Pestaña: Juzgados */}
          {activeTab === 'juzgados' && (
            <div className="space-y-12 fade-in">
              <CausasEnTramitePorJuzgadoChart limit={20} />
              <JuecesMayorDemoraChart limit={10} />
              <CausasPorFiscalChart limit={15} />
            </div>
          )}

          {/* Pestaña: Otros */}
          {activeTab === 'otros' && (
            <div className="space-y-12 fade-in">
              <CausasPorFueroChart />
            </div>
          )}

          {/* Pestaña: Exportación */}
          {activeTab === 'exportacion' && (
            <ExportacionTab />
          )}
        </div>
      </div>
    </div>
  );
};

/**
 * Componente para la pestaña de exportación
 */
const ExportacionTab = () => {
  const [downloading, setDownloading] = useState(false);

  const handleDownload = async () => {
    setDownloading(true);
    try {
      await downloadBaseZip();
    } catch (error) {
      console.error('Error al descargar:', error);
      // El error ya se loguea en downloadBaseZip
    } finally {
      setDownloading(false);
    }
  };

  return (
    <div className="space-y-12 fade-in">
      <div className="bg-white border border-gray-200 shadow-md shadow-gray-200/60 rounded-xl p-8 hover:shadow-lg transition-shadow">
        <h2 className="text-2xl font-bold mb-4 text-[#1E3A8A] tracking-tight">Descargar Base de Datos</h2>
        <p className="text-gray-600 mb-6 leading-relaxed">
          Descarga toda la base de datos en formato ZIP. El archivo incluye todas las tablas
          exportadas como archivos CSV.
        </p>
        <button
          onClick={handleDownload}
          disabled={downloading}
          className={`
            w-full py-3 px-6 rounded-lg font-semibold text-base
            transition-all duration-200 shadow-sm
            ${downloading
              ? 'bg-gray-400 cursor-not-allowed text-white'
              : 'bg-[#3B82F6] hover:bg-[#2563EB] text-white'
            }
            focus:outline-none focus:ring-2 focus:ring-[#3B82F6] focus:ring-offset-2
          `}
        >
          {downloading ? 'Descargando...' : 'Descargar base completa (ZIP)'}
        </button>
        {downloading && (
          <p className="text-sm text-gray-500 mt-4 text-center">
            Descargando...
          </p>
        )}
      </div>
    </div>
  );
};

export default AnalyticsPage;

