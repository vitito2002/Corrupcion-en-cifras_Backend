import { useAnalytics } from '@/hooks/useAnalytics';
import { fetchPersonasMasDenunciadas } from '@/services/analytics';
import type { PersonasMasDenunciadasResponse } from '@/types/analytics';
import BarChart from '@/components/analytics/BarChart';

interface PersonasMasDenunciadasChartProps {
  title?: string;
  limit?: number;
  className?: string;
}

/**
 * Componente completo para el gráfico de personas más denunciadas
 */
const PersonasMasDenunciadasChart = ({ 
  title = 'Personas Más Denunciadas',
  limit,
  className = '' 
}: PersonasMasDenunciadasChartProps) => {
  const { data, loading, error } = useAnalytics<PersonasMasDenunciadasResponse>(
    () => fetchPersonasMasDenunciadas(limit),
    limit !== undefined ? [limit] : []
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

  // Filtrar valores NaN, null, undefined o vacíos
  const filteredLabels: string[] = [];
  const filteredData: number[] = [];
  
  data.datos_grafico.labels.forEach((label, index) => {
    const value = data.datos_grafico.data[index];
    // Validar que label y value sean válidos
    if (
      label && 
      label !== 'NaN' && 
      label.trim() !== '' &&
      typeof value === 'number' && 
      !isNaN(value) && 
      isFinite(value) &&
      value > 0
    ) {
      filteredLabels.push(label);
      filteredData.push(value);
    }
  });

  if (filteredLabels.length === 0) {
    return (
      <div className={`bg-white border border-muted/30 shadow-md rounded-2xl p-8 hover:shadow-md-hover hover:-translate-y-0.5 transition-all duration-300 ${className}`}>
        <h2 className="text-2xl font-bold mb-4 text-primary tracking-tight">{title}</h2>
        <p className="text-gray-500">No hay datos válidos disponibles</p>
      </div>
    );
  }

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
      <h2 className="text-2xl font-bold mb-4 text-primary tracking-tight">{title}</h2>
      <BarChart
        labels={filteredLabels}
        data={filteredData}
        title="Cantidad de causas por persona denunciada"
        options={horizontalOptions}
      />
    </div>
  );
};

export default PersonasMasDenunciadasChart;

