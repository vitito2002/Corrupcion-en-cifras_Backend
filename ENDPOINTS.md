# 📋 Listado de Endpoints - Corrupción en Cifras API

Base URL: `http://localhost:8000`

---

## 🔍 Endpoint de Verificación

### `GET /`
**Descripción:** Verificación de estado de la API

**Respuesta:**
```json
{
  "message": "API funcionando ✅"
}
```

---

## 📊 Endpoints de Analytics

Todos los endpoints de analytics tienen el prefijo `/analytics` y están agrupados bajo el tag `analytics`.

### 1. `GET /analytics/casos-por-estado`
**Descripción:** Obtener datos para gráfico de casos por estado procesal

**Parámetros:** Ninguno

**Respuesta:**
- `labels`: Lista de estados procesales ['En trámite', 'Terminada']
- `data`: Lista de conteos
- `porcentajes`: Lista de porcentajes
- `total`: Total de casos

**Uso:** Gráfico de pie o barras para mostrar distribución por estado procesal

---

### 2. `GET /analytics/jueces-mayor-demora`
**Descripción:** Obtener datos para gráfico de jueces con mayor demora promedio

**Parámetros:**
- `limit` (query, opcional): Número máximo de jueces a retornar (default: 10)

**Respuesta:**
- `labels`: Lista de labels ['Juez 1 - Tribunal 1', ...]
- `data`: Lista de demoras promedio en días
- `cantidad_expedientes`: Lista de cantidad de expedientes
- `jueces`: Lista completa con todos los datos de cada juez

**Uso:** Gráfico de barras para mostrar jueces con mayor demora

---

### 3. `GET /analytics/causas-iniciadas-por-ano`
**Descripción:** Obtener datos para gráfico de causas iniciadas por año

**Parámetros:** Ninguno

**Respuesta:**
- `labels`: Lista de años [2010, 2011, 2012, ...]
- `data`: Lista de cantidad de causas por año
- `anos`: Lista completa con todos los datos de cada año
- `total_causas`: Total de causas en todos los años

**Uso:** Gráfico de línea temporal o barras por año

---

### 4. `GET /analytics/delitos-mas-frecuentes`
**Descripción:** Obtener datos para gráfico de delitos más frecuentes

**Parámetros:**
- `limit` (query, opcional): Número máximo de delitos a retornar (default: 10)

**Respuesta:**
- `labels`: Lista de nombres de delitos
- `data`: Lista de cantidad de causas por delito
- `delitos`: Lista completa con todos los datos de cada delito
- `total_causas`: Total de causas en todos los delitos

**Uso:** Gráfico de barras horizontales o pie chart

---

### 5. `GET /analytics/causas-en-tramite-por-juzgado`
**Descripción:** Obtener cantidad de causas en trámite por juzgado

**Parámetros:**
- `limit` (query, opcional): Número máximo de juzgados a retornar (default: 20)

**Respuesta:**
- `labels`: Lista de nombres de juzgados/tribunales
- `data`: Lista de cantidad de causas en trámite por juzgado
- `juzgados`: Lista completa con todos los datos de cada juzgado
- `total_causas_en_tramite`: Total general de causas en trámite

**Uso:** Gráfico de barras horizontales o verticales

---

### 6. `GET /analytics/duracion-instruccion`
**Descripción:** Obtener duración de instrucción de causas

**Parámetros:**
- `limit` (query, opcional): Número máximo de causas a retornar (default: 50)

**Respuesta:**
- `labels`: Lista de carátulas o números de expediente
- `data`: Lista de duración en días
- `causas`: Lista completa con todos los datos de cada causa
- `duracion_promedio_dias`: Duración promedio en días
- `duracion_maxima_dias`: Duración máxima en días
- `duracion_minima_dias`: Duración mínima en días
- `total_causas`: Total de causas analizadas

**Uso:** Gráfico de barras ordenadas por duración

---

### 7. `GET /analytics/causas-por-fuero`
**Descripción:** Obtener distribución de causas por fuero judicial

**Parámetros:** Ninguno

**Respuesta:**
- `labels`: Lista de nombres de fueros judiciales
- `data`: Lista de cantidad de causas por fuero
- `fueros`: Lista completa con todos los datos de cada fuero
- `total_causas`: Total general de causas

