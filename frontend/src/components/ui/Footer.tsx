/**
 * Footer institucional premium visible en todas las páginas
 * Diseño profesional, elegante y con mejor estructura visual
 */
const Footer = () => {
  return (
    <footer className="bg-soft/30 border-t border-muted/30 mt-auto">
      <div className="max-w-6xl mx-auto px-8 py-8">
        <div className="flex flex-col md:flex-row items-center justify-between gap-4">
          <div className="flex flex-col items-center md:items-start">
            <p className="text-sm font-medium text-primary">
              Corrupción en Cifras
            </p>
            <p className="text-xs text-secondary mt-1">
              Proyecto UTDT + ACIJ
            </p>
          </div>
          <div className="text-xs text-secondary">
            © {new Date().getFullYear()} Todos los derechos reservados
          </div>
        </div>
      </div>
    </footer>
  );
};

export default Footer;

