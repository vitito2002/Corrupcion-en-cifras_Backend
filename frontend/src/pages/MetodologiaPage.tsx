/**
 * Página de Metodología
 * Explica el proceso de scraping, normalización de datos y construcción de la base
 */
const MetodologiaPage = () => {
  return (
    <div className="py-12">
      <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
        <h1 className="text-5xl md:text-6xl font-bold text-primary mb-6 tracking-tight leading-tight" style={{ fontFamily: "'Playfair Display', Georgia, serif" }}>
          Metodología
        </h1>
        
        <div className="space-y-8">
          <div className="bg-white border border-muted/30 shadow-md rounded-2xl p-8 hover:shadow-lg transition-all duration-300">
            <h2 className="text-2xl font-bold mb-4 text-primary tracking-tight">Proceso de Recolección de Datos</h2>
            <p className="text-gray-700 leading-relaxed mb-4">
              Aquí irá el texto explicando la metodología, el proceso de scraping, 
              normalización de datos, construcción de la base, y cómo se generan 
              las visualizaciones. Esto debe ser solo texto estático, 
              sin componentes adicionales.
            </p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default MetodologiaPage;

