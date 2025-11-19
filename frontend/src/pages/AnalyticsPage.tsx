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
} from '@/components/analytics/visualizations';

type TabId = 'general' | 'personas' | 'fiscales' | 'juzgados' | 'otros';

const AnalyticsPage = () => {
  const [activeTab, setActiveTab] = useState<TabId>('general');

  const tabs: Tab[] = [
    { id: 'general', label: 'General' },
    { id: 'personas', label: 'Personas' },
    { id: 'fiscales', label: 'Fiscales' },
    { id: 'juzgados', label: 'Juzgados' },
    { id: 'otros', label: 'Otros' },
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
              <div className="bg-white shadow rounded-lg p-6">
                <h2 className="text-2xl font-bold mb-4">Duración de Instrucción</h2>
                <p className="text-gray-500">
                  Próximamente: Gráfico de duración de instrucción
                </p>
              </div>
              <div className="bg-white shadow rounded-lg p-6">
                <h2 className="text-2xl font-bold mb-4">Causas por Fuero</h2>
                <p className="text-gray-500">
                  Próximamente: Gráfico de causas por fuero judicial
                </p>
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

export default AnalyticsPage;

