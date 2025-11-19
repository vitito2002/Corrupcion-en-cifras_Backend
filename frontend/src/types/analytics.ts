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
    data: number[];
    anos: Array<{
      anio: number;
      cantidad_causas: number;
    }>;
    total_causas: number;
    color?: string;
  };
}

export interface DelitosMasFrecuentesResponse {
  datos_grafico: {
    labels: string[];
    data: number[];
    delitos: Array<{
      delito: string;
      cantidad_causas: number;
    }>;
    total_causas: number;
    colores?: string[];
  };
}

export interface CausasEnTramitePorJuzgadoResponse {
  datos_grafico: {
    labels: string[];
    data: number[];
    juzgados: Array<{
      tribunal: string;
      cantidad_causas_en_tramite: number;
    }>;
    total_causas_en_tramite: number;
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
  };
}

