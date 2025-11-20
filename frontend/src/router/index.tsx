import { createBrowserRouter } from 'react-router-dom';
import Layout from '@/components/ui/Layout';
import Dashboard from '@/pages/Dashboard';
import AnalyticsPage from '@/pages/AnalyticsPage';
import MetodologiaPage from '@/pages/MetodologiaPage';

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
      {
        path: '/metodologia',
        element: <MetodologiaPage />,
      },
    ],
  },
]);

