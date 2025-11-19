import { createBrowserRouter } from 'react-router-dom';
import Dashboard from '@/pages/Dashboard';
import AnalyticsPage from '@/pages/AnalyticsPage';

export const router = createBrowserRouter([
  {
    path: '/',
    element: <Dashboard />,
  },
  {
    path: '/analytics',
    element: <AnalyticsPage />,
  },
]);

