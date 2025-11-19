import '@/config/chart';
import { Pie } from 'react-chartjs-2';

interface PieChartProps {
  labels: string[];
  data: number[];
  title: string;
}

const PieChart = ({ labels, data, title }: PieChartProps) => {
  // Paleta de colores Gobierno Moderno / Transparencia
  const colors = [
    'rgba(30, 58, 138, 0.7)',   // Azul oscuro
    'rgba(59, 130, 246, 0.7)',  // Azul principal
    'rgba(147, 197, 253, 0.7)', // Azul suave
    'rgba(16, 185, 129, 0.7)',  // Verde acento
    'rgba(229, 231, 235, 0.7)', // Gris medio
  ];
  
  const borderColors = [
    'rgba(30, 58, 138, 1)',
    'rgba(59, 130, 246, 1)',
    'rgba(147, 197, 253, 1)',
    'rgba(16, 185, 129, 1)',
    'rgba(229, 231, 235, 1)',
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
  };

  return (
    <div className="p-2">
      <h3 className="text-lg font-semibold mb-4 text-[#1E3A8A] tracking-tight">{title}</h3>
      <div className="h-96">
        <Pie data={chartData} options={options} />
      </div>
    </div>
  );
};

export default PieChart;

