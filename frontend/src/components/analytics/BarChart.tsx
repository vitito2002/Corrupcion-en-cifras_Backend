import '@/config/chart';
import { Bar } from 'react-chartjs-2';
import type { ChartOptions } from 'chart.js';

interface BarChartProps {
  labels: string[];
  data: number[];
  title: string;
  options?: ChartOptions<'bar'>;
}

const BarChart = ({ labels, data, title, options: customOptions }: BarChartProps) => {
  // Encontrar el índice del valor máximo
  const maxIndex = data.length > 0 
    ? data.reduce((maxIdx, current, idx, arr) => (current > arr[maxIdx] ? idx : maxIdx), 0)
    : -1;

  // Generar colores: naranja para el máximo, azul para el resto
  const backgroundColor = data.map((_, index) => 
    index === maxIndex 
      ? 'rgba(249, 115, 22, 0.7)' // Naranja (orange-500)
      : 'rgba(59, 130, 246, 0.7)' // Azul
  );

  const borderColor = data.map((_, index) => 
    index === maxIndex 
      ? 'rgba(234, 88, 12, 1)' // Naranja más oscuro para el borde
      : 'rgba(30, 58, 138, 1)' // Azul oscuro
  );

  const chartData = {
    labels,
    datasets: [
      {
        label: 'Cantidad',
        data,
        backgroundColor,
        borderColor,
        borderWidth: 1.5,
      },
    ],
  };

  const defaultOptions: ChartOptions<'bar'> = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: {
        display: false,
      },
      tooltip: {
        enabled: true,
        titleFont: {
          size: 14,
          weight: 'bold' as const,
        },
        bodyFont: {
          size: 13,
          weight: 'normal' as const,
        },
      },
    },
    scales: {
      x: {
        ticks: {
          font: {
            size: 13,
            weight: 'bold' as const,
          },
        },
      },
      y: {
        beginAtZero: true,
        ticks: {
          font: {
            size: 13,
            weight: 'bold' as const,
          },
        },
      },
    },
  };

  // Merge de opciones personalizadas con las opciones por defecto
  // Asegurar que los ticks mantengan el formato de fuente grande y negrita
  let options = defaultOptions;
  if (customOptions) {
    options = {
      ...defaultOptions,
      ...customOptions,
      scales: {
        ...defaultOptions.scales,
        ...(customOptions.scales || {}),
        x: {
          ...defaultOptions.scales?.x,
          ...(customOptions.scales?.x || {}),
          ticks: {
            ...defaultOptions.scales?.x?.ticks,
            ...(customOptions.scales?.x?.ticks || {}),
            font: {
              size: 13,
              weight: 'bold' as const,
            },
          },
        },
        y: {
          ...defaultOptions.scales?.y,
          ...(customOptions.scales?.y || {}),
          ticks: {
            ...defaultOptions.scales?.y?.ticks,
            ...(customOptions.scales?.y?.ticks || {}),
            font: {
              size: 13,
              weight: 'bold' as const,
            },
          },
        },
      },
    } as ChartOptions<'bar'>;
  }

  // Determinar altura según si es horizontal o vertical
  const isHorizontal = customOptions?.indexAxis === 'y';
  const chartHeight = isHorizontal ? 'h-[600px]' : 'h-96';

  return (
    <div className="p-2">
      <h3 className="text-lg font-semibold mb-4 text-[#1E3A8A] tracking-tight">{title}</h3>
      <div className={chartHeight}>
        <Bar data={chartData} options={options} />
      </div>
    </div>
  );
};

export default BarChart;

