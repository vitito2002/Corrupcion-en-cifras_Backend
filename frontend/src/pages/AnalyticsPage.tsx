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
    <div className="py-12 pb-16">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        {/* Header Section */}
        <div className="mb-12 fade-in-up">
          <h1 
            className="text-5xl md:text-6xl lg:text-7xl font-bold text-primary mb-4 tracking-tight leading-tight" 
            style={{ fontFamily: "'Playfair Display', Georgia, serif" }}
          >
            Corrupción en Cifras
          </h1>
          <p className="text-lg text-secondary max-w-2xl leading-relaxed">
            Visualización de datos sobre casos de corrupción en el sistema judicial
          </p>
        </div>

        {/* Sección de KPIs */}
        <div className="mb-10 fade-in-up">
          <KPIsSection />
        </div>

        {/* Sistema de Pestañas */}
        <div className="mb-10 fade-in-up">
          <Tabs
            tabs={tabs}
            activeTab={activeTab}
            onTabChange={(tabId) => setActiveTab(tabId as TabId)}
          />
        </div>

        {/* Contenido de las Pestañas */}
        <div className="space-y-10">
          {/* Pestaña: General */}
          {activeTab === 'general' && (
            <div className="space-y-10 fade-in-up">
              <div className="stagger-item">
                <CausasIniciadasPorAnoChart />
              </div>
              <div className="stagger-item">
                <CasosPorEstadoChart />
              </div>
              <div className="stagger-item">
                <DelitosMasFrecuentesChart limit={10} />
              </div>
              <div className="stagger-item">
                <DuracionOutliersChart limit={5} />
              </div>
            </div>
          )}

          {/* Pestaña: Personas */}
          {activeTab === 'personas' && (
            <div className="space-y-10 fade-in-up">
              <div className="stagger-item">
                <PersonasMasDenunciadasChart limit={20} />
              </div>
              <div className="stagger-item">
                <PersonasQueMasDenunciaronChart limit={20} />
              </div>
            </div>
          )}

          {/* Pestaña: Fiscales */}
          {activeTab === 'fiscales' && (
            <div className="space-y-10 fade-in-up">
              <div className="stagger-item">
                <CausasPorFiscalChart limit={20} />
              </div>
            </div>
          )}

          {/* Pestaña: Juzgados */}
          {activeTab === 'juzgados' && (
            <div className="space-y-10 fade-in-up">
              <div className="stagger-item">
                <CausasEnTramitePorJuzgadoChart limit={20} />
              </div>
              <div className="stagger-item">
                <JuecesMayorDemoraChart limit={10} />
              </div>
              <div className="stagger-item">
                <CausasPorFiscalChart limit={15} />
              </div>
            </div>
          )}

          {/* Pestaña: Otros */}
          {activeTab === 'otros' && (
            <div className="space-y-10 fade-in-up">
              <div className="stagger-item">
                <CausasPorFueroChart />
              </div>
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
    <div className="space-y-10 fade-in-up">
      <div className="bg-white border border-muted/30 shadow-md rounded-2xl p-8 hover:shadow-lg transition-all duration-300">
        <h2 className="text-2xl font-bold mb-3 text-primary tracking-tight">
          Descargar Base de Datos
        </h2>
        <p className="text-secondary mb-6 leading-relaxed">
          Descarga toda la base de datos en formato ZIP. El archivo incluye todas las tablas
          exportadas como archivos CSV.
        </p>
        <button
          onClick={handleDownload}
          disabled={downloading}
          className={`
            w-full py-3.5 px-6 rounded-xl font-semibold text-base
            transition-all duration-200 shadow-sm
            ${downloading
              ? 'bg-[#7F9C96] cursor-not-allowed text-white'
              : 'bg-[#1B4079] hover:bg-[#4D7C8A] text-white hover:shadow-md hover:-translate-y-0.5'
            }
            focus:outline-none focus:ring-2 focus:ring-primary focus:ring-offset-2
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

