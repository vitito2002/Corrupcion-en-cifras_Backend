import { useAnalytics } from '@/hooks/useAnalytics';
import { fetchDelitosMasFrecuentes } from '@/services/analytics';
import type { DelitosMasFrecuentesResponse } from '@/types/analytics';
import BarChart from '@/components/analytics/BarChart';

interface DelitosMasFrecuentesChartProps {
  title?: string;
  limit?: number;
  className?: string;
}

/**
 * Componente completo para el gráfico de delitos más frecuentes
 */
const DelitosMasFrecuentesChart = ({ 
  title = 'Delitos Más Frecuentes',
  limit = 10,
  className = '' 
}: DelitosMasFrecuentesChartProps) => {
  const { data, loading, error } = useAnalytics<DelitosMasFrecuentesResponse>(
    () => fetchDelitosMasFrecuentes(limit),
    [limit]
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
      <BarChart
        labels={data.datos_grafico.labels}
        data={data.datos_grafico.data}
        title="Top delitos por cantidad de causas"
      />
    </div>
  );
};

export default DelitosMasFrecuentesChart;

