import { useAnalytics } from '@/hooks/useAnalytics';
import { fetchJuecesMayorDemora } from '@/services/analytics';
import type { JuecesMayorDemoraResponse } from '@/types/analytics';
import BarChart from '@/components/analytics/BarChart';

interface JuecesMayorDemoraChartProps {
  title?: string;
  limit?: number;
  className?: string;
}

/**
 * Componente completo para el gráfico de jueces con mayor demora
 */
const JuecesMayorDemoraChart = ({ 
  title = 'Jueces con Mayor Demora',
  limit = 10,
  className = '' 
}: JuecesMayorDemoraChartProps) => {
  const { data, loading, error } = useAnalytics<JuecesMayorDemoraResponse>(
    () => fetchJuecesMayorDemora(limit),
    [limit]
  );

  if (loading) {
    return (
      <div className={`bg-white border border-gray-200 shadow-md shadow-gray-200/60 rounded-xl p-8 hover:shadow-lg hover:-translate-y-0.5 transition-all duration-200 ${className}`}>
        <h2 className="text-2xl font-bold mb-4 text-[#1E3A8A] tracking-tight">{title}</h2>
        <div className="flex items-center justify-center h-64">
          <div className="text-center">
            <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-[#3B82F6] mx-auto mb-2"></div>
            <p className="text-gray-500 text-sm">Cargando datos...</p>
          </div>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className={`bg-white border border-gray-200 shadow-md shadow-gray-200/60 rounded-xl p-8 hover:shadow-lg hover:-translate-y-0.5 transition-all duration-200 ${className}`}>
        <h2 className="text-2xl font-bold mb-4 text-[#1E3A8A] tracking-tight">{title}</h2>
        <div className="bg-red-50 border border-red-200 rounded p-4">
          <p className="text-red-600 text-sm">{error}</p>
        </div>
      </div>
    );
  }

  if (!data?.datos_grafico) {
    return (
      <div className={`bg-white border border-gray-200 shadow-md shadow-gray-200/60 rounded-xl p-8 hover:shadow-lg hover:-translate-y-0.5 transition-all duration-200 ${className}`}>
        <h2 className="text-2xl font-bold mb-4 text-[#1E3A8A] tracking-tight">{title}</h2>
        <p className="text-gray-500">No hay datos disponibles</p>
      </div>
    );
  }

  return (
    <div className={`bg-white border border-gray-200 shadow-md shadow-gray-200/60 rounded-xl p-8 hover:shadow-lg hover:-translate-y-0.5 transition-all duration-200 ${className}`}>
      <h2 className="text-2xl font-bold mb-4 text-[#1E3A8A] tracking-tight">{title}</h2>
      <BarChart
        labels={data.datos_grafico.labels}
        data={data.datos_grafico.data}
        title="Demora promedio en días por juez"
      />
    </div>
  );
};

export default JuecesMayorDemoraChart;

