import { useState } from 'react';
import { useAnalytics } from '@/hooks/useAnalytics';
import { fetchCausasIniciadasPorAno } from '@/services/analytics';
import type { CausasIniciadasPorAnoResponse } from '@/types/analytics';
import type { EstadoCausa } from '@/components/ui/EstadoCausaSwitch';
import EstadoCausaSwitch from '@/components/ui/EstadoCausaSwitch';
import LineChart from '@/components/analytics/LineChart';

interface CausasIniciadasPorAnoChartProps {
  title?: string;
  className?: string;
}

/**
 * Componente completo para el gráfico de causas iniciadas por año
 * Incluye un switch para alternar entre causas abiertas, terminadas y ambas
 */
const CausasIniciadasPorAnoChart = ({ 
  title = 'Causas Iniciadas por Año',
  className = '' 
}: CausasIniciadasPorAnoChartProps) => {
  const [estado, setEstado] = useState<EstadoCausa>('ambas');
  
  const { data, loading, error } = useAnalytics<CausasIniciadasPorAnoResponse>(
    fetchCausasIniciadasPorAno,
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

  // Seleccionar los datos según el estado seleccionado
  const datosGrafico = estado === 'abiertas'
    ? data.datos_grafico.causas_abiertas
    : estado === 'terminadas'
    ? data.datos_grafico.causas_terminadas
    : data.datos_grafico.data;

  // Calcular el máximo global entre todas las opciones para fijar la escala
  const maxAbiertas = Math.max(...data.datos_grafico.causas_abiertas, 0);
  const maxTerminadas = Math.max(...data.datos_grafico.causas_terminadas, 0);
  const maxAmbas = Math.max(...data.datos_grafico.data, 0);
  const maxGlobal = Math.max(maxAbiertas, maxTerminadas, maxAmbas);
  // Agregar un pequeño margen (10%) para mejor visualización
  const maxY = Math.ceil(maxGlobal * 1.1);

  const tituloGrafico = estado === 'abiertas'
    ? 'Evolución temporal de causas abiertas iniciadas'
    : estado === 'terminadas'
    ? 'Evolución temporal de causas terminadas iniciadas'
    : 'Evolución temporal de causas iniciadas';

  // Opciones para fijar la escala del eje Y
  const chartOptions = {
    scales: {
      y: {
        max: maxY,
      },
    },
  };

  return (
    <div className={`bg-white border border-muted/30 shadow-md rounded-2xl p-8 hover:shadow-md-hover hover:-translate-y-0.5 transition-all duration-300 ${className}`}>
      <div className="flex items-center justify-between mb-4">
        <h2 className="text-2xl font-bold text-primary tracking-tight">{title}</h2>
        <EstadoCausaSwitch estado={estado} onChange={setEstado} />
      </div>
      <LineChart
        labels={data.datos_grafico.labels}
        data={datosGrafico}
        title={tituloGrafico}
        options={chartOptions}
      />
    </div>
  );
};

export default CausasIniciadasPorAnoChart;

