import { useMemo } from 'react';
import { useAnalytics } from '@/hooks/useAnalytics';
import { fetchDuracionInstruccion } from '@/services/analytics';
import type { DuracionInstruccionResponse } from '@/types/analytics';
import { scaleTime, scaleLinear } from '@visx/scale';
import { AxisBottom, AxisLeft } from '@visx/axis';
import { useTooltip, TooltipWithBounds } from '@visx/tooltip';
import { localPoint } from '@visx/event';

interface DuracionTimelineProps {
  title?: string;
  limit?: number;
  className?: string;
}

interface TimelinePoint {
  x: Date;
  y: number;
  causa: DuracionInstruccionResponse['datos_grafico']['causas'][0];
}

const DuracionTimeline = ({
  title = 'Duración de Instrucción - Timeline',
  limit,
  className = '',
}: DuracionTimelineProps) => {
  const { data, loading, error } = useAnalytics<DuracionInstruccionResponse>(
    () => fetchDuracionInstruccion(limit),
    limit !== undefined ? [limit] : []
  );

  const {
    tooltipData,
    tooltipLeft,
    tooltipTop,
    tooltipOpen,
    showTooltip,
    hideTooltip,
  } = useTooltip<TimelinePoint>();

  // Dimensiones del gráfico
  const width = 800;
  const height = 400;
  const margin = { top: 20, right: 20, bottom: 60, left: 60 };

  // Procesar datos para el timeline
  const timelineData = useMemo(() => {
    if (!data?.datos_grafico?.causas) return [];

    return data.datos_grafico.causas
      .filter((causa) => causa.fecha_inicio && causa.fecha_ultimo_movimiento)
      .map((causa) => ({
        x: new Date(causa.fecha_inicio!),
        y: causa.duracion_dias,
        causa,
      }))
      .sort((a, b) => a.x.getTime() - b.x.getTime());
  }, [data]);

  // Escalas
  const xScale = useMemo(() => {
    if (timelineData.length === 0) return null;

    const dates = timelineData.map((d) => d.x);
    return scaleTime({
      domain: [Math.min(...dates.map((d) => d.getTime())), Math.max(...dates.map((d) => d.getTime()))],
      range: [margin.left, width - margin.right],
    });
  }, [timelineData, width, margin]);

  const yScale = useMemo(() => {
    if (timelineData.length === 0) return null;

    const durations = timelineData.map((d) => d.y);
    return scaleLinear({
      domain: [0, Math.max(...durations) * 1.1],
      range: [height - margin.bottom, margin.top],
    });
  }, [timelineData, height, margin]);

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

  if (!data?.datos_grafico || timelineData.length === 0) {
    return (
      <div className={`bg-white border border-muted/30 shadow-md rounded-2xl p-8 hover:shadow-md-hover hover:-translate-y-0.5 transition-all duration-300 ${className}`}>
        <h2 className="text-2xl font-bold mb-4 text-primary tracking-tight">{title}</h2>
        <p className="text-gray-500">No hay datos disponibles</p>
      </div>
    );
  }

  if (!xScale || !yScale) {
    return (
      <div className={`bg-white border border-muted/30 shadow-md rounded-2xl p-8 hover:shadow-md-hover hover:-translate-y-0.5 transition-all duration-300 ${className}`}>
        <h2 className="text-2xl font-bold mb-4 text-primary tracking-tight">{title}</h2>
        <p className="text-gray-500">Error al procesar los datos</p>
      </div>
    );
  }

  return (
    <div className={`bg-white border border-muted/30 shadow-md rounded-2xl p-8 hover:shadow-md-hover hover:-translate-y-0.5 transition-all duration-300 ${className}`}>
      <h2 className="text-2xl font-bold mb-4 text-primary tracking-tight">{title}</h2>
      <div className="overflow-x-auto">
        <svg width={width} height={height} className="overflow-visible">
          {/* Eje X - Tiempo */}
          <AxisBottom
            top={height - margin.bottom}
            left={margin.left}
            scale={xScale}
            numTicks={6}
            stroke="#6B7280"
            tickStroke="#6B7280"
            tickLabelProps={{
              fill: '#6B7280',
              fontSize: 11,
              textAnchor: 'middle',
            }}
          />

          {/* Eje Y - Duración */}
          <AxisLeft
            left={margin.left}
            scale={yScale}
            numTicks={5}
            stroke="#6B7280"
            tickStroke="#6B7280"
            tickLabelProps={{
              fill: '#6B7280',
              fontSize: 11,
              textAnchor: 'end',
              dx: -5,
            }}
          />

          {/* Puntos del timeline */}
          {timelineData.map((point, i) => {
            const x = xScale(point.x);
            const y = yScale(point.y);

            return (
              <g key={i}>
                <circle
                  cx={x}
                  cy={y}
                  r={4}
                  fill="#3B82F6"
                  stroke="#1E3A8A"
                  strokeWidth={1.5}
                  style={{ cursor: 'pointer' }}
                  onMouseMove={(e) => {
                    const coords = localPoint(e);
                    if (coords) {
                      showTooltip({
                        tooltipLeft: coords.x,
                        tooltipTop: coords.y,
                        tooltipData: point,
                      });
                    }
                  }}
                  onMouseLeave={hideTooltip}
                />
              </g>
            );
          })}
        </svg>
      </div>

      {/* Tooltip */}
      {tooltipOpen && tooltipData && (
        <TooltipWithBounds
          left={tooltipLeft}
          top={tooltipTop}
          style={{
            backgroundColor: 'rgba(0, 0, 0, 0.85)',
            color: 'white',
            padding: '8px 12px',
            borderRadius: '6px',
            fontSize: '12px',
            pointerEvents: 'none',
          }}
        >
          <div>
            <div className="font-semibold mb-1">
              {tooltipData.causa.caratula || tooltipData.causa.numero_expediente}
            </div>
            <div className="text-xs opacity-90">
              <div>Expediente: {tooltipData.causa.numero_expediente}</div>
              {tooltipData.causa.tribunal && <div>Tribunal: {tooltipData.causa.tribunal}</div>}
              <div>Duración: {tooltipData.causa.duracion_dias} días</div>
              {tooltipData.causa.fecha_inicio && (
                <div>Inicio: {new Date(tooltipData.causa.fecha_inicio).toLocaleDateString()}</div>
              )}
              {tooltipData.causa.fecha_ultimo_movimiento && (
                <div>Último movimiento: {new Date(tooltipData.causa.fecha_ultimo_movimiento).toLocaleDateString()}</div>
              )}
            </div>
          </div>
        </TooltipWithBounds>
      )}

      {/* Leyenda */}
      <div className="mt-4 text-sm text-gray-600">
        <p>Total de causas: {data.datos_grafico.total_causas}</p>
        <p>Duración promedio: {data.datos_grafico.duracion_promedio_dias.toFixed(1)} días</p>
      </div>
    </div>
  );
};

export default DuracionTimeline;

