from fastapi import APIRouter, Depends, HTTPException
from app.services.analytics_service import AnalyticsService
from app.repositories.expediente_repository import (
    ExpedienteRepository,
    get_expediente_repository
)
from app.schemas.analytics_schema import CasosPorEstadoProcesalResponse

router = APIRouter(prefix="/analytics", tags=["analytics"])


@router.get(
    "/casos-por-estado/{estado_procesal}",
    response_model=CasosPorEstadoProcesalResponse,
    summary="Obtener casos por estado procesal",
    description="Endpoint para obtener casos filtrados por estado procesal. "
                "Útil para gráficos que muestran distribución de casos por estado."
)
def get_casos_por_estado_procesal(
    estado_procesal: str,
    skip: int = 0,
    limit: int = 100,
    expediente_repo: ExpedienteRepository = Depends(get_expediente_repository)
):
    """
    Obtiene casos filtrados por estado procesal.
    
    - **estado_procesal**: Estado procesal ('En trámite' o 'Terminada')
    - **skip**: Número de registros a saltar (para paginación)
    - **limit**: Número máximo de registros a retornar
    
    Retorna los casos con el estado especificado y el total de casos con ese estado.
    """
    # Crear el service con el repository inyectado
    service = AnalyticsService(expediente_repo)
    
    try:
        return service.get_casos_por_estado_procesal(
            estado_procesal=estado_procesal,
            skip=skip,
            limit=limit
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
