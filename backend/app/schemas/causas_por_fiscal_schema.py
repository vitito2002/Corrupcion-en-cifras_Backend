from pydantic import BaseModel
from typing import List


class FiscalCausasItem(BaseModel):
    """Schema para un item individual de fiscal con cantidad de causas"""
    fiscal: str
    causas_abiertas: int
    causas_terminadas: int
    total_causas: int

    class Config:
        from_attributes = True


class DatosGraficoCausasPorFiscal(BaseModel):
    """Schema con datos listos para graficar causas por fiscal"""
    labels: List[str]  # Nombres de los fiscales
    causas_abiertas: List[int]  # Cantidad de causas abiertas por fiscal
    causas_terminadas: List[int]  # Cantidad de causas terminadas por fiscal
    fiscales: List[FiscalCausasItem]  # Lista de objetos con fiscal y cantidades
    total_causas_abiertas: int  # Total general de causas abiertas
    total_causas_terminadas: int  # Total general de causas terminadas
    total_causas: int  # Total general de causas


class CausasPorFiscalResponse(BaseModel):
    """Schema de respuesta para causas por fiscal - formato listo para gráficos"""
    datos_grafico: DatosGraficoCausasPorFiscal

    class Config:
        from_attributes = True

