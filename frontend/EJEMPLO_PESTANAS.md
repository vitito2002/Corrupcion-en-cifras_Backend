# 🎯 Ejemplo: Cómo Implementar Pestañas en AnalyticsPage

Este documento muestra cómo modificar `AnalyticsPage.tsx` para agregar un sistema de pestañas que organice los gráficos por categorías.

## 📋 Estructura de Pestañas Propuesta

1. **General**: Casos por estado, Causas iniciadas por año, Delitos más frecuentes
2. **Personas**: Personas más denunciadas, Personas que más denunciaron
3. **Fiscales**: Causas por fiscal (abiertas/terminadas)
4. **Juzgados**: Causas en trámite por juzgado, Jueces con mayor demora
5. **Otros**: Duración de instrucción, Causas por fuero

---

## 💻 Código Completo con Pestañas

Aquí tienes el código completo para `AnalyticsPage.tsx` con sistema de pestañas:

```tsx
import { useEffect, useState } from 'react';
import BarChart from '@/components/analytics/BarChart';
import PieChart from '@/components/analytics/PieChart';
import LineChart from '@/components/analytics/LineChart';
import {
  fetchCasosPorEstado,
  fetchJuecesMayorDemora,
  fetchCausasIniciadasPorAno,
  fetchDelitosMasFrecuentes,
  fetchCausasEnTramitePorJuzgado,
  // Agregar aquí las nuevas funciones cuando las crees
} from '@/services/analytics';
import type {
  CasosPorEstadoResponse,
  JuecesMayorDemoraResponse,
  CausasIniciadasPorAnoResponse,
  DelitosMasFrecuentesResponse,
  CausasEnTramitePorJuzgadoResponse,
} from '@/types/analytics';

type TabId = 'general' | 'personas' | 'fiscales' | 'juzgados' | 'otros';

const AnalyticsPage = () => {
  // Estado para la pestaña activa
  const [activeTab, setActiveTab] = useState<TabId>('general');

  // Estados para los datos
  const [casosPorEstado, setCasosPorEstado] = useState<CasosPorEstadoResponse | null>(null);
  const [juecesMayorDemora, setJuecesMayorDemora] = useState<JuecesMayorDemoraResponse | null>(null);
  const [causasIniciadasPorAno, setCausasIniciadasPorAno] = useState<CausasIniciadasPorAnoResponse | null>(null);
  const [delitosMasFrecuentes, setDelitosMasFrecuentes] = useState<DelitosMasFrecuentesResponse | null>(null);
  const [causasEnTramitePorJuzgado, setCausasEnTramitePorJuzgado] = useState<CausasEnTramitePorJuzgadoResponse | null>(null);
  
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  // Definir las pestañas
  const tabs: Array<{ id: TabId; label: string }> = [
    { id: 'general', label: 'General' },
    { id: 'personas', label: 'Personas' },
    { id: 'fiscales', label: 'Fiscales' },
    { id: 'juzgados', label: 'Juzgados' },
    { id: 'otros', label: 'Otros' },
  ];

  // Cargar datos al montar el componente
  useEffect(() => {
    const loadData = async () => {
      setLoading(true);
      setError(null);

      try {
        const [
          casosData,
          juecesData,
          causasAnoData,
          delitosData,
          causasJuzgadoData,
        ] = await Promise.all([
          fetchCasosPorEstado(),
          fetchJuecesMayorDemora(10),
          fetchCausasIniciadasPorAno(),
          fetchDelitosMasFrecuentes(10),
          fetchCausasEnTramitePorJuzgado(20),
        ]);

        setCasosPorEstado(casosData);
        setJuecesMayorDemora(juecesData);
        setCausasIniciadasPorAno(causasAnoData);
        setDelitosMasFrecuentes(delitosData);
        setCausasEnTramitePorJuzgado(causasJuzgadoData);
      } catch (err) {
        setError('Error al cargar los datos. Por favor, verifica que el backend esté corriendo.');
        console.error('Error loading analytics data:', err);
      } finally {
        setLoading(false);
      }
    };

    loadData();
  }, []);

  if (loading) {
    return (
      <div className="min-h-screen bg-gray-50 flex items-center justify-center">
        <div className="text-center">
          <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600 mx-auto mb-4"></div>
          <p className="text-gray-600">Cargando datos...</p>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="min-h-screen bg-gray-50 flex items-center justify-center">
        <div className="bg-red-50 border border-red-200 rounded-lg p-6 max-w-md">
          <h2 className="text-red-800 font-semibold mb-2">Error</h2>
          <p className="text-red-600">{error}</p>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gray-50 py-8">
      <div className="container mx-auto px-4">
        <h1 className="text-3xl font-bold text-gray-900 mb-8">
          Analytics - Corrupción en Cifras
        </h1>

        {/* Sistema de Pestañas */}
        <div className="border-b border-gray-200 mb-6">
          <nav className="flex space-x-8" aria-label="Tabs">
            {tabs.map((tab) => (
              <button
                key={tab.id}
                onClick={() => setActiveTab(tab.id)}
                className={`
                  py-4 px-1 border-b-2 font-medium text-sm transition-colors
                  ${
                    activeTab === tab.id
                      ? 'border-blue-500 text-blue-600'
                      : 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300'
                  }
                `}
              >
                {tab.label}
              </button>
            ))}
          </nav>
        </div>

        {/* Contenido de las Pestañas */}
        <div className="mt-6">
          {/* Pestaña: General */}
          {activeTab === 'general' && (
            <div className="space-y-10">
              {/* Casos por estado procesal */}
              <section>
                <h2 className="text-2xl font-bold mb-4">Casos por Estado Procesal</h2>
                <div className="bg-white shadow rounded-lg p-6">
                  {casosPorEstado?.datos_grafico ? (
                    <PieChart
                      labels={casosPorEstado.datos_grafico.labels}
                      data={casosPorEstado.datos_grafico.data}
                      title="Distribución de casos por estado procesal"
                    />
                  ) : (
                    <p className="text-gray-500">No hay datos disponibles</p>
                  )}
                </div>
              </section>

              {/* Causas iniciadas por año */}
              <section>
                <h2 className="text-2xl font-bold mb-4">Causas Iniciadas por Año</h2>
                <div className="bg-white shadow rounded-lg p-6">
                  {causasIniciadasPorAno?.datos_grafico ? (
                    <LineChart
                      labels={causasIniciadasPorAno.datos_grafico.labels.map(String)}
                      data={causasIniciadasPorAno.datos_grafico.data}
                      title="Evolución temporal de causas iniciadas"
                    />
                  ) : (
                    <p className="text-gray-500">No hay datos disponibles</p>
                  )}
                </div>
              </section>

              {/* Delitos más frecuentes */}
              <section>
                <h2 className="text-2xl font-bold mb-4">Delitos Más Frecuentes</h2>
                <div className="bg-white shadow rounded-lg p-6">
                  {delitosMasFrecuentes?.datos_grafico ? (
                    <BarChart
                      labels={delitosMasFrecuentes.datos_grafico.labels}
                      data={delitosMasFrecuentes.datos_grafico.data}
                      title="Top delitos por cantidad de causas"
                    />
                  ) : (
                    <p className="text-gray-500">No hay datos disponibles</p>
                  )}
                </div>
              </section>
            </div>
          )}

          {/* Pestaña: Personas */}
          {activeTab === 'personas' && (
            <div className="space-y-10">
              <section>
                <h2 className="text-2xl font-bold mb-4">Personas Más Denunciadas</h2>
                <div className="bg-white shadow rounded-lg p-6">
                  <p className="text-gray-500">
                    {/* Aquí agregarías el gráfico cuando implementes fetchPersonasMasDenunciadas */}
                    Próximamente: Gráfico de personas más denunciadas
                  </p>
                </div>
              </section>

              <section>
                <h2 className="text-2xl font-bold mb-4">Personas que Más Denunciaron</h2>
                <div className="bg-white shadow rounded-lg p-6">
                  <p className="text-gray-500">
                    {/* Aquí agregarías el gráfico cuando implementes fetchPersonasQueMasDenunciaron */}
                    Próximamente: Gráfico de personas que más denunciaron
                  </p>
                </div>
              </section>
            </div>
          )}

          {/* Pestaña: Fiscales */}
          {activeTab === 'fiscales' && (
            <div className="space-y-10">
              <section>
                <h2 className="text-2xl font-bold mb-4">Causas por Fiscal</h2>
                <div className="bg-white shadow rounded-lg p-6">
                  <p className="text-gray-500">
                    {/* Aquí agregarías el gráfico cuando implementes fetchCausasPorFiscal */}
                    Próximamente: Gráfico de causas por fiscal (abiertas/terminadas)
                  </p>
                </div>
              </section>
            </div>
          )}

          {/* Pestaña: Juzgados */}
          {activeTab === 'juzgados' && (
            <div className="space-y-10">
              {/* Causas en trámite por juzgado */}
              <section>
                <h2 className="text-2xl font-bold mb-4">Causas en Trámite por Juzgado</h2>
                <div className="bg-white shadow rounded-lg p-6">
                  {causasEnTramitePorJuzgado?.datos_grafico ? (
                    <BarChart
                      labels={causasEnTramitePorJuzgado.datos_grafico.labels}
                      data={causasEnTramitePorJuzgado.datos_grafico.data}
                      title="Cantidad de causas en trámite por juzgado"
                    />
                  ) : (
                    <p className="text-gray-500">No hay datos disponibles</p>
                  )}
                </div>
              </section>

              {/* Jueces con mayor demora */}
              <section>
                <h2 className="text-2xl font-bold mb-4">Jueces con Mayor Demora</h2>
                <div className="bg-white shadow rounded-lg p-6">
                  {juecesMayorDemora?.datos_grafico ? (
                    <BarChart
                      labels={juecesMayorDemora.datos_grafico.labels}
                      data={juecesMayorDemora.datos_grafico.data}
                      title="Demora promedio en días por juez"
                    />
                  ) : (
                    <p className="text-gray-500">No hay datos disponibles</p>
                  )}
                </div>
              </section>
            </div>
          )}

          {/* Pestaña: Otros */}
          {activeTab === 'otros' && (
            <div className="space-y-10">
              <section>
                <h2 className="text-2xl font-bold mb-4">Duración de Instrucción</h2>
                <div className="bg-white shadow rounded-lg p-6">
                  <p className="text-gray-500">
                    {/* Aquí agregarías el gráfico cuando implementes fetchDuracionInstruccion */}
                    Próximamente: Gráfico de duración de instrucción
                  </p>
                </div>
              </section>

              <section>
                <h2 className="text-2xl font-bold mb-4">Causas por Fuero</h2>
                <div className="bg-white shadow rounded-lg p-6">
                  <p className="text-gray-500">
                    {/* Aquí agregarías el gráfico cuando implementes fetchCausasPorFuero */}
                    Próximamente: Gráfico de causas por fuero judicial
                  </p>
                </div>
              </section>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

export default AnalyticsPage;
```

