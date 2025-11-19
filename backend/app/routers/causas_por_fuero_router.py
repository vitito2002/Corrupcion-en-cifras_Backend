from fastapi import APIRouter, Depends
from app.services.causas_por_fuero_service import CausasPorFueroService
from app.repositories.expediente_repository import (
    ExpedienteRepository,
    get_expediente_repository
)
from app.schemas.causas_por_fuero_schema import CausasPorFueroResponse

router = APIRouter(prefix="/analytics", tags=["analytics"])


@router.get(
    "/causas-por-fuero",
    response_model=CausasPorFueroResponse,
    summary="Obtener distribución de causas por fuero judicial",
    description="Endpoint que devuelve datos agregados listos para graficar. "
                "Muestra la distribución de causas según el fuero judicial correspondiente. "
                "Incluye labels (nombres de fueros), datos (cantidades) y total. "
                "No requiere procesamiento adicional en el frontend."
)
def get_causas_por_fuero(
    expediente_repo: ExpedienteRepository = Depends(get_expediente_repository)
):
    """
    Obtiene datos procesados de causas por fuero listos para graficar.
    
    Retorna:
    - **labels**: Lista de nombres de fueros judiciales
    - **data**: Lista de cantidad de causas por fuero
    - **fueros**: Lista completa con todos los datos de cada fuero
    - **total_causas**: Total general de causas
    
    Los datos están listos para usar directamente en librerías como Chart.js, D3, etc.
    Ideal para gráficos de barras o pie chart.
    """
    # Crear el service con el repository inyectado
    service = CausasPorFueroService(expediente_repo)
    
    return service.get_datos_grafico()

