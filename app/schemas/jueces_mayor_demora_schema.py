from pydantic import BaseModel
from typing import List


class JuezDemoraItem(BaseModel):
    """Item individual de juez con su demora"""
    juez_nombre: str
    tribunal_nombre: str
    demora_promedio_dias: float
    cantidad_expedientes: int
    label: str  # Juez + Tribunal para el gráfico


class DatosGraficoJuecesMayorDemora(BaseModel):
    """Schema con datos listos para graficar jueces con mayor demora"""
    labels: List[str]  # ['Juez 1 - Tribunal 1', 'Juez 2 - Tribunal 2', ...]
    data: List[float]  # [1234.56, 987.32, ...] - demora promedio en días
    cantidad_expedientes: List[int]  # [42, 35, ...] - cantidad de expedientes
    jueces: List[JuezDemoraItem]  # Datos completos de cada juez
    colores: List[str] = []  # Colores generados automáticamente


class JuecesMayorDemoraResponse(BaseModel):
    """Schema de respuesta para jueces con mayor demora - formato listo para gráficos"""
    datos_grafico: DatosGraficoJuecesMayorDemora
    
    class Config:
        from_attributes = True