---

## 🎨 Estilos CSS Adicionales (Opcional)

Si quieres mejorar el diseño de las pestañas, puedes agregar estos estilos en `index.css`:

```css
/* Transición suave para las pestañas */
.tab-button {
  transition: all 0.2s ease-in-out;
}

.tab-button:hover {
  transform: translateY(-2px);
}

/* Indicador activo más visible */
.tab-active {
  position: relative;
}

.tab-active::after {
  content: '';
  position: absolute;
  bottom: -1px;
  left: 0;
  right: 0;
  height: 3px;
  background: linear-gradient(90deg, #3b82f6, #2563eb);
  border-radius: 3px 3px 0 0;
}
```

---

## ✅ Ventajas de este Enfoque

1. **Organización clara**: Los gráficos están agrupados por categorías lógicas
2. **Mejor UX**: El usuario puede navegar fácilmente entre diferentes tipos de análisis
3. **Carga eficiente**: Todos los datos se cargan una vez al inicio
4. **Fácil de extender**: Agregar nuevas pestañas o gráficos es muy simple
5. **Responsive**: Funciona bien en móviles y tablets

---

## 🚀 Próximos Pasos

1. Implementar las funciones faltantes en `services/analytics.ts`
2. Agregar los tipos faltantes en `types/analytics.ts`
3. Reemplazar los "Próximamente" con los gráficos reales
4. Agregar animaciones de transición entre pestañas
5. Agregar indicadores de cantidad de gráficos por pestaña

