import { Link } from 'react-router-dom';
import { Database, FileText, BarChart3 } from 'lucide-react';

/**
 * Landing page principal del proyecto Corrupción en Cifras
 * Página de presentación moderna y profesional
 */
const Dashboard = () => {
  return (
    <div className="min-h-screen pt-16 pb-16 bg-gradient-to-b from-soft/20 to-white">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        {/* Hero Section */}
        <div className="text-center mb-12 fade-in-up">
          <h1 
            className="text-6xl md:text-7xl lg:text-8xl font-bold tracking-tight text-primary mb-4"
            style={{ fontFamily: "'Playfair Display', Georgia, serif" }}
          >
            Corrupción en Cifras
          </h1>
          <p className="text-secondary text-xl max-w-3xl mx-auto leading-relaxed">
            Monitoreo, análisis y visualización de datos judiciales sobre causas de corrupción en Argentina.
          </p>
        </div>

        {/* CTA Button */}
        <div className="text-center mb-12 fade-in-up">
          <Link
            to="/analytics"
            className="inline-flex items-center gap-2 bg-[#1B4079] hover:bg-[#4D7C8A] text-white px-10 py-4 rounded-xl shadow-lg text-lg font-semibold transition-all duration-300 hover:shadow-xl hover:-translate-y-1 relative z-10"
          >
            Ir al Dashboard
            <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13 7l5 5m0 0l-5 5m5-5H6" />
            </svg>
          </Link>
        </div>

        {/* Features Section */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 fade-in-up">
          {/* Feature 1: Scraping Automático */}
          <div className="bg-white border-2 border-muted/30 p-6 rounded-2xl shadow-md hover:shadow-lg hover:-translate-y-1 transition-all duration-300 stagger-item">
            <div className="flex items-center justify-center w-12 h-12 bg-accent/30 rounded-xl mb-4">
              <Database className="w-6 h-6 text-primary" />
            </div>
            <h3 className="text-lg font-semibold text-primary mb-2 tracking-tight">
              Scraping Automático
            </h3>
            <p className="text-secondary text-sm leading-relaxed">
              Recolección automatizada de datos judiciales desde fuentes públicas, 
              garantizando actualización constante y exhaustiva de la información.
            </p>
          </div>

          {/* Feature 2: Normalización y ETL */}
          <div className="bg-white border-2 border-muted/30 p-6 rounded-2xl shadow-md hover:shadow-lg hover:-translate-y-1 transition-all duration-300 stagger-item">
            <div className="flex items-center justify-center w-12 h-12 bg-accent/30 rounded-xl mb-4">
              <FileText className="w-6 h-6 text-primary" />
            </div>
            <h3 className="text-lg font-semibold text-primary mb-2 tracking-tight">
              Normalización y ETL
            </h3>
            <p className="text-secondary text-sm leading-relaxed">
              Procesamiento y transformación de datos mediante técnicas de ETL, 
              asegurando consistencia y calidad en la información almacenada.
            </p>
          </div>

          {/* Feature 3: Visualizaciones Interactivas */}
          <div className="bg-white border-2 border-muted/30 p-6 rounded-2xl shadow-md hover:shadow-lg hover:-translate-y-1 transition-all duration-300 stagger-item">
            <div className="flex items-center justify-center w-12 h-12 bg-accent/30 rounded-xl mb-4">
              <BarChart3 className="w-6 h-6 text-primary" />
            </div>
            <h3 className="text-lg font-semibold text-primary mb-2 tracking-tight">
              Visualizaciones Interactivas
            </h3>
            <p className="text-secondary text-sm leading-relaxed">
              Gráficos y dashboards interactivos que permiten explorar los datos 
              de manera intuitiva y descubrir patrones en los casos de corrupción.
            </p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Dashboard;
