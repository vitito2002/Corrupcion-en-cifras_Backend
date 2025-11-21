import { type ReactNode, useRef, useEffect, useState } from 'react';

export interface Tab {
  id: string;
  label: string;
  icon?: ReactNode;
  disabled?: boolean;
}

interface TabsProps {
  tabs: Tab[];
  activeTab: string;
  onTabChange: (tabId: string) => void;
  className?: string;
}

/**
 * Componente de pestañas reutilizable con animación de desplazamiento suave
 * 
 * @param tabs - Array de objetos Tab con id, label e icon opcional
 * @param activeTab - ID de la pestaña activa
 * @param onTabChange - Callback cuando se cambia de pestaña
 * @param className - Clases CSS adicionales para el contenedor
 * 
 * @example
 * ```tsx
 * <Tabs
 *   tabs={[
 *     { id: 'general', label: 'General' },
 *     { id: 'personas', label: 'Personas' },
 *   ]}
 *   activeTab={activeTab}
 *   onTabChange={setActiveTab}
 * />
 * ```
 */
const Tabs = ({ tabs, activeTab, onTabChange, className = '' }: TabsProps) => {
  const [indicatorStyle, setIndicatorStyle] = useState({ left: 0, width: 0 });
  const tabRefs = useRef<{ [key: string]: HTMLButtonElement | null }>({});
  const containerRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const activeTabElement = tabRefs.current[activeTab];
    const containerElement = containerRef.current;

    if (activeTabElement && containerElement) {
      const containerRect = containerElement.getBoundingClientRect();
      const tabRect = activeTabElement.getBoundingClientRect();
      
      setIndicatorStyle({
        left: tabRect.left - containerRect.left,
        width: tabRect.width,
      });
    }
  }, [activeTab, tabs]);

  return (
    <div 
      ref={containerRef}
      className={`
        relative inline-flex items-center gap-1 
        bg-soft/20 backdrop-blur-sm 
        border border-muted/30 
        rounded-xl 
        p-1.5
        ${className}
      `} 
      role="tablist" 
      aria-label="Analytics Tabs"
    >
      {/* Indicador animado */}
      <div
        className="absolute h-[calc(100%-0.75rem)] bg-[#4D7C8A] rounded-lg shadow-sm transition-all duration-300 ease-out"
        style={{
          left: `${indicatorStyle.left}px`,
          width: `${indicatorStyle.width}px`,
          top: '0.375rem',
        }}
      />

      {tabs.map((tab) => (
        <button
          key={tab.id}
          ref={(el) => {
            tabRefs.current[tab.id] = el;
          }}
          onClick={() => !tab.disabled && onTabChange(tab.id)}
          disabled={tab.disabled}
          className={`
            relative z-10 px-4 py-2 rounded-lg font-medium text-sm 
            transition-colors duration-200 ease-out
            ${
              activeTab === tab.id
                ? 'text-white'
                : tab.disabled
                ? 'text-muted/50 cursor-not-allowed opacity-50'
                : 'text-secondary hover:text-primary hover:bg-secondary/10'
            }
          `}
          aria-current={activeTab === tab.id ? 'page' : undefined}
          role="tab"
        >
          <div className="flex items-center gap-2">
            {tab.icon && <span className="w-4 h-4">{tab.icon}</span>}
            <span>{tab.label}</span>
          </div>
        </button>
      ))}
    </div>
  );
};

export default Tabs;

