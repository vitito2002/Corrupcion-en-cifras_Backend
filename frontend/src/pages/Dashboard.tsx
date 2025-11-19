import { Link } from 'react-router-dom';
import { Database, FileText, BarChart3 } from 'lucide-react';

/**
 * Landing page principal del proyecto Corrupción en Cifras
 * Página de presentación moderna y profesional
 */
const Dashboard = () => {
  return (
    <div className="bg-gray-50 min-h-screen pt-20 pb-20">
      <div className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
        {/* Hero Section */}
        <div className="text-center mb-16">
          <h1 
            className="text-5xl font-bold tracking-tight text-[#1E3A8A] mb-4"
            style={{ fontFamily: "'Playfair Display', Georgia, serif" }}
          >
            Corrupción en Cifras
          </h1>
          <p className="text-gray-600 text-lg max-w-2xl mx-auto mt-4">
            Monitoreo, análisis y visualización de datos judiciales sobre causas de corrupción en Argentina.
          </p>
        </div>

        {/* CTA Button */}
        <div className="text-center mb-20">
          <Link
            to="/analytics"
            className="inline-block bg-blue-600 hover:bg-blue-700 text-white px-8 py-4 rounded-xl mt-10 shadow-md text-xl font-semibold transition-all duration-200 hover:shadow-lg hover:-translate-y-0.5"
          >
            Ir al Dashboard
          </Link>
        </div>

        {/* Features Section */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8 mt-16">
          {/* Feature 1: Scraping Automático */}
          <div className="bg-white border border-gray-200 p-6 rounded-xl shadow-sm hover:shadow-md transition-all duration-200">
            <div className="flex items-center justify-center w-12 h-12 bg-blue-100 rounded-lg mb-4">
              <Database className="w-6 h-6 text-blue-600" />
            </div>
            <h3 className="text-xl font-semibold text-[#1E3A8A] mb-3">
              Scraping Automático
            </h3>
            <p className="text-gray-600 text-sm leading-relaxed">
              Recolección automatizada de datos judiciales desde fuentes públicas, 
              garantizando actualización constante y exhaustiva de la información.
            </p>
          </div>

          {/* Feature 2: Normalización y ETL */}
          <div className="bg-white border border-gray-200 p-6 rounded-xl shadow-sm hover:shadow-md transition-all duration-200">
            <div className="flex items-center justify-center w-12 h-12 bg-blue-100 rounded-lg mb-4">
              <FileText className="w-6 h-6 text-blue-600" />
            </div>
            <h3 className="text-xl font-semibold text-[#1E3A8A] mb-3">
              Normalización y ETL
            </h3>
            <p className="text-gray-600 text-sm leading-relaxed">
              Procesamiento y transformación de datos mediante técnicas de ETL, 
              asegurando consistencia y calidad en la información almacenada.
            </p>
          </div>

          {/* Feature 3: Visualizaciones Interactivas */}
          <div className="bg-white border border-gray-200 p-6 rounded-xl shadow-sm hover:shadow-md transition-all duration-200">
            <div className="flex items-center justify-center w-12 h-12 bg-blue-100 rounded-lg mb-4">
              <BarChart3 className="w-6 h-6 text-blue-600" />
            </div>
            <h3 className="text-xl font-semibold text-[#1E3A8A] mb-3">
              Visualizaciones Interactivas
            </h3>
            <p className="text-gray-600 text-sm leading-relaxed">
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
