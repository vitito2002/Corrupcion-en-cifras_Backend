from pydantic import BaseModel
from typing import List


class FueroCausaItem(BaseModel):
    """Schema para un item individual de fuero con cantidad de causas"""
    fuero: str
    cantidad_causas: int

    class Config:
        from_attributes = True


class DatosGraficoCausasPorFuero(BaseModel):
    """Schema con datos listos para graficar causas por fuero"""
    labels: List[str]  # Nombres de los fueros
    data: List[int]  # Cantidad de causas por fuero
    fueros: List[FueroCausaItem]  # Lista de objetos con fuero y cantidad
    total_causas: int  # Total general de causas


class CausasPorFueroResponse(BaseModel):
    """Schema de respuesta para causas por fuero - formato listo para gráficos"""
    datos_grafico: DatosGraficoCausasPorFuero

    class Config:
        from_attributes = True

