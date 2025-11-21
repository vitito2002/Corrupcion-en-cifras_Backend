import { useAnalytics } from '@/hooks/useAnalytics';
import { fetchCasosPorEstado } from '@/services/analytics';
import type { CasosPorEstadoResponse } from '@/types/analytics';
import PieChart from '@/components/analytics/PieChart';

interface CasosPorEstadoChartProps {
  title?: string;
  className?: string;
}

/**
 * Componente completo para el gráfico de casos por estado procesal
 * Encapsula la carga de datos, manejo de estados y renderizado
 */
const CasosPorEstadoChart = ({ 
  title = 'Casos por Estado Procesal',
  className = '' 
}: CasosPorEstadoChartProps) => {
  const { data, loading, error } = useAnalytics<CasosPorEstadoResponse>(
    fetchCasosPorEstado,
    []
  );

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

  return (
    <div className={`bg-white border border-muted/30 shadow-md rounded-2xl p-8 hover:shadow-md-hover hover:-translate-y-0.5 transition-all duration-300 ${className}`}>
      <h2 className="text-2xl font-bold mb-4 text-primary tracking-tight">{title}</h2>
      <PieChart
        labels={data.datos_grafico.labels}
        data={data.datos_grafico.data}
        title="Distribución de casos por estado procesal"
      />
    </div>
  );
};

export default CasosPorEstadoChart;

