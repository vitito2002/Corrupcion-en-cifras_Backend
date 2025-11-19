from fastapi import APIRouter, Depends
from app.services.delitos_mas_frecuentes_service import DelitosMasFrecuentesService
from app.repositories.expediente_repository import (
    ExpedienteRepository,
    get_expediente_repository
)
from app.schemas.delitos_mas_frecuentes_schema import DelitosMasFrecuentesResponse

router = APIRouter(prefix="/analytics", tags=["analytics"])


@router.get(
    "/delitos-mas-frecuentes",
    response_model=DelitosMasFrecuentesResponse,
    summary="Obtener datos para gráfico de delitos más frecuentes",
    description="Endpoint que devuelve datos agregados listos para graficar. "
                "Muestra los delitos más frecuentes ordenados por cantidad de causas. "
                "Incluye labels, datos y total. "
                "No requiere procesamiento adicional en el frontend."
)
def get_delitos_mas_frecuentes(
    limit: int = 10,
    expediente_repo: ExpedienteRepository = Depends(get_expediente_repository)
):
    """
    Obtiene datos procesados de delitos más frecuentes listos para graficar.
    
    - **limit**: Número máximo de delitos a retornar (default: 10)
    
    Retorna:
    - **labels**: Lista de nombres de delitos ['Delito 1', 'Delito 2', ...]
    - **data**: Lista de cantidad de causas por delito [150, 120, ...]
    - **delitos**: Lista completa con todos los datos de cada delito
    - **total_causas**: Total de causas en todos los delitos
    
    Los datos están listos para usar directamente en librerías como Chart.js, D3, etc.
    Ideal para gráficos de barras horizontales o pie chart.
    """
    # Crear el service con el repository inyectado
    service = DelitosMasFrecuentesService(expediente_repo)
    
    return service.get_datos_grafico(limit=limit)

