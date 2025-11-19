from pydantic import BaseModel
from typing import List


class AnioCausaItem(BaseModel):
    """Item individual de año con cantidad de causas"""
    anio: int
    cantidad_causas_abiertas: int
    cantidad_causas_terminadas: int
    cantidad_causas: int


class DatosGraficoCausasPorAno(BaseModel):
    """Schema con datos listos para graficar causas iniciadas por año"""
    labels: List[int]  # [2010, 2011, 2012, ...] - años
    causas_abiertas: List[int]  # Cantidad de causas abiertas por año
    causas_terminadas: List[int]  # Cantidad de causas terminadas por año
    data: List[int]  # Cantidad total de causas por año (para compatibilidad)
    anos: List[AnioCausaItem]  # Datos completos de cada año
    total_causas_abiertas: int  # Total de causas abiertas en todos los años
    total_causas_terminadas: int  # Total de causas terminadas en todos los años
    total_causas: int  # Total de causas en todos los años


class CausasIniciadasPorAnoResponse(BaseModel):
    """Schema de respuesta para causas iniciadas por año - formato listo para gráficos"""
    datos_grafico: DatosGraficoCausasPorAno
    
    class Config:
        from_attributes = True

