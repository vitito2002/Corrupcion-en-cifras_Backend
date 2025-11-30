# Frontend - Corrupción en Cifras

Frontend del proyecto "Corrupción en Cifras" desarrollado con React, TypeScript, Vite y TailwindCSS.

## Descripción

Aplicación web de visualización de datos sobre casos de corrupción en Argentina. Proporciona dashboards interactivos con gráficos y análisis de datos.

## Requisitos

- Node.js 18+
- npm o yarn

## Instalación

```bash
npm install
```

## Desarrollo

```bash
npm run dev
```

La aplicación estará disponible en `http://localhost:5173`

## Build para Producción

```bash
npm run build
```

## Preview de Producción

```bash
npm run preview
```

## Estructura del Proyecto

```
src/
├── components/     # Componentes reutilizables
│   ├── analytics/  # Componentes de visualización
│   └── ui/         # Componentes de interfaz
├── pages/          # Páginas de la aplicación
├── services/       # Servicios API y lógica de negocio
├── types/          # Definiciones de tipos TypeScript
├── hooks/          # Custom React hooks
├── router/         # Configuración de rutas
└── context/        # Context API de React
```

## Tecnologías

- React 19 - Biblioteca de UI
- TypeScript - Tipado estático
- Vite - Build tool y dev server
- TailwindCSS - Framework CSS utility-first
- React Router DOM - Enrutamiento
- Chart.js - Visualización de gráficos

## API

El servicio API está configurado para conectarse al backend en `http://localhost:8000`.

### Uso del Servicio API

```typescript
import { get } from '@/services/api';

const response = await get('/analytics/casos-por-estado');
if (response.data) {
  // Procesar datos
}
```

## Estilos

El proyecto usa TailwindCSS con las fuentes Inter y Roboto. Los estilos base están configurados en `src/index.css`.

## Paths Absolutos

El proyecto está configurado para usar paths absolutos:

- `@/components` → `src/components`
- `@/pages` → `src/pages`
- `@/services` → `src/services`
- `@/types` → `src/types`
- `@/hooks` → `src/hooks`
- `@/router` → `src/router`
- `@/context` → `src/context`

## Configuración

- TypeScript: Configurado en `tsconfig.app.json`
- Vite: Configurado en `vite.config.ts`
- TailwindCSS: Configurado en `tailwind.config.js`
