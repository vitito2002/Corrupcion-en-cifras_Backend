import '@/config/chart';
import { Pie } from 'react-chartjs-2';

interface PieChartProps {
  labels: string[];
  data: number[];
  title: string;
}

const PieChart = ({ labels, data, title }: PieChartProps) => {
  // Nueva paleta de colores: primary, secondary, muted, soft, accent
  // Convertir hex a rgba: #1B4079, #4D7C8A, #7F9C96, #8FAD88, #CBDF90
  const colors = [
    'rgba(27, 64, 121, 0.7)',   // Primary (Yale Blue)
    'rgba(77, 124, 138, 0.7)',  // Secondary (Air Force Blue)
    'rgba(127, 156, 150, 0.7)', // Muted (Cambridge Blue)
    'rgba(143, 173, 136, 0.7)', // Soft (Cambridge Green)
    'rgba(203, 223, 144, 0.7)', // Accent (Mindaro)
  ];
  
  const borderColors = [
    'rgba(27, 64, 121, 1)',
    'rgba(77, 124, 138, 1)',
    'rgba(127, 156, 150, 1)',
    'rgba(143, 173, 136, 1)',
    'rgba(203, 223, 144, 1)',
  ];

  const chartData = {
    labels,
    datasets: [
      {
        data,
        backgroundColor: colors.slice(0, data.length),
        borderColor: borderColors.slice(0, data.length),
        borderWidth: 1.5,
      },
    ],
  };

  const options = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: {
        position: 'right' as const,
        labels: {
          font: {
            size: 14,
            weight: 'bold' as const,
          },
          padding: 15,
        },
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
  };

  return (
    <div className="p-2">
      <h3 className="text-lg font-semibold mb-4 text-primary tracking-tight">{title}</h3>
      <div className="h-96">
        <Pie data={chartData} options={options} />
      </div>
    </div>
  );
};

export default PieChart;

