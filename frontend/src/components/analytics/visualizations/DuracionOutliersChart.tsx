import { useAnalytics } from '@/hooks/useAnalytics';
import { fetchDuracionOutliers } from '@/services/analytics';
import type { DuracionOutliersResponse } from '@/types/analytics';
import BarChart from '@/components/analytics/BarChart';

interface DuracionOutliersChartProps {
  title?: string;
  limit?: number;
  className?: string;
}

/**
 * Componente completo para el gráfico de outliers de duración de instrucción
 * Muestra dos gráficos: uno para las causas más largas y otro para las más cortas
 */
const DuracionOutliersChart = ({ 
  title = 'Outliers de Duración de Instrucción',
  limit = 5,
  className = '' 
}: DuracionOutliersChartProps) => {
  const { data, loading, error } = useAnalytics<DuracionOutliersResponse>(
    () => fetchDuracionOutliers(limit),
    limit !== undefined ? [limit] : []
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

  // Preparar datos para gráficos de barras horizontales
  const causasMasLargas = data.datos_grafico.causas_mas_largas;
  const causasMasCortas = data.datos_grafico.causas_mas_cortas;

  // Labels para causas más largas (usar nombre del imputado)
  const labelsMasLargas = causasMasLargas.map(causa => {
    const nombre = causa.imputado_nombre || 'Sin imputado';
    return nombre.length > 50 ? nombre.substring(0, 47) + '...' : nombre;
  });
  const dataMasLargas = causasMasLargas.map(causa => causa.duracion_dias);

  // Labels para causas más cortas (usar nombre del imputado)
  const labelsMasCortas = causasMasCortas.map(causa => {
    const nombre = causa.imputado_nombre || 'Sin imputado';
    return nombre.length > 50 ? nombre.substring(0, 47) + '...' : nombre;
  });
  const dataMasCortas = causasMasCortas.map(causa => causa.duracion_dias);

  // Función helper para formatear fecha
  const formatearFecha = (fecha: string | null) => {
    if (!fecha) return 'N/A';
    try {
      const date = new Date(fecha);
      return date.toLocaleDateString('es-AR', { year: 'numeric', month: 'short', day: 'numeric' });
    } catch {
      return fecha;
    }
  };

  // Opciones para gráficos horizontales con tooltips mejorados
  const createHorizontalOptions = (causas: typeof causasMasLargas) => {
    return {
    indexAxis: 'y' as const,
    plugins: {
      legend: { display: false },
      tooltip: { 
        enabled: true,
        backgroundColor: 'rgba(0, 0, 0, 0.8)',
        padding: 12,
        titleFont: {
          size: 14,
          weight: 'bold' as const,
        },
        bodyFont: {
          size: 13,
        },
        callbacks: {
          title: (tooltipItems: any[]) => {
            const index = tooltipItems[0].dataIndex;
            const causa = causas[index];
            return causa?.imputado_nombre || 'Sin imputado';
          },
          label: (context: any) => {
            const index = context.dataIndex;
            const causa = causas[index];
            if (!causa) return [];
            
            const labels = [];
            labels.push(`Duración: ${causa.duracion_dias} días`);
            if (causa.caratula) {
              labels.push(`Carátula: ${causa.caratula}`);
            }
            if (causa.numero_expediente) {
              labels.push(`Expediente: ${causa.numero_expediente}`);
            }
            if (causa.tribunal) {
              labels.push(`Tribunal: ${causa.tribunal}`);
            }
            if (causa.estado_procesal) {
              labels.push(`Estado: ${causa.estado_procesal}`);
            }
            if (causa.fecha_inicio) {
              labels.push(`Inicio: ${formatearFecha(causa.fecha_inicio)}`);
            }
            if (causa.fecha_ultimo_movimiento) {
              labels.push(`Último movimiento: ${formatearFecha(causa.fecha_ultimo_movimiento)}`);
            }
            return labels;
          },
        },
      },
    },
    scales: {
      x: {
        beginAtZero: true,
        title: {
          display: true,
          text: 'Duración (días)',
          font: {
            size: 13,
            weight: 'bold' as const,
          },
        },
        ticks: {
          font: {
            size: 13,
            weight: 'bold' as const,
          },
        },
      },
      y: {
        ticks: {
          autoSkip: false,
          padding: 10,
          font: {
            size: 13,
            weight: 'bold' as const,
          },
        },
      },
    },
    };
  };

  return (
    <div className={`space-y-8 ${className}`}>
      {/* Causas más largas */}
      <div className="bg-white border border-gray-200 shadow-md shadow-gray-200/60 rounded-xl p-8 hover:shadow-lg hover:-translate-y-0.5 transition-all duration-200">
        <h3 className="text-xl font-bold mb-4 text-[#1E3A8A] tracking-tight">
          Top {limit} Causas con Mayor Duración
        </h3>
        {causasMasLargas.length > 0 ? (
          <BarChart
            labels={labelsMasLargas}
            data={dataMasLargas}
            title="Duración en días"
            options={createHorizontalOptions(causasMasLargas)}
          />
        ) : (
          <p className="text-gray-500">No hay datos disponibles</p>
        )}
      </div>

      {/* Causas más cortas */}
      <div className="bg-white border border-gray-200 shadow-md shadow-gray-200/60 rounded-xl p-8 hover:shadow-lg hover:-translate-y-0.5 transition-all duration-200">
        <h3 className="text-xl font-bold mb-4 text-[#1E3A8A] tracking-tight">
          Top {limit} Causas con Menor Duración
        </h3>
        {causasMasCortas.length > 0 ? (
          <BarChart
            labels={labelsMasCortas}
            data={dataMasCortas}
            title="Duración en días"
            options={createHorizontalOptions(causasMasCortas)}
          />
        ) : (
          <p className="text-gray-500">No hay datos disponibles</p>
        )}
      </div>
    </div>
  );
};

export default DuracionOutliersChart;

