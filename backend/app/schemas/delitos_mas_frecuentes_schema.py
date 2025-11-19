from pydantic import BaseModel
from typing import List


class DelitoItem(BaseModel):
    """Item individual de delito con cantidad de causas"""
    delito: str
    cantidad_causas: int


class DatosGraficoDelitosMasFrecuentes(BaseModel):
    """Schema con datos listos para graficar delitos más frecuentes"""
    labels: List[str]  # ['Delito 1', 'Delito 2', ...] - nombres de delitos
    data: List[int]  # [150, 120, ...] - cantidad de causas por delito
    delitos: List[DelitoItem]  # Datos completos de cada delito
    total_causas: int  # Total de causas en todos los delitos


class DelitosMasFrecuentesResponse(BaseModel):
    """Schema de respuesta para delitos más frecuentes - formato listo para gráficos"""
    datos_grafico: DatosGraficoDelitosMasFrecuentes
    
    class Config:
        from_attributes = True

