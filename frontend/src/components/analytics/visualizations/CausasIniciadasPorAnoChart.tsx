import { useAnalytics } from '@/hooks/useAnalytics';
import { fetchCausasIniciadasPorAno } from '@/services/analytics';
import type { CausasIniciadasPorAnoResponse } from '@/types/analytics';
import LineChart from '@/components/analytics/LineChart';

interface CausasIniciadasPorAnoChartProps {
  title?: string;
  className?: string;
}

/**
 * Componente completo para el gráfico de causas iniciadas por año
 */
const CausasIniciadasPorAnoChart = ({ 
  title = 'Causas Iniciadas por Año',
  className = '' 
}: CausasIniciadasPorAnoChartProps) => {
  const { data, loading, error } = useAnalytics<CausasIniciadasPorAnoResponse>(
    fetchCausasIniciadasPorAno,
    []
  );

  if (loading) {
    return (
      <div className={`bg-white shadow rounded-lg p-6 ${className}`}>
        <h2 className="text-2xl font-bold mb-4">{title}</h2>
        <div className="flex items-center justify-center h-64">
          <div className="text-center">
            <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-blue-600 mx-auto mb-2"></div>
            <p className="text-gray-500 text-sm">Cargando datos...</p>
          </div>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className={`bg-white shadow rounded-lg p-6 ${className}`}>
        <h2 className="text-2xl font-bold mb-4">{title}</h2>
        <div className="bg-red-50 border border-red-200 rounded p-4">
          <p className="text-red-600 text-sm">{error}</p>
        </div>
      </div>
    );
  }

  if (!data?.datos_grafico) {
    return (
      <div className={`bg-white shadow rounded-lg p-6 ${className}`}>
        <h2 className="text-2xl font-bold mb-4">{title}</h2>
        <p className="text-gray-500">No hay datos disponibles</p>
      </div>
    );
  }

  return (
    <div className={`bg-white shadow rounded-lg p-6 ${className}`}>
      <h2 className="text-2xl font-bold mb-4">{title}</h2>
      <LineChart
        labels={data.datos_grafico.labels}
        data={data.datos_grafico.data}
        title="Evolución temporal de causas iniciadas"
      />
    </div>
  );
};

export default CausasIniciadasPorAnoChart;

