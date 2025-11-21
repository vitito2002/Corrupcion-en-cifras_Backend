import { Outlet } from 'react-router-dom';
import Header from './Header';
import Footer from './Footer';

/**
 * Layout principal que envuelve todas las páginas
 * Incluye el header y footer institucionales
 */
const Layout = () => {
  return (
    <div className="min-h-screen bg-gray-50 flex flex-col">
      <Header />
      <main className="flex-1">
        <Outlet />
      </main>
      <Footer />
    </div>
  );
};

export default Layout;

