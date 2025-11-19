from fastapi import APIRouter, Depends
from app.services.jueces_mayor_demora_service import JuecesMayorDemoraService
from app.repositories.juez_repository import (
    JuezRepository,
    get_juez_repository
)
from app.schemas.jueces_mayor_demora_schema import JuecesMayorDemoraResponse

router = APIRouter(prefix="/analytics", tags=["analytics"])


@router.get(
    "/jueces-mayor-demora",
    response_model=JuecesMayorDemoraResponse,
    summary="Obtener datos para gráfico de jueces con mayor demora",
    description="Endpoint que devuelve datos agregados listos para graficar. "
                "Incluye labels, demoras promedio y cantidad de expedientes. "
                "No requiere procesamiento adicional en el frontend."
)
def get_jueces_mayor_demora(
    limit: int = 10,
    juez_repo: JuezRepository = Depends(get_juez_repository)
):
    """
    Obtiene datos procesados de jueces con mayor demora promedio listos para graficar.
    
    - **limit**: Número máximo de jueces a retornar (default: 10)
    
    Retorna:
    - **labels**: Lista de labels ['Juez 1 - Tribunal 1', 'Juez 2 - Tribunal 2', ...]
    - **data**: Lista de demoras promedio en días [1234.56, 987.32, ...]
    - **cantidad_expedientes**: Lista de cantidad de expedientes [42, 35, ...]
    - **jueces**: Lista completa con todos los datos de cada juez
    
    Los datos están listos para usar directamente en librerías como Chart.js, D3, etc.
    """
    # Crear el service con el repository inyectado
    service = JuecesMayorDemoraService(juez_repo)
    
    return service.get_datos_grafico(limit=limit)

