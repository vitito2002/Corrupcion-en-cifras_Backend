from pydantic import BaseModel
from typing import List


class DatosGraficoEstadoProcesal(BaseModel):
    """Schema con datos listos para graficar casos por estado procesal"""
    labels: List[str]  # ['En trámite', 'Terminada']
    data: List[int]  # [264, 1807] - conteos
    porcentajes: List[float]  # [12.7, 87.3] - porcentajes
    total: int  # Total de casos
    colores: List[str] = ["#FF6384", "#36A2EB"]  # Colores sugeridos para el gráfico


class CasosPorEstadoProcesalResponse(BaseModel):
    """Schema de respuesta para casos por estado procesal - formato listo para gráficos"""
    datos_grafico: DatosGraficoEstadoProcesal
    
    class Config:
        from_attributes = True


class EstadisticasEstadoProcesalResponse(BaseModel):
    """Schema de respuesta para estadísticas de estado procesal"""
    total: int
    en_tramite: int
    terminada: int
    porcentaje_en_tramite: float
    porcentaje_terminada: float

