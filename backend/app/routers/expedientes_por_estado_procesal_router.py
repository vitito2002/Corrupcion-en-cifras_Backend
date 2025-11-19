from fastapi import APIRouter, Depends
from app.services.causas_por_estado_procesal_service import CausasPorEstadoProcesalService
from app.repositories.expediente_repository import (
    ExpedienteRepository,
    get_expediente_repository
)
from app.schemas.expedientes_por_estado_procesal_schema import CasosPorEstadoProcesalResponse

router = APIRouter(prefix="/analytics", tags=["analytics"])


@router.get(
    "/casos-por-estado",
    response_model=CasosPorEstadoProcesalResponse,
    summary="Obtener datos para gráfico de casos por estado procesal",
    description="Endpoint que devuelve datos agregados listos para graficar. "
                "Incluye labels, valores y porcentajes. "
                "No requiere procesamiento adicional en el frontend."
)
def get_casos_por_estado_procesal(
    expediente_repo: ExpedienteRepository = Depends(get_expediente_repository)
):
    """
    Obtiene datos procesados y agregados por estado procesal listos para graficar.
    
    Retorna:
    - **labels**: Lista de estados procesales ['En trámite', 'Terminada']
    - **data**: Lista de conteos [264, 1807]
    - **porcentajes**: Lista de porcentajes [12.7, 87.3]
    - **total**: Total de casos
    
    Los datos están listos para usar directamente en librerías como Chart.js, D3, etc.
    """
    # Crear el service con el repository inyectado
    service = CausasPorEstadoProcesalService(expediente_repo)
    
    return service.get_datos_grafico()

