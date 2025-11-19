const Dashboard = () => {
  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-50 to-gray-100">
      <div className="container mx-auto px-4 py-16">
        <div className="text-center">
          <h1 className="text-5xl font-bold text-gray-900 mb-4">
            Corrupción en Cifras
          </h1>
          <p className="text-xl text-gray-600 mb-8">
            Dashboard de visualizaciones sobre casos de corrupción
          </p>
          
          <div className="mt-12 bg-white rounded-lg shadow-lg p-8 max-w-2xl mx-auto">
            <h2 className="text-2xl font-semibold text-gray-800 mb-4">
              Bienvenido
            </h2>
            <p className="text-gray-600">
              Este es el dashboard principal. Aquí se mostrarán los gráficos y visualizaciones
              de los datos de corrupción.
            </p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Dashboard;

