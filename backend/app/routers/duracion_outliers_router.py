from fastapi import APIRouter, Depends
from app.services.duracion_outliers_service import DuracionOutliersService
from app.repositories.expediente_repository import (
    ExpedienteRepository,
    get_expediente_repository
)
from app.schemas.duracion_outliers_schema import DuracionOutliersResponse

router = APIRouter(prefix="/analytics", tags=["analytics"])


@router.get(
    "/duracion-outliers",
    response_model=DuracionOutliersResponse,
    summary="Obtener outliers de duración de instrucción",
    description="Endpoint que devuelve los top 5 causas con mayor y menor duración de instrucción. "
                "Útil para identificar casos atípicos (outliers) que tardan mucho o poco tiempo. "
                "La duración se calcula como la diferencia entre fecha_ultimo_movimiento y fecha_inicio. "
                "No requiere procesamiento adicional en el frontend."
)
def get_duracion_outliers(
    limit: int = 5,
    expediente_repo: ExpedienteRepository = Depends(get_expediente_repository)
):
    """
    Obtiene los outliers de duración de instrucción (top más largos y top más cortos).
    
    - **limit**: Número máximo de causas a retornar en cada categoría (default: 5)
    
    Retorna:
    - **causas_mas_largas**: Lista de top causas con mayor duración (ordenadas DESC)
    - **causas_mas_cortas**: Lista de top causas con menor duración (ordenadas ASC)
    
    Cada causa incluye:
    - numero_expediente
    - caratula
    - tribunal
    - estado_procesal
    - fecha_inicio
    - fecha_ultimo_movimiento
    - duracion_dias
    
    Los datos están listos para usar directamente en tablas o visualizaciones.
    Ideal para análisis de casos atípicos y benchmarking.
    """
    # Crear el service con el repository inyectado
    service = DuracionOutliersService(expediente_repo)
    
    return service.get_datos_outliers(limit=limit)

