from pydantic import BaseModel
from typing import List


class AnioCausaItem(BaseModel):
    """Item individual de año con cantidad de causas"""
    anio: int
    cantidad_causas: int


class DatosGraficoCausasPorAno(BaseModel):
    """Schema con datos listos para graficar causas iniciadas por año"""
    labels: List[int]  # [2010, 2011, 2012, ...] - años
    data: List[int]  # [45, 67, 89, ...] - cantidad de causas por año
    anos: List[AnioCausaItem]  # Datos completos de cada año
    total_causas: int  # Total de causas en todos los años


class CausasIniciadasPorAnoResponse(BaseModel):
    """Schema de respuesta para causas iniciadas por año - formato listo para gráficos"""
    datos_grafico: DatosGraficoCausasPorAno
    
    class Config:
        from_attributes = True

