import { type ReactNode } from 'react';

interface StatsCardProps {
  title: string;
  value: string | number;
  icon?: ReactNode;
}

/**
 * Componente de tarjeta de estadísticas (KPI)
 * Diseñado para mostrar métricas clave en el dashboard
 * 
 * @param title - Título de la métrica
 * @param value - Valor de la métrica (puede ser string o number)
 * @param icon - Icono opcional a mostrar en un círculo azul suave
 * 
 * @example
 * ```tsx
 * <StatsCard 
 *   title="Total de causas" 
 *   value="2076" 
 *   icon={<ChartIcon />}
 * />
 * ```
 */
const StatsCard = ({ title, value, icon }: StatsCardProps) => {
  return (
    <div className="bg-white border border-gray-200 shadow-md shadow-gray-200/60 rounded-xl p-6 hover:shadow-lg transition-shadow">
      <div className="flex items-start justify-between">
        <div className="flex-1">
          <p className="text-gray-600 text-sm font-medium mb-2">{title}</p>
          <p className="text-3xl font-bold text-[#1E3A8A] tracking-tight">
            {value}
          </p>
        </div>
        {icon && (
          <div className="ml-4 flex-shrink-0">
            <div className="w-12 h-12 rounded-full bg-[#93C5FD] bg-opacity-20 flex items-center justify-center">
              <div className="text-[#3B82F6]">
                {icon}
              </div>
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

export default StatsCard;