**Uso:** Gráfico de barras o pie chart

---

### 8. `GET /analytics/personas-mas-denunciadas`
**Descripción:** Obtener personas más denunciadas

**Parámetros:**
- `limit` (query, opcional): Número máximo de personas a retornar (default: 20)

**Respuesta:**
- `labels`: Lista de nombres de personas
- `data`: Lista de cantidad de causas por persona
- `personas`: Lista completa con todos los datos de cada persona
- `total_causas`: Total general de causas

**Uso:** Gráfico de barras horizontales o verticales

---

### 9. `GET /analytics/personas-que-mas-denunciaron`
**Descripción:** Obtener personas que más denunciaron (denunciantes y querellantes)

**Parámetros:**
- `limit` (query, opcional): Número máximo de personas a retornar (default: 20)

**Respuesta:**
- `labels`: Lista de nombres de personas
- `data`: Lista de cantidad de denuncias por persona
- `personas`: Lista completa con todos los datos de cada persona
- `total_denuncias`: Total general de denuncias

**Uso:** Gráfico de barras horizontales o verticales

---

### 10. `GET /analytics/causas-por-fiscal`
**Descripción:** Obtener cantidad de causas por fiscal clasificadas por abiertas y terminadas

**Parámetros:**
- `limit` (query, opcional): Número máximo de fiscales a retornar (default: 20)

**Respuesta:**
- `labels`: Lista de nombres de fiscales
- `causas_abiertas`: Lista de cantidad de causas abiertas (En trámite) por fiscal
- `causas_terminadas`: Lista de cantidad de causas terminadas por fiscal
- `fiscales`: Lista completa con todos los datos de cada fiscal
- `total_causas_abiertas`: Total general de causas abiertas
- `total_causas_terminadas`: Total general de causas terminadas
- `total_causas`: Total general de causas

**Uso:** Gráfico de barras agrupadas o apiladas

---

## 📥 Endpoints de Exportación

### 11. `GET /exportacion/descargar-base-de-datos`
**Descripción:** Descargar base de datos completa en formato ZIP

**Parámetros:** Ninguno

**Respuesta:**
- Archivo ZIP con todas las tablas exportadas como CSV
- Nombre del archivo: `base_corrupcion.zip`
- Tablas incluidas: fuero, jurisdiccion, tribunal, secretaria, expediente, radicacion, resolucion, parte, rol_parte, letrado, representacion, expediente_delito, tipo_delito, plazo, juez, tribunal_juez

**Uso:** Descarga completa de la base de datos para análisis externo

---

## 📝 Resumen

| # | Endpoint | Método | Parámetros | Descripción |
|---|----------|--------|------------|-------------|
| 1 | `/` | GET | - | Verificación de estado |
| 2 | `/analytics/casos-por-estado` | GET | - | Casos por estado procesal |
| 3 | `/analytics/jueces-mayor-demora` | GET | `limit` (opcional) | Jueces con mayor demora |
| 4 | `/analytics/causas-iniciadas-por-ano` | GET | - | Causas iniciadas por año |
| 5 | `/analytics/delitos-mas-frecuentes` | GET | `limit` (opcional) | Delitos más frecuentes |
| 6 | `/analytics/causas-en-tramite-por-juzgado` | GET | `limit` (opcional) | Causas en trámite por juzgado |
| 7 | `/analytics/duracion-instruccion` | GET | `limit` (opcional) | Duración de instrucción |
| 8 | `/analytics/causas-por-fuero` | GET | - | Causas por fuero judicial |
| 9 | `/analytics/personas-mas-denunciadas` | GET | `limit` (opcional) | Personas más denunciadas |
| 10 | `/analytics/personas-que-mas-denunciaron` | GET | `limit` (opcional) | Personas que más denunciaron |
| 11 | `/analytics/causas-por-fiscal` | GET | `limit` (opcional) | Causas por fiscal (abiertas/terminadas) |
| 12 | `/exportacion/descargar-base-de-datos` | GET | - | Descargar BD completa (ZIP) |

**Total: 12 endpoints**

---

## 🔗 Documentación Interactiva

Una vez que el servidor esté corriendo, puedes acceder a la documentación interactiva de FastAPI en:

- **Swagger UI:** `http://localhost:8000/docs`
- **ReDoc:** `http://localhost:8000/redoc`

