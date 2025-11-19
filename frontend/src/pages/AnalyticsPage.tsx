import { useState } from 'react';
import Tabs, { type Tab } from '@/components/ui/Tabs';
import {
  CasosPorEstadoChart,
  JuecesMayorDemoraChart,
  CausasIniciadasPorAnoChart,
  DelitosMasFrecuentesChart,
  CausasEnTramitePorJuzgadoChart,
  PersonasMasDenunciadasChart,
  PersonasQueMasDenunciaronChart,
  CausasPorFiscalChart,
  DuracionInstruccionChart,
} from '@/components/analytics/visualizations';
import { downloadBaseZip } from '@/services/analytics';

type TabId = 'metodologia' | 'general' | 'personas' | 'fiscales' | 'juzgados' | 'otros' | 'exportacion';

const AnalyticsPage = () => {
  const [activeTab, setActiveTab] = useState<TabId>('metodologia');

  const tabs: Tab[] = [
    { id: 'metodologia', label: 'Metodología' },
    { id: 'general', label: 'General' },
    { id: 'personas', label: 'Personas' },
    { id: 'fiscales', label: 'Fiscales' },
    { id: 'juzgados', label: 'Juzgados' },
    { id: 'otros', label: 'Otros' },
    { id: 'exportacion', label: 'Exportación' },
  ];

  return (
    <div className="min-h-screen bg-gray-50 py-8">
      <div className="container mx-auto px-4">
        <h1 className="text-3xl font-bold text-gray-900 mb-8">
          Analytics - Corrupción en Cifras
        </h1>

        {/* Sistema de Pestañas */}
        <Tabs
          tabs={tabs}
          activeTab={activeTab}
          onTabChange={(tabId) => setActiveTab(tabId as TabId)}
          className="mb-6"
        />

        {/* Contenido de las Pestañas */}
        <div className="mt-6">
          {/* Pestaña: Metodología */}
          {activeTab === 'metodologia' && (
            <div className="space-y-6">
              <div className="bg-white shadow rounded-lg p-6">
                <h2 className="text-2xl font-bold mb-4">Metodología</h2>
                <p className="text-gray-700 leading-relaxed">
                  Aquí irá el texto explicando la metodología, el proceso de scraping, 
                  normalización de datos, construcción de la base, y cómo se generan 
                  las visualizaciones. Esto debe ser solo texto estático, 
                  sin componentes adicionales.
                </p>
              </div>
            </div>
          )}

          {/* Pestaña: General */}
          {activeTab === 'general' && (
            <div className="space-y-10">
              <CasosPorEstadoChart />
              <CausasIniciadasPorAnoChart />
              <DelitosMasFrecuentesChart limit={10} />
            </div>
          )}

          {/* Pestaña: Personas */}
          {activeTab === 'personas' && (
            <div className="space-y-10">
              <PersonasMasDenunciadasChart limit={20} />
              <PersonasQueMasDenunciaronChart limit={20} />
            </div>
          )}

          {/* Pestaña: Fiscales */}
          {activeTab === 'fiscales' && (
            <div className="space-y-10">
              <CausasPorFiscalChart limit={20} />
            </div>
          )}

          {/* Pestaña: Juzgados */}
          {activeTab === 'juzgados' && (
            <div className="space-y-10">
              <CausasEnTramitePorJuzgadoChart limit={20} />
              <JuecesMayorDemoraChart limit={10} />
              <CausasPorFiscalChart limit={15} />
            </div>
          )}

          {/* Pestaña: Otros */}
          {activeTab === 'otros' && (
            <div className="space-y-10">
              <DuracionInstruccionChart
                limit={20}
                title="Duración promedio de instrucción"
              />
              <div className="bg-white shadow rounded-lg p-6">
                <h2 className="text-2xl font-bold mb-4">Causas por Fuero</h2>
                <p className="text-gray-500">
                  Próximamente: Gráfico de causas por fuero judicial
                </p>
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
    <div className="space-y-10">
      <div className="bg-white shadow rounded-lg p-6">
        <h2 className="text-2xl font-bold mb-4">Descargar Base de Datos</h2>
        <p className="text-gray-600 mb-6">
          Descarga toda la base de datos en formato ZIP. El archivo incluye todas las tablas
          exportadas como archivos CSV.
        </p>
        <button
          onClick={handleDownload}
          disabled={downloading}
          className={`
            w-full py-4 px-6 rounded-lg font-semibold text-lg
            transition-colors duration-200
            ${downloading
              ? 'bg-gray-400 cursor-not-allowed text-white'
              : 'bg-blue-600 hover:bg-blue-700 text-white'
            }
            focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2
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

