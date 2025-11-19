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
        borderColor: 'rgba(59, 130, 246, 1)',
        backgroundColor: 'rgba(59, 130, 246, 0.1)',
        borderWidth: 2,
        fill: true,
        tension: 0.4,
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
      },
      tooltip: {
        enabled: true,
      },
    },
    scales: {
      y: {
        beginAtZero: true,
      },
    },
  };

  return (
    <div className="p-4">
      <h3 className="text-xl font-semibold mb-3">{title}</h3>
      <div className="h-64">
        <Line data={chartData} options={options} />
      </div>
    </div>
  );
};

export default LineChart;

