import { type ReactNode } from 'react';

interface CardProps {
  children: ReactNode;
  className?: string;
  hover?: boolean;
  padding?: 'sm' | 'md' | 'lg';
}

/**
 * Componente Card premium reutilizable
 * Diseño consistente para todas las tarjetas del dashboard
 * 
 * @param children - Contenido de la tarjeta
 * @param className - Clases CSS adicionales
 * @param hover - Activar efecto hover premium (default: true)
 * @param padding - Tamaño del padding (sm: 1.5rem, md: 2rem, lg: 2.5rem)
 */
const Card = ({ 
  children, 
  className = '', 
  hover = true,
  padding = 'md'
}: CardProps) => {
  const paddingClasses = {
    sm: 'p-6',
    md: 'p-8',
    lg: 'p-10',
  };

  const hoverClasses = hover
    ? 'hover:shadow-lg hover:-translate-y-0.5 hover:border-primary/40'
    : '';

  return (
    <div
      className={`
        bg-white 
        border border-muted/30 
        rounded-2xl 
        shadow-md
        transition-all duration-300 ease-out
        ${paddingClasses[padding]}
        ${hoverClasses}
        ${className}
      `}
    >
      {children}
    </div>
  );
};

export default Card;

