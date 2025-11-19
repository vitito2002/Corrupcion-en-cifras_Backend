export type EstadoCausa = 'abiertas' | 'terminadas' | 'ambas';

interface EstadoCausaSwitchProps {
  estado: EstadoCausa;
  onChange: (estado: EstadoCausa) => void;
  className?: string;
}

/**
 * Componente Switch de 3 opciones para filtrar causas por estado
 * Similar al switch de CausasPorFiscalChart pero con 3 opciones
 * 
 * @param estado - Estado actual seleccionado ('abiertas', 'terminadas', 'ambas')
 * @param onChange - Callback cuando se cambia el estado
 * @param className - Clases CSS adicionales
 */
const EstadoCausaSwitch = ({ estado, onChange, className = '' }: EstadoCausaSwitchProps) => {
  return (
    <div className={`flex items-center space-x-2 ${className}`}>
      <button
        type="button"
        onClick={() => onChange('abiertas')}
        className={`
          px-3 py-1.5 rounded-lg text-sm font-medium transition-all duration-200
          ${estado === 'abiertas'
            ? 'bg-blue-100 text-blue-700 border border-blue-300 shadow-sm'
            : 'bg-gray-100 text-gray-500 hover:bg-gray-200 border border-transparent'
          }
        `}
      >
        Abiertas
      </button>
      <button
        type="button"
        onClick={() => onChange('terminadas')}
        className={`
          px-3 py-1.5 rounded-lg text-sm font-medium transition-all duration-200
          ${estado === 'terminadas'
            ? 'bg-blue-100 text-blue-700 border border-blue-300 shadow-sm'
            : 'bg-gray-100 text-gray-500 hover:bg-gray-200 border border-transparent'
          }
        `}
      >
        Terminadas
      </button>
      <button
        type="button"
        onClick={() => onChange('ambas')}
        className={`
          px-3 py-1.5 rounded-lg text-sm font-medium transition-all duration-200
          ${estado === 'ambas'
            ? 'bg-blue-100 text-blue-700 border border-blue-300 shadow-sm'
            : 'bg-gray-100 text-gray-500 hover:bg-gray-200 border border-transparent'
          }
        `}
      >
        Ambas
      </button>
    </div>
  );
};

export default EstadoCausaSwitch;

