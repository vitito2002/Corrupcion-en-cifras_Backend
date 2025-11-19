from pydantic import BaseModel
from typing import List


class PersonaDenuncianteItem(BaseModel):
    """Schema para un item individual de persona que denunció"""
    persona: str
    cantidad_denuncias: int

    class Config:
        from_attributes = True


class DatosGraficoPersonasQueMasDenunciaron(BaseModel):
    """Schema con datos listos para graficar personas que más denunciaron"""
    labels: List[str]  # Nombres de las personas
    data: List[int]  # Cantidad de denuncias por persona
    personas: List[PersonaDenuncianteItem]  # Lista de objetos con persona y cantidad
    total_denuncias: int  # Total general de denuncias


class PersonasQueMasDenunciaronResponse(BaseModel):
    """Schema de respuesta para personas que más denunciaron - formato listo para gráficos"""
    datos_grafico: DatosGraficoPersonasQueMasDenunciaron

    class Config:
        from_attributes = True

