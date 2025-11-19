# 📁 Estructura del Proyecto Frontend - Corrupción en Cifras

## 🗂️ Organización Actual

```
frontend/
├── src/
│   ├── App.tsx                    # Componente raíz (solo maneja el router)
│   ├── main.tsx                   # Punto de entrada de la aplicación
│   ├── index.css                  # Estilos globales (TailwindCSS)
│   │
│   ├── pages/                     # 📄 PÁGINAS (rutas principales)
│   │   ├── Dashboard.tsx          # Página principal (/)
│   │   └── AnalyticsPage.tsx      # Página de analytics (/analytics)
│   │
│   ├── components/                 # 🧩 COMPONENTES REUTILIZABLES
│   │   └── analytics/             # Componentes específicos de gráficos
│   │       ├── BarChart.tsx       # Gráfico de barras
│   │       ├── PieChart.tsx        # Gráfico de pie
│   │       └── LineChart.tsx       # Gráfico de línea
│   │
│   ├── services/                   # 🔌 SERVICIOS (llamadas al backend)
│   │   ├── api.ts                 # Funciones genéricas de API (get, post, etc.)
│   │   └── analytics.ts           # Funciones específicas para analytics
│   │
│   ├── types/                      # 📝 TIPOS TypeScript
│   │   └── analytics.ts           # Interfaces para respuestas del backend
│   │
│   ├── router/                     # 🛣️ RUTAS
│   │   └── index.tsx              # Configuración de React Router
│   │
│   ├── config/                     # ⚙️ CONFIGURACIONES
│   │   └── chart.ts               # Configuración de Chart.js
│   │
│   ├── hooks/                      # 🎣 CUSTOM HOOKS (vacío por ahora)
│   └── context/                    # 🗄️ CONTEXT API (vacío por ahora)
│
├── public/                         # Archivos estáticos
├── package.json                    # Dependencias del proyecto
├── vite.config.ts                  # Configuración de Vite
├── tailwind.config.js              # Configuración de TailwindCSS
└── tsconfig.json                   # Configuración de TypeScript
```

---

## 🔄 Flujo de Datos Actual

```
1. Usuario visita /analytics
   ↓
2. AnalyticsPage se monta (useEffect)
   ↓
3. Llama a funciones en services/analytics.ts
   ↓
4. services/analytics.ts usa services/api.ts
   ↓
5. api.ts hace fetch al backend (http://localhost:8000)
   ↓
6. Backend responde con datos JSON
   ↓
7. AnalyticsPage guarda datos en estados (useState)
   ↓
8. Renderiza componentes de gráficos (BarChart, PieChart, etc.)
```

---

## 📋 Cómo Está Organizado Actualmente

### 1. **Páginas (pages/)**
- **Dashboard.tsx**: Página de bienvenida (ruta `/`)
- **AnalyticsPage.tsx**: Página con todos los gráficos (ruta `/analytics`)
  - Muestra todos los gráficos uno debajo del otro
  - Carga todos los datos al montar el componente
  - Maneja estados de loading y error

### 2. **Componentes (components/)**
- **BarChart.tsx**: Gráfico de barras (Chart.js)
- **PieChart.tsx**: Gráfico de pie (Chart.js)
- **LineChart.tsx**: Gráfico de línea (Chart.js)

### 3. **Servicios (services/)**
- **api.ts**: Funciones genéricas para hacer peticiones HTTP
- **analytics.ts**: Funciones específicas para cada endpoint de analytics

### 4. **Tipos (types/)**
- **analytics.ts**: Interfaces TypeScript que coinciden con las respuestas del backend

### 5. **Router (router/)**
- Define las rutas de la aplicación
- Actualmente tiene 2 rutas: `/` y `/analytics`

---

## 🎯 Cómo Agregar Pestañas con Gráficos en la Misma Página

### Opción 1: Sistema de Pestañas Simple (Recomendado)

Puedes modificar `AnalyticsPage.tsx` para tener pestañas que organicen los gráficos por categorías.

#### Ejemplo de implementación:

