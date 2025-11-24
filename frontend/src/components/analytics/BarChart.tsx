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
  // Generar colores: primary y secondary alternados
  // Convertir hex a rgba: #1B4079 = rgb(27, 64, 121), #4D7C8A = rgb(77, 124, 138)
  const backgroundColor = data.map((_, index) => 
    index % 2 === 0 
      ? 'rgba(27, 64, 121, 0.7)' // Primary (Yale Blue)
      : 'rgba(77, 124, 138, 0.7)' // Secondary (Air Force Blue)
  );

  const borderColor = data.map((_, index) => 
    index % 2 === 0
      ? 'rgba(27, 64, 121, 1)' // Primary
      : 'rgba(77, 124, 138, 1)' // Secondary
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
        backgroundColor: 'rgba(27, 64, 121, 0.9)', // Primary con opacidad
        titleColor: '#FFFFFF',
        bodyColor: '#FFFFFF',
        titleFont: {
          size: 14,
          weight: 'bold' as const,
        },
        bodyFont: {
          size: 13,
          weight: 'normal' as const,
        },
        padding: 12,
        cornerRadius: 8,
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
      <h3 className="text-lg font-semibold mb-4 text-primary tracking-tight">{title}</h3>
      <div className={chartHeight}>
        <Bar data={chartData} options={options} />
      </div>
    </div>
  );
};

export default BarChart;

