import { type ReactNode } from 'react';

interface VerticalCarouselProps {
  children: ReactNode;
  className?: string;
}

/**
 * Componente de carrusel vertical con scroll snap
 * Permite navegar suavemente entre tarjetas con scroll vertical
 * 
 * @param children - Contenido del carrusel (tarjetas)
 * @param className - Clases CSS adicionales
 * 
 * @example
 * ```tsx
 * <VerticalCarousel>
 *   <ChartCard />
 *   <ChartCard />
 * </VerticalCarousel>
 * ```
 */
const VerticalCarousel = ({ children, className = '' }: VerticalCarouselProps) => {
  return (
    <div
      className={`
        overflow-y-auto
        scroll-smooth
        snap-y snap-mandatory
        space-y-12
        ${className}
      `}
      style={{
        scrollbarWidth: 'thin',
        scrollbarColor: '#E5E7EB #F3F4F6',
      }}
    >
      {Array.isArray(children)
        ? children.map((child, index) => (
            <div
              key={index}
              className="snap-start scroll-mt-8"
            >
              {child}
            </div>
          ))
        : <div className="snap-start scroll-mt-8">{children}</div>}
    </div>
  );
};

export default VerticalCarousel;

