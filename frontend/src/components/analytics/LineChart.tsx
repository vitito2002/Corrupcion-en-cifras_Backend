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
        borderColor: 'rgba(30, 58, 138, 1)',
        backgroundColor: 'rgba(59, 130, 246, 0.15)',
        borderWidth: 2.5,
        fill: true,
        tension: 0.4,
        pointBackgroundColor: 'rgba(59, 130, 246, 1)',
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

  return (
    <div className="p-2">
      <h3 className="text-lg font-semibold mb-4 text-[#1E3A8A] tracking-tight">{title}</h3>
      <div className="h-96">
        <Line data={chartData} options={options} />
      </div>
    </div>
  );
};

export default LineChart;

