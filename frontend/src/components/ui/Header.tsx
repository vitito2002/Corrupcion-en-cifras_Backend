import { Link, useLocation } from 'react-router-dom';

/**
 * Header institucional visible en todas las páginas
 * Diseño moderno y minimalista con navegación
 */
const Header = () => {
  const location = useLocation();

  const isActive = (path: string) => {
    return location.pathname === path;
  };

  return (
    <header className="bg-white border-b border-gray-200 shadow-sm h-16 flex items-center justify-between px-6 sticky top-0 z-50">
      {/* Logo / Nombre del proyecto */}
      <Link to="/" className="flex items-center">
        <h1 className="text-xl font-semibold text-[#1E3A8A] tracking-tight">
          Corrupción en Cifras
        </h1>
      </Link>

      {/* Navegación */}
      <nav className="flex items-center space-x-6">
        <Link
          to="/"
          className={`
            text-sm font-medium transition-colors duration-200
            ${isActive('/')
              ? 'text-[#3B82F6] border-b-2 border-[#3B82F6] pb-1'
              : 'text-gray-600 hover:text-[#3B82F6]'
            }
          `}
        >
          Inicio
        </Link>
        <Link
          to="/analytics"
          className={`
            text-sm font-medium transition-colors duration-200
            ${isActive('/analytics')
              ? 'text-[#3B82F6] border-b-2 border-[#3B82F6] pb-1'
              : 'text-gray-600 hover:text-[#3B82F6]'
            }
          `}
        >
          Dashboard
        </Link>
      </nav>
    </header>
  );
};

export default Header;

