import { useState } from 'react';
import { useAnalytics } from '@/hooks/useAnalytics';
import { fetchCausasPorFiscal } from '@/services/analytics';
import type { CausasPorFiscalResponse } from '@/types/analytics';
import BarChart from '@/components/analytics/BarChart';

interface CausasPorFiscalChartProps {
  title?: string;
  limit?: number;
  className?: string;
}

type TipoCausa = 'abiertas' | 'terminadas';

/**
 * Componente completo para el gráfico de causas por fiscal
 * Incluye un switch para alternar entre causas abiertas y terminadas
 */
const CausasPorFiscalChart = ({ 
  title = 'Causas por Fiscal',
  limit,
  className = '' 
}: CausasPorFiscalChartProps) => {
  const [tipoCausa, setTipoCausa] = useState<TipoCausa>('abiertas');
  
  const { data, loading, error } = useAnalytics<CausasPorFiscalResponse>(
    () => fetchCausasPorFiscal(limit),
    limit !== undefined ? [limit] : []
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

  if (!data?.datos_grafico || data.datos_grafico.labels.length === 0) {
    return (
      <div className={`bg-white shadow rounded-lg p-6 ${className}`}>
        <h2 className="text-2xl font-bold mb-4">{title}</h2>
        <p className="text-gray-500">No hay datos disponibles</p>
      </div>
    );
  }

  // Seleccionar los datos según el tipo de causa seleccionado
  const datosGrafico = tipoCausa === 'abiertas' 
    ? data.datos_grafico.causas_abiertas 
    : data.datos_grafico.causas_terminadas;

  const tituloGrafico = tipoCausa === 'abiertas'
    ? 'Cantidad de causas abiertas por fiscal'
    : 'Cantidad de causas terminadas por fiscal';

  return (
    <div className={`bg-white shadow rounded-lg p-6 ${className}`}>
      <div className="flex items-center justify-between mb-4">
        <h2 className="text-2xl font-bold">{title}</h2>
        
        {/* Switch para alternar entre abiertas y terminadas */}
        <div className="flex items-center space-x-3">
          <span className={`text-sm font-medium ${tipoCausa === 'abiertas' ? 'text-blue-600' : 'text-gray-500'}`}>
            Abiertas
          </span>
          <button
            type="button"
            className={`relative inline-flex h-6 w-11 items-center rounded-full transition-colors focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 ${
              tipoCausa === 'terminadas' ? 'bg-blue-600' : 'bg-gray-300'
            }`}
            onClick={() => setTipoCausa(tipoCausa === 'abiertas' ? 'terminadas' : 'abiertas')}
            role="switch"
            aria-checked={tipoCausa === 'terminadas'}
            aria-label="Alternar entre causas abiertas y terminadas"
          >
            <span
              className={`inline-block h-4 w-4 transform rounded-full bg-white transition-transform ${
                tipoCausa === 'terminadas' ? 'translate-x-6' : 'translate-x-1'
              }`}
            />
          </button>
          <span className={`text-sm font-medium ${tipoCausa === 'terminadas' ? 'text-blue-600' : 'text-gray-500'}`}>
            Terminadas
          </span>
        </div>
      </div>
      
      <BarChart
        labels={data.datos_grafico.labels}
        data={datosGrafico}
        title={tituloGrafico}
      />
    </div>
  );
};

export default CausasPorFiscalChart;

