import '@/config/chart';
import { Bar } from 'react-chartjs-2';

interface BarChartProps {
  labels: string[];
  data: number[];
  title: string;
}

const BarChart = ({ labels, data, title }: BarChartProps) => {
  const chartData = {
    labels,
    datasets: [
      {
        label: 'Cantidad',
        data,
        backgroundColor: 'rgba(59, 130, 246, 0.6)',
        borderColor: 'rgba(59, 130, 246, 1)',
        borderWidth: 1,
      },
    ],
  };

  const options = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: {
        display: false,
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
        <Bar data={chartData} options={options} />
      </div>
    </div>
  );
};

export default BarChart;

