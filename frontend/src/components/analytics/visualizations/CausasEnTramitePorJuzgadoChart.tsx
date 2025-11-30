import { useState, useMemo } from 'react';
import { useAnalytics } from '@/hooks/useAnalytics';
import { fetchCausasEnTramitePorJuzgado } from '@/services/analytics';
import type { CausasEnTramitePorJuzgadoResponse } from '@/types/analytics';
import type { EstadoCausa } from '@/components/ui/EstadoCausaSwitch';
import EstadoCausaSwitch from '@/components/ui/EstadoCausaSwitch';
import BarChart from '@/components/analytics/BarChart';

interface CausasEnTramitePorJuzgadoChartProps {
  title?: string;
  limit?: number;
  className?: string;
}

/**
 * Componente completo para el gráfico de causas por juzgado
 * Incluye un switch para alternar entre causas abiertas, terminadas y ambas
 */
const CausasEnTramitePorJuzgadoChart = ({ 
  title = 'Causas por Juzgado',
  limit = 20,
  className = '' 
}: CausasEnTramitePorJuzgadoChartProps) => {
  const [estado, setEstado] = useState<EstadoCausa>('ambas');
  
  const { data, loading, error } = useAnalytics<CausasEnTramitePorJuzgadoResponse>(
    () => fetchCausasEnTramitePorJuzgado(limit),
    [limit]
  );

  // Seleccionar y ordenar los datos según el estado seleccionado
  // IMPORTANTE: Este hook DEBE estar antes de cualquier return condicional
  const { labelsOrdenados, datosOrdenados } = useMemo(() => {
    if (!data?.datos_grafico) {
      return { labelsOrdenados: [], datosOrdenados: [] };
    }

    const datosGrafico = estado === 'abiertas'
      ? data.datos_grafico.causas_abiertas
      : estado === 'terminadas'
      ? data.datos_grafico.causas_terminadas
      : data.datos_grafico.data;

    // Crear array de objetos para ordenar
    const items = data.datos_grafico.labels.map((label, index) => ({
      label,
      data: datosGrafico[index],
    }));

    // Ordenar de mayor a menor
    items.sort((a, b) => b.data - a.data);

    return {
      labelsOrdenados: items.map(item => item.label),
      datosOrdenados: items.map(item => item.data),
    };
  }, [data, estado]);

  // Ahora sí, los early returns después de todos los hooks
  if (loading) {
    return (
      <div className={`bg-white border border-muted/30 shadow-md rounded-2xl p-8 hover:shadow-md-hover hover:-translate-y-0.5 transition-all duration-300 ${className}`}>
        <h2 className="text-2xl font-bold mb-4 text-primary tracking-tight">{title}</h2>
        <div className="flex items-center justify-center h-64">
          <div className="text-center">
            <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-primary mx-auto mb-2"></div>
            <p className="text-gray-500 text-sm">Cargando datos...</p>
          </div>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className={`bg-white border border-muted/30 shadow-md rounded-2xl p-8 hover:shadow-md-hover hover:-translate-y-0.5 transition-all duration-300 ${className}`}>
        <h2 className="text-2xl font-bold mb-4 text-primary tracking-tight">{title}</h2>
        <div className="bg-red-50 border border-red-200 rounded p-4">
          <p className="text-red-600 text-sm">{error}</p>
        </div>
      </div>
    );
  }

  if (!data?.datos_grafico) {
    return (
      <div className={`bg-white border border-muted/30 shadow-md rounded-2xl p-8 hover:shadow-md-hover hover:-translate-y-0.5 transition-all duration-300 ${className}`}>
        <h2 className="text-2xl font-bold mb-4 text-primary tracking-tight">{title}</h2>
        <p className="text-gray-500">No hay datos disponibles</p>
      </div>
    );
  }

  const tituloGrafico = estado === 'abiertas'
    ? 'Cantidad de causas abiertas por juzgado'
    : estado === 'terminadas'
    ? 'Cantidad de causas terminadas por juzgado'
    : 'Cantidad de causas por juzgado';

  // Calcular el máximo global entre todas las opciones para fijar la escala
  const maxAbiertas = Math.max(...data.datos_grafico.causas_abiertas, 0);
  const maxTerminadas = Math.max(...data.datos_grafico.causas_terminadas, 0);
  const maxAmbas = Math.max(...data.datos_grafico.data, 0);
  const maxGlobal = Math.max(maxAbiertas, maxTerminadas, maxAmbas);
  // Agregar un pequeño margen (10%) para mejor visualización
  const maxX = Math.ceil(maxGlobal * 1.1);

  // Opciones personalizadas para gráfico horizontal
  const horizontalOptions = {
    indexAxis: 'y' as const,
    plugins: {
      legend: { display: false },
      tooltip: { enabled: true },
    },
    scales: {
      x: {
        beginAtZero: true,
        max: maxX,
      },
      y: {
        ticks: {
          autoSkip: false,
          padding: 10,
        },
      },
    },
  };

  return (
    <div className={`bg-white border border-muted/30 shadow-md rounded-2xl p-8 hover:shadow-md-hover hover:-translate-y-0.5 transition-all duration-300 ${className}`}>
      <div className="flex items-center justify-between mb-4">
        <h2 className="text-2xl font-bold text-primary tracking-tight">{title}</h2>
        <EstadoCausaSwitch estado={estado} onChange={setEstado} />
      </div>
      <BarChart
        labels={labelsOrdenados}
        data={datosOrdenados}
        title={tituloGrafico}
        options={horizontalOptions}
      />
    </div>
  );
};

export default CausasEnTramitePorJuzgadoChart;

