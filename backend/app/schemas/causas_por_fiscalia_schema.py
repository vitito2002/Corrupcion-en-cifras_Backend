from pydantic import BaseModel
from typing import List


class FiscaliaCausasItem(BaseModel):
    """Schema para un item individual de fiscalía con cantidad de causas"""
    fiscalia: str
    causas_abiertas: int
    causas_terminadas: int
    total_causas: int

    class Config:
        from_attributes = True


class DatosGraficoCausasPorFiscalia(BaseModel):
    """Schema con datos listos para graficar causas por fiscalía"""
    labels: List[str]  # Nombres de las fiscalías
    causas_abiertas: List[int]  # Cantidad de causas abiertas por fiscalía
    causas_terminadas: List[int]  # Cantidad de causas terminadas por fiscalía
    fiscalias: List[FiscaliaCausasItem]  # Lista de objetos con fiscalía y cantidades
    total_causas_abiertas: int  # Total general de causas abiertas
    total_causas_terminadas: int  # Total general de causas terminadas
    total_causas: int  # Total general de causas


class CausasPorFiscaliaResponse(BaseModel):
    """Schema de respuesta para causas por fiscalía - formato listo para gráficos"""
    datos_grafico: DatosGraficoCausasPorFiscalia

    class Config:
        from_attributes = True





