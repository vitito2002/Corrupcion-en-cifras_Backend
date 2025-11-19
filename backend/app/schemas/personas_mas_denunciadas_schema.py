from pydantic import BaseModel
from typing import List


class PersonaDenunciadaItem(BaseModel):
    """Schema para un item individual de persona denunciada"""
    persona: str
    cantidad_causas: int

    class Config:
        from_attributes = True


class DatosGraficoPersonasMasDenunciadas(BaseModel):
    """Schema con datos listos para graficar personas más denunciadas"""
    labels: List[str]  # Nombres de las personas
    data: List[int]  # Cantidad de causas por persona
    personas: List[PersonaDenunciadaItem]  # Lista de objetos con persona y cantidad
    total_causas: int  # Total general de causas


class PersonasMasDenunciadasResponse(BaseModel):
    """Schema de respuesta para personas más denunciadas - formato listo para gráficos"""
    datos_grafico: DatosGraficoPersonasMasDenunciadas

    class Config:
        from_attributes = True