```tsx
// AnalyticsPage.tsx con pestañas
import { useState } from 'react';

const AnalyticsPage = () => {
  const [activeTab, setActiveTab] = useState('general');

  const tabs = [
    { id: 'general', label: 'General' },
    { id: 'personas', label: 'Personas' },
    { id: 'fiscales', label: 'Fiscales' },
    { id: 'juzgados', label: 'Juzgados' },
  ];

  return (
    <div className="min-h-screen bg-gray-50 py-8">
      <div className="container mx-auto px-4">
        <h1 className="text-3xl font-bold text-gray-900 mb-8">
          Analytics - Corrupción en Cifras
        </h1>

        {/* Pestañas */}
        <div className="border-b border-gray-200 mb-6">
          <nav className="flex space-x-8">
            {tabs.map((tab) => (
              <button
                key={tab.id}
                onClick={() => setActiveTab(tab.id)}
                className={`py-4 px-1 border-b-2 font-medium text-sm ${
                  activeTab === tab.id
                    ? 'border-blue-500 text-blue-600'
                    : 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300'
                }`}
              >
                {tab.label}
              </button>
            ))}
          </nav>
        </div>

        {/* Contenido de las pestañas */}
        {activeTab === 'general' && (
          <div>
            {/* Gráficos generales */}
            <CasosPorEstado />
            <CausasIniciadasPorAno />
            <DelitosMasFrecuentes />
          </div>
        )}

        {activeTab === 'personas' && (
          <div>
            {/* Gráficos de personas */}
            <PersonasMasDenunciadas />
            <PersonasQueMasDenunciaron />
          </div>
        )}

        {activeTab === 'fiscales' && (
          <div>
            {/* Gráficos de fiscales */}
            <CausasPorFiscal />
          </div>
        )}

        {activeTab === 'juzgados' && (
          <div>
            {/* Gráficos de juzgados */}
            <CausasEnTramitePorJuzgado />
            <JuecesMayorDemora />
          </div>
        )}
      </div>
    </div>
  );
};
```

---

## 📝 Pasos para Agregar un Nuevo Gráfico

### Paso 1: Agregar el tipo TypeScript
**Archivo:** `src/types/analytics.ts`

```typescript
export interface NuevoGraficoResponse {
  datos_grafico: {
    labels: string[];
    data: number[];
    // ... otros campos
  };
}
```

### Paso 2: Agregar función de servicio
**Archivo:** `src/services/analytics.ts`

```typescript
export async function fetchNuevoGrafico(
  limit?: number
): Promise<NuevoGraficoResponse | null> {
  const response = await get<NuevoGraficoResponse>(
    `/analytics/nuevo-grafico${limit ? `?limit=${limit}` : ''}`
  );
  if (response.error || !response.data) {
    console.error('Error fetching nuevo grafico:', response.error);
    return null;
  }
  return response.data;
}
```

### Paso 3: Agregar estado y carga de datos
**Archivo:** `src/pages/AnalyticsPage.tsx`

```typescript
// En el useState
const [nuevoGrafico, setNuevoGrafico] = useState<NuevoGraficoResponse | null>(null);

// En el useEffect, dentro de Promise.all
const nuevoGraficoData = await fetchNuevoGrafico(20);
setNuevoGrafico(nuevoGraficoData);
```

### Paso 4: Renderizar el gráfico
**Archivo:** `src/pages/AnalyticsPage.tsx`

```tsx
<section className="mb-10">
  <h2 className="text-2xl font-bold mb-4">Nuevo Gráfico</h2>
  <div className="bg-white shadow rounded-lg p-6">
    {nuevoGrafico?.datos_grafico ? (
      <BarChart
        labels={nuevoGrafico.datos_grafico.labels}
        data={nuevoGrafico.datos_grafico.data}
        title="Título del gráfico"
      />
    ) : (
      <p className="text-gray-500">No hay datos disponibles</p>
    )}
  </div>
</section>
```

---

## 🎨 Mejoras Sugeridas

### 1. **Componente de Pestañas Reutilizable**
Crear `src/components/ui/Tabs.tsx` para reutilizar en otras páginas.

### 2. **Separar Gráficos en Componentes**
En lugar de tener todo en `AnalyticsPage.tsx`, crear componentes individuales:
- `src/components/analytics/CasosPorEstadoChart.tsx`
- `src/components/analytics/JuecesMayorDemoraChart.tsx`
- etc.

### 3. **Custom Hook para Datos**
Crear `src/hooks/useAnalytics.ts` para manejar la lógica de carga de datos:

```typescript
export function useAnalytics() {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    // Lógica de carga
  }, []);

  return { data, loading, error };
}
```

### 4. **Layout Component**
Crear un componente `Layout.tsx` para el header, navegación, etc.

---

## 🚀 Próximos Pasos Recomendados

1. **Implementar sistema de pestañas** en `AnalyticsPage.tsx`
2. **Agregar los gráficos faltantes** (causas-por-fuero, personas-mas-denunciadas, etc.)
3. **Crear componentes individuales** para cada gráfico
4. **Agregar navegación** entre páginas
5. **Mejorar el diseño** con un layout más profesional

