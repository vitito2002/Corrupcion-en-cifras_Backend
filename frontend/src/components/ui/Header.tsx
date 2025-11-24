import { Link, useLocation } from 'react-router-dom';
import { useRef, useEffect, useState } from 'react';
import { downloadBaseZip } from '@/services/analytics';

/**
 * Header institucional premium visible en todas las páginas
 * Diseño moderno, elegante y profesional con navegación mejorada
 * Incluye animación de desplazamiento suave para el indicador activo
 */
const Header = () => {
  const location = useLocation();
  const [indicatorStyle, setIndicatorStyle] = useState({ left: 0, width: 0 });
  const [downloading, setDownloading] = useState(false);
  const linkRefs = useRef<{ [key: string]: HTMLAnchorElement | null }>({});
  const navRef = useRef<HTMLElement>(null);

  const handleExport = async () => {
    setDownloading(true);
    try {
      await downloadBaseZip();
    } catch (error) {
      console.error('Error al descargar:', error);
    } finally {
      setDownloading(false);
    }
  };

  const navLinks = [
    { path: '/', label: 'Inicio' },
    { path: '/analytics', label: 'Dashboard' },
    { path: '/metodologia', label: 'Metodología' },
  ];

  useEffect(() => {
    const activePath = location.pathname;
    const activeLink = linkRefs.current[activePath];
    const navElement = navRef.current;

    if (activeLink && navElement) {
      const navRect = navElement.getBoundingClientRect();
      const linkRect = activeLink.getBoundingClientRect();
      
      setIndicatorStyle({
        left: linkRect.left - navRect.left,
        width: linkRect.width,
      });
    }
  }, [location.pathname]);

  return (
    <header className="bg-white/80 backdrop-blur-sm border-b border-muted/30 shadow-sm h-20 flex items-center justify-between px-8 sticky top-0 z-50">
      {/* Logo / Nombre del proyecto */}
      <Link 
        to="/" 
        className="flex items-center group transition-opacity duration-200 hover:opacity-80"
      >
        <h1 className="text-2xl font-semibold text-primary tracking-tight">
          Corrupción en Cifras
        </h1>
      </Link>

      {/* Navegación */}
      <nav 
        ref={navRef}
        className="relative flex items-center space-x-1"
      >
        {/* Indicador animado */}
        <div
          className="absolute bottom-0 h-0.5 bg-[#4D7C8A] rounded-full transition-all duration-300 ease-out"
          style={{
            left: `${indicatorStyle.left}px`,
            width: `${indicatorStyle.width}px`,
          }}
        />

        {navLinks.map((link) => (
          <Link
            key={link.path}
            ref={(el) => {
              linkRefs.current[link.path] = el;
            }}
            to={link.path}
            className={`
              relative z-10 px-4 py-2 rounded-lg text-sm font-medium 
              transition-colors duration-200
              ${location.pathname === link.path
                ? 'text-primary'
                : 'text-secondary hover:text-primary hover:bg-secondary/10'
              }
            `}
          >
            {link.label}
          </Link>
        ))}

        {/* Botón de Exportación con Tooltip */}
        <div className="relative group ml-4">
          <button
            onClick={handleExport}
            disabled={downloading}
            className={`
              px-5 py-2 rounded-lg text-sm font-semibold
              transition-all duration-200 shadow-sm
              ${downloading
                ? 'bg-[#7F9C96] cursor-not-allowed text-white'
                : 'bg-[#1B4079] hover:bg-[#4D7C8A] text-white hover:shadow-md hover:-translate-y-0.5'
              }
              focus:outline-none focus:ring-2 focus:ring-[#1B4079] focus:ring-offset-2
            `}
          >
            {downloading ? 'Descargando...' : 'Exportación'}
          </button>
          
          {/* Tooltip - Abajo alineado a la derecha del botón */}
          {!downloading && (
            <div className="absolute top-full right-0 mt-2 px-4 py-2.5 bg-gray-900 text-white text-sm font-medium rounded-lg shadow-2xl opacity-0 group-hover:opacity-100 transition-all duration-200 pointer-events-none whitespace-nowrap z-[100] border border-gray-700 min-w-max">
              Descargar base de datos completa en formato ZIP
              <div className="absolute bottom-full right-4 -mb-1">
                <div className="border-4 border-transparent border-b-gray-900"></div>
              </div>
            </div>
          )}
        </div>
      </nav>
    </header>
  );
};

export default Header;

