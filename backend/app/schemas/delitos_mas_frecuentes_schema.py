from pydantic import BaseModel
from typing import List


class DelitoItem(BaseModel):
    """Item individual de delito con cantidad de causas"""
    delito: str
    cantidad_causas_abiertas: int
    cantidad_causas_terminadas: int
    cantidad_causas: int


class DatosGraficoDelitosMasFrecuentes(BaseModel):
    """Schema con datos listos para graficar delitos más frecuentes"""
    labels: List[str]  # ['Delito 1', 'Delito 2', ...] - nombres de delitos
    causas_abiertas: List[int]  # Cantidad de causas abiertas por delito
    causas_terminadas: List[int]  # Cantidad de causas terminadas por delito
    data: List[int]  # Cantidad total de causas por delito (para compatibilidad)
    delitos: List[DelitoItem]  # Datos completos de cada delito
    total_causas_abiertas: int  # Total de causas abiertas en todos los delitos
    total_causas_terminadas: int  # Total de causas terminadas en todos los delitos
    total_causas: int  # Total de causas en todos los delitos


class DelitosMasFrecuentesResponse(BaseModel):
    """Schema de respuesta para delitos más frecuentes - formato listo para gráficos"""
    datos_grafico: DatosGraficoDelitosMasFrecuentes
    
    class Config:
        from_attributes = True

