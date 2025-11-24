from fastapi import APIRouter, Depends
from datetime import datetime
from zoneinfo import ZoneInfo
from app.repositories.metadata_repository import (
    MetadataRepository,
    get_metadata_repository
)
from app.schemas.metadata_schema import UltimaActualizacionResponse

# Zona horaria de Argentina
TZ_ARGENTINA = ZoneInfo("America/Argentina/Buenos_Aires")

router = APIRouter(prefix="/analytics", tags=["analytics"])


@router.get(
    "/ultima-actualizacion",
    response_model=UltimaActualizacionResponse,
    summary="Obtener fecha de última actualización de los datos",
    description="Endpoint que devuelve la fecha y hora de la última actualización de los datos en el sistema."
)
def get_ultima_actualizacion(
    metadata_repo: MetadataRepository = Depends(get_metadata_repository)
):
    """
    Obtiene la fecha de última actualización de los datos.
    
    Retorna:
    - **ultima_actualizacion**: Fecha y hora de última actualización (datetime)
    - **formato_fecha**: Fecha formateada en español para mostrar (ej: "15 de enero de 2024, 14:30")
    """
    ultima_actualizacion = metadata_repo.get_ultima_actualizacion()
    
    # Formatear fecha en español
    formato_fecha = "No disponible"
    if ultima_actualizacion:
        # Convertir a zona horaria de Argentina
        # Si la fecha viene sin timezone, asumimos que está en UTC
        if ultima_actualizacion.tzinfo is None:
            # Si no tiene timezone, asumimos UTC y convertimos a Argentina
            fecha_arg = ultima_actualizacion.replace(tzinfo=ZoneInfo("UTC")).astimezone(TZ_ARGENTINA)
        else:
            # Si ya tiene timezone, convertir a Argentina
            fecha_arg = ultima_actualizacion.astimezone(TZ_ARGENTINA)
        
        meses = [
            "enero", "febrero", "marzo", "abril", "mayo", "junio",
            "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"
        ]
        dia = fecha_arg.day
        mes = meses[fecha_arg.month - 1]
        año = fecha_arg.year
        hora = fecha_arg.strftime("%H:%M")
        formato_fecha = f"{dia} de {mes} de {año}, {hora}"
    
    return UltimaActualizacionResponse(
        ultima_actualizacion=ultima_actualizacion,
        formato_fecha=formato_fecha
    )

