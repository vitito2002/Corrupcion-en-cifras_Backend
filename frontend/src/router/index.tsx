import { createBrowserRouter } from 'react-router-dom';
import Layout from '@/components/ui/Layout';
import Dashboard from '@/pages/Dashboard';
import AnalyticsPage from '@/pages/AnalyticsPage';

export const router = createBrowserRouter([
  {
    element: <Layout />,
    children: [
      {
        path: '/',
        element: <Dashboard />,
      },
      {
        path: '/analytics',
        element: <AnalyticsPage />,
      },
    ],
  },
]);

