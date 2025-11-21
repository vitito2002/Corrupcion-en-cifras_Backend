import { Link, useLocation } from 'react-router-dom';
import { useRef, useEffect, useState } from 'react';

/**
 * Header institucional premium visible en todas las páginas
 * Diseño moderno, elegante y profesional con navegación mejorada
 * Incluye animación de desplazamiento suave para el indicador activo
 */
const Header = () => {
  const location = useLocation();
  const [indicatorStyle, setIndicatorStyle] = useState({ left: 0, width: 0 });
  const linkRefs = useRef<{ [key: string]: HTMLAnchorElement | null }>({});
  const navRef = useRef<HTMLElement>(null);

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
      </nav>
    </header>
  );
};

export default Header;

