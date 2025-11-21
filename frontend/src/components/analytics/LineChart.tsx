import '@/config/chart';
import { Line } from 'react-chartjs-2';

interface LineChartProps {
  labels: (string | number)[];
  data: number[];
  title: string;
}

const LineChart = ({ labels, data, title }: LineChartProps) => {
  const chartData = {
    labels: labels.map(String),
    datasets: [
      {
        label: 'Cantidad de causas',
        data,
        borderColor: 'rgba(27, 64, 121, 1)', // Primary (Yale Blue)
        backgroundColor: 'rgba(27, 64, 121, 0.15)', // Primary con opacidad baja
        borderWidth: 2.5,
        fill: true,
        tension: 0.4,
        pointBackgroundColor: 'rgba(27, 64, 121, 1)', // Primary
        pointBorderColor: '#FFFFFF',
        pointBorderWidth: 2,
        pointRadius: 4,
      },
    ],
  };

  const options = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: {
        display: true,
        position: 'top' as const,
        labels: {
          font: {
            size: 14,
            weight: 'bold' as const,
          },
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

  return (
    <div className="p-2">
      <h3 className="text-lg font-semibold mb-4 text-primary tracking-tight">{title}</h3>
      <div className="h-96">
        <Line data={chartData} options={options} />
      </div>
    </div>
  );
};

export default LineChart;

