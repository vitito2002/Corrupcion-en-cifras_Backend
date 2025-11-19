from pydantic import BaseModel
from typing import List


class FueroCausaItem(BaseModel):
    """Schema para un item individual de fuero con cantidad de causas"""
    fuero: str
    cantidad_causas_abiertas: int
    cantidad_causas_terminadas: int
    cantidad_causas: int

    class Config:
        from_attributes = True


class DatosGraficoCausasPorFuero(BaseModel):
    """Schema con datos listos para graficar causas por fuero"""
    labels: List[str]  # Nombres de los fueros
    causas_abiertas: List[int]  # Cantidad de causas abiertas por fuero
    causas_terminadas: List[int]  # Cantidad de causas terminadas por fuero
    data: List[int]  # Cantidad total de causas por fuero (para compatibilidad)
    fueros: List[FueroCausaItem]  # Lista de objetos con fuero y cantidades
    total_causas_abiertas: int  # Total general de causas abiertas
    total_causas_terminadas: int  # Total general de causas terminadas
    total_causas: int  # Total general de causas


class CausasPorFueroResponse(BaseModel):
    """Schema de respuesta para causas por fuero - formato listo para gráficos"""
    datos_grafico: DatosGraficoCausasPorFuero

    class Config:
        from_attributes = True

