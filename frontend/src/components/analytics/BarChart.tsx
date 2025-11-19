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

  const defaultOptions: ChartOptions<'bar'> = {
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

  const options = customOptions 
    ? { ...defaultOptions, ...customOptions } 
    : defaultOptions;

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

