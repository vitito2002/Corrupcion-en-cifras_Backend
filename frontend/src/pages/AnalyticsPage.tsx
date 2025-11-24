import { useState, useMemo, useEffect } from 'react';
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
import { fetchCasosPorEstado, fetchDuracionInstruccion, fetchUltimaActualizacion } from '@/services/analytics';
import { useAnalytics } from '@/hooks/useAnalytics';
import type { CasosPorEstadoResponse, DuracionInstruccionResponse } from '@/types/analytics';

type TabId = 'general' | 'personas' | 'fiscales' | 'juzgados' | 'otros';

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
  const [ultimaActualizacion, setUltimaActualizacion] = useState<string | null>(null);

  // Obtener fecha de última actualización
  useEffect(() => {
    const obtenerUltimaActualizacion = async () => {
      const data = await fetchUltimaActualizacion();
      if (data?.formato_fecha) {
        setUltimaActualizacion(data.formato_fecha);
      }
    };
    obtenerUltimaActualizacion();
  }, []);

  const tabs: Tab[] = [
    { id: 'general', label: 'General' },
    { id: 'personas', label: 'Personas' },
    { id: 'fiscales', label: 'Fiscalías' },
    { id: 'juzgados', label: 'Juzgados' },
    { id: 'otros', label: 'Otros' },
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
            {ultimaActualizacion && (
              <span className="block mt-2 text-sm text-gray-500">
                Última actualización: {ultimaActualizacion}
              </span>
            )}
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

          {/* Pestaña: Fiscalías */}
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
        </div>
      </div>
    </div>
  );
};

export default AnalyticsPage;

