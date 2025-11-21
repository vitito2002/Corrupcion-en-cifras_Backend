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
    <div className="bg-[#4D7C8A] border border-muted/30 shadow-md rounded-2xl p-6 hover:shadow-lg hover:-translate-y-0.5 transition-all duration-300 ease-out">
      <div className="flex items-start justify-between">
        <div className="flex-1 min-w-0">
          <p className="text-white/80 text-xs font-medium uppercase tracking-wider mb-3">
            {title}
          </p>
          <p className="text-3xl font-bold text-white tracking-tight">
            {value}
          </p>
        </div>
        {icon && (
          <div className="ml-4 flex-shrink-0">
            <div className="w-12 h-12 rounded-xl bg-white/20 flex items-center justify-center">
              <div className="text-white w-5 h-5">
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

