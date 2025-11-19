# Frontend - Corrupción en Cifras

Frontend del proyecto "Corrupción en Cifras" desarrollado con React, TypeScript, Vite y TailwindCSS.

## 🚀 Inicio Rápido

### Instalación

```bash
npm install
```

### Desarrollo

```bash
npm run dev
```

La aplicación estará disponible en `http://localhost:5173`

### Build para Producción

```bash
npm run build
```

### Preview de Producción

```bash
npm run preview
```

## 📁 Estructura del Proyecto

```
src/
├── components/     # Componentes reutilizables
├── pages/          # Páginas de la aplicación
├── services/       # Servicios API y lógica de negocio
├── types/          # Definiciones de tipos TypeScript
├── hooks/          # Custom React hooks
├── router/         # Configuración de rutas
└── context/        # Context API de React
```

## 🛠️ Tecnologías

- **React 19** - Biblioteca de UI
- **TypeScript** - Tipado estático
- **Vite** - Build tool y dev server
- **TailwindCSS** - Framework CSS utility-first
- **React Router DOM** - Enrutamiento

## 📡 API

El servicio API está configurado para conectarse al backend en `http://localhost:8000`.

### Uso del Servicio API

```typescript
import { get } from '@/services/api';

// Ejemplo de uso
const response = await get('/analytics/casos-por-estado');
if (response.data) {
  // Procesar datos
}
```

## 🎨 Estilos

El proyecto usa TailwindCSS con las fuentes Inter y Roboto. Los estilos base están configurados en `src/index.css`.

## 📝 Paths Absolutos

El proyecto está configurado para usar paths absolutos:

- `@/components` → `src/components`
- `@/pages` → `src/pages`
- `@/services` → `src/services`
- `@/types` → `src/types`
- `@/hooks` → `src/hooks`
- `@/router` → `src/router`
- `@/context` → `src/context`

## 🔧 Configuración

- **TypeScript**: Configurado en `tsconfig.app.json`
- **Vite**: Configurado en `vite.config.ts`
- **TailwindCSS**: Configurado en `tailwind.config.js`
