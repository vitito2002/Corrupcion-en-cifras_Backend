import { type ReactNode } from 'react';

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
 * Componente de pestañas reutilizable
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
  return (
    <div className={`flex flex-wrap gap-2 ${className}`} role="tablist" aria-label="Analytics Tabs">
      {tabs.map((tab) => (
        <button
          key={tab.id}
          onClick={() => !tab.disabled && onTabChange(tab.id)}
          disabled={tab.disabled}
          className={`
            px-4 py-2 rounded-lg font-medium text-sm transition-all duration-200
            ${
              activeTab === tab.id
                ? 'text-blue-700 bg-blue-100 border border-blue-300 shadow-sm'
                : tab.disabled
                ? 'text-gray-400 cursor-not-allowed'
                : 'text-gray-500 hover:bg-gray-100 border border-transparent'
            }
          `}
          aria-current={activeTab === tab.id ? 'page' : undefined}
          role="tab"
        >
          <div className="flex items-center gap-2">
            {tab.icon && <span>{tab.icon}</span>}
            <span>{tab.label}</span>
          </div>
        </button>
      ))}
    </div>
  );
};

export default Tabs;

