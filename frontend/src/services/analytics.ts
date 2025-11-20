import { get } from '@/services/api';
import type {
  CasosPorEstadoResponse,
  JuecesMayorDemoraResponse,
  CausasIniciadasPorAnoResponse,
  DelitosMasFrecuentesResponse,
  CausasEnTramitePorJuzgadoResponse,
  PersonasMasDenunciadasResponse,
  PersonasQueMasDenunciaronResponse,
  CausasPorFiscalResponse,
  DuracionInstruccionResponse,
  CausasPorFueroResponse,
  DuracionOutliersResponse,
} from '@/types/analytics';

/**
 * Obtiene los casos por estado procesal
 */
export async function fetchCasosPorEstado(): Promise<CasosPorEstadoResponse | null> {
  const response = await get<CasosPorEstadoResponse>('/analytics/casos-por-estado');
  if (response.error || !response.data) {
    console.error('Error fetching casos por estado:', response.error);
    return null;
  }
  return response.data;
}

/**
 * Obtiene los jueces con mayor demora
 */
export async function fetchJuecesMayorDemora(
  limit: number = 10
): Promise<JuecesMayorDemoraResponse | null> {
  const response = await get<JuecesMayorDemoraResponse>(
    `/analytics/jueces-mayor-demora?limit=${limit}`
  );
  if (response.error || !response.data) {
    console.error('Error fetching jueces mayor demora:', response.error);
    return null;
  }
  return response.data;
}

/**
 * Obtiene las causas iniciadas por año
 */
export async function fetchCausasIniciadasPorAno(): Promise<CausasIniciadasPorAnoResponse | null> {
  const response = await get<CausasIniciadasPorAnoResponse>('/analytics/causas-iniciadas-por-ano');
  if (response.error || !response.data) {
    console.error('Error fetching causas iniciadas por año:', response.error);
    return null;
  }
  return response.data;
}

/**
 * Obtiene los delitos más frecuentes
 */
export async function fetchDelitosMasFrecuentes(
  limit: number = 10
): Promise<DelitosMasFrecuentesResponse | null> {
  const response = await get<DelitosMasFrecuentesResponse>(
    `/analytics/delitos-mas-frecuentes?limit=${limit}`
  );
  if (response.error || !response.data) {
    console.error('Error fetching delitos mas frecuentes:', response.error);
    return null;
  }
  return response.data;
}

/**
 * Obtiene las causas en trámite por juzgado
 */
export async function fetchCausasEnTramitePorJuzgado(
  limit: number = 20
): Promise<CausasEnTramitePorJuzgadoResponse | null> {
  const response = await get<CausasEnTramitePorJuzgadoResponse>(
    `/analytics/causas-en-tramite-por-juzgado?limit=${limit}`
  );
  if (response.error || !response.data) {
    console.error('Error fetching causas en tramite por juzgado:', response.error);
    return null;
  }
  return response.data;
}

/**
 * Obtiene las personas más denunciadas
 */
export async function fetchPersonasMasDenunciadas(
  limit?: number
): Promise<PersonasMasDenunciadasResponse | null> {
  const endpoint = limit 
    ? `/analytics/personas-mas-denunciadas?limit=${limit}`
    : '/analytics/personas-mas-denunciadas';
  const response = await get<PersonasMasDenunciadasResponse>(endpoint);
  if (response.error || !response.data) {
    console.error('Error fetching personas mas denunciadas:', response.error);
    return null;
  }
  return response.data;
}

/**
 * Obtiene las personas que más denunciaron
 */
export async function fetchPersonasQueMasDenunciaron(
  limit?: number
): Promise<PersonasQueMasDenunciaronResponse | null> {
  const endpoint = limit 
    ? `/analytics/personas-que-mas-denunciaron?limit=${limit}`
    : '/analytics/personas-que-mas-denunciaron';
  const response = await get<PersonasQueMasDenunciaronResponse>(endpoint);
  if (response.error || !response.data) {
    console.error('Error fetching personas que mas denunciaron:', response.error);
    return null;
  }
  return response.data;
}

/**
 * Obtiene las causas por fiscal
 */
export async function fetchCausasPorFiscal(
  limit?: number
): Promise<CausasPorFiscalResponse | null> {
  const endpoint = limit 
    ? `/analytics/causas-por-fiscal?limit=${limit}`
    : '/analytics/causas-por-fiscal';
  const response = await get<CausasPorFiscalResponse>(endpoint);
  if (response.error || !response.data) {
    console.error('Error fetching causas por fiscal:', response.error);
    return null;
  }
  return response.data;
}

/**
 * Obtiene la duración de instrucción de causas
 */
export async function fetchDuracionInstruccion(
  limit?: number
): Promise<DuracionInstruccionResponse | null> {
  const endpoint = limit 
    ? `/analytics/duracion-instruccion?limit=${limit}`
    : '/analytics/duracion-instruccion';
  const response = await get<DuracionInstruccionResponse>(endpoint);
  if (response.error || !response.data) {
    console.error('Error fetching duracion instruccion:', response.error);
    return null;
  }
  return response.data;
}

/**
 * Obtiene las causas por fuero judicial
 */
export async function fetchCausasPorFuero(): Promise<CausasPorFueroResponse | null> {
  const response = await get<CausasPorFueroResponse>('/analytics/causas-por-fuero');
  if (response.error || !response.data) {
    console.error('Error fetching causas por fuero:', response.error);
    return null;
  }
  return response.data;
}

/**
 * Obtiene los outliers de duración de instrucción (top más largos y más cortos)
 */
export async function fetchDuracionOutliers(
  limit?: number
): Promise<DuracionOutliersResponse | null> {
  const endpoint = limit 
    ? `/analytics/duracion-outliers?limit=${limit}`
    : '/analytics/duracion-outliers';
  const response = await get<DuracionOutliersResponse>(endpoint);
  if (response.error || !response.data) {
    console.error('Error fetching duracion outliers:', response.error);
    return null;
  }
  return response.data;
}

/**
 * Descarga la base de datos completa como archivo ZIP
 */
export async function downloadBaseZip(): Promise<void> {
  try {
    const API_BASE_URL = 'http://localhost:8000';
    const response = await fetch(`${API_BASE_URL}/exportacion/descargar-base-de-datos`, {
      method: 'GET',
    });

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    // Convertir la respuesta a blob
    const blob = await response.blob();

    // Crear Object URL
    const url = window.URL.createObjectURL(blob);

    // Crear un elemento <a> temporal para descargar
    const link = document.createElement('a');
    link.href = url;
    
    // Obtener el nombre del archivo del header Content-Disposition o usar uno por defecto
    const contentDisposition = response.headers.get('Content-Disposition');
    let filename = 'base_corrupcion.zip';
    if (contentDisposition) {
      const filenameMatch = contentDisposition.match(/filename="?(.+)"?/i);
      if (filenameMatch) {
        filename = filenameMatch[1];
      }
    }
    
    link.download = filename;
    document.body.appendChild(link);
    link.click();

    // Limpiar
    document.body.removeChild(link);
    window.URL.revokeObjectURL(url);
  } catch (error) {
    console.error('Error downloading base ZIP:', error);
    throw error;
  }
}

