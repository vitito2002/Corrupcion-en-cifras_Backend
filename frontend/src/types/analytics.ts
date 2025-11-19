// Tipos para los endpoints de analytics

export interface CasosPorEstadoResponse {
  datos_grafico: {
    labels: string[];
    data: number[];
    porcentajes: number[];
    total: number;
    colores?: string[];
  };
}

export interface JuecesMayorDemoraResponse {
  datos_grafico: {
    labels: string[];
    data: number[];
    cantidad_expedientes: number[];
    jueces: Array<{
      juez_nombre: string;
      tribunal_nombre: string;
      demora_promedio_dias: number;
      cantidad_expedientes: number;
      label: string;
    }>;
    colores?: string[];
  };
}

export interface CausasIniciadasPorAnoResponse {
  datos_grafico: {
    labels: number[];
    causas_abiertas: number[];
    causas_terminadas: number[];
    data: number[];
    anos: Array<{
      anio: number;
      cantidad_causas_abiertas: number;
      cantidad_causas_terminadas: number;
      cantidad_causas: number;
    }>;
    total_causas_abiertas: number;
    total_causas_terminadas: number;
    total_causas: number;
    color?: string;
  };
}

export interface DelitosMasFrecuentesResponse {
  datos_grafico: {
    labels: string[];
    causas_abiertas: number[];
    causas_terminadas: number[];
    data: number[];
    delitos: Array<{
      delito: string;
      cantidad_causas_abiertas: number;
      cantidad_causas_terminadas: number;
      cantidad_causas: number;
    }>;
    total_causas_abiertas: number;
    total_causas_terminadas: number;
    total_causas: number;
    colores?: string[];
  };
}

export interface CausasEnTramitePorJuzgadoResponse {
  datos_grafico: {
    labels: string[];
    causas_abiertas: number[];
    causas_terminadas: number[];
    data: number[];
    juzgados: Array<{
      tribunal: string;
      cantidad_causas_abiertas: number;
      cantidad_causas_terminadas: number;
      cantidad_causas: number;
    }>;
    total_causas_abiertas: number;
    total_causas_terminadas: number;
    total_causas_en_tramite: number;
    total_causas: number;
    colores?: string[];
  };
}

export interface PersonasMasDenunciadasResponse {
  datos_grafico: {
    labels: string[];
    data: number[];
  };
}

export interface PersonasQueMasDenunciaronResponse {
  datos_grafico: {
    labels: string[];
    data: number[];
  };
}

export interface CausasPorFiscalResponse {
  datos_grafico: {
    labels: string[];
    causas_abiertas: number[];
    causas_terminadas: number[];
    fiscales: Array<{
      fiscal: string;
      causas_abiertas: number;
      causas_terminadas: number;
      total_causas: number;
    }>;
    total_causas_abiertas: number;
    total_causas_terminadas: number;
    total_causas: number;
  };
}

export interface DuracionInstruccionResponse {
  datos_grafico: {
    labels: string[];
    data: number[];
    causas: Array<{
      numero_expediente: string;
      caratula: string | null;
      tribunal: string | null;
      estado_procesal: string | null;
      fecha_inicio: string | null;
      fecha_ultimo_movimiento: string | null;
      duracion_dias: number;
    }>;
    duracion_promedio_dias: number;
    duracion_maxima_dias: number;
    duracion_minima_dias: number;
    total_causas: number;
  };
}

export interface CausasPorFueroResponse {
  datos_grafico: {
    labels: string[];
    causas_abiertas: number[];
    causas_terminadas: number[];
    data: number[];
    fueros: Array<{
      fuero: string;
      cantidad_causas_abiertas: number;
      cantidad_causas_terminadas: number;
      cantidad_causas: number;
    }>;
    total_causas_abiertas: number;
    total_causas_terminadas: number;
    total_causas: number;
  };
}

export interface DuracionOutliersResponse {
  datos_grafico: {
    causas_mas_largas: Array<{
      numero_expediente: string;
      caratula: string | null;
      tribunal: string | null;
      estado_procesal: string | null;
      fecha_inicio: string | null;
      fecha_ultimo_movimiento: string | null;
      duracion_dias: number;
      imputado_nombre: string | null;
    }>;
    causas_mas_cortas: Array<{
      numero_expediente: string;
      caratula: string | null;
      tribunal: string | null;
      estado_procesal: string | null;
      fecha_inicio: string | null;
      fecha_ultimo_movimiento: string | null;
      duracion_dias: number;
      imputado_nombre: string | null;
    }>;
  };
}

