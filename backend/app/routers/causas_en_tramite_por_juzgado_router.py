from fastapi import APIRouter, Depends
from app.services.causas_en_tramite_por_juzgado_service import CausasEnTramitePorJuzgadoService
from app.repositories.expediente_repository import (
    ExpedienteRepository,
    get_expediente_repository
)
from app.schemas.causas_en_tramite_por_juzgado_schema import CausasEnTramitePorJuzgadoResponse

router = APIRouter(prefix="/analytics", tags=["analytics"])


@router.get(
    "/causas-en-tramite-por-juzgado",
    response_model=CausasEnTramitePorJuzgadoResponse,
    summary="Obtener cantidad de causas en trámite por juzgado",
    description="Endpoint que devuelve datos agregados listos para graficar. "
                "Muestra la cantidad de causas en trámite agrupadas por juzgado/tribunal. "
                "Incluye labels (nombres de juzgados), datos (cantidades) y total. "
                "No requiere procesamiento adicional en el frontend."
)
def get_causas_en_tramite_por_juzgado(
    limit: int = 20,
    expediente_repo: ExpedienteRepository = Depends(get_expediente_repository)
):
    """
    Obtiene datos procesados de causas en trámite por juzgado listos para graficar.
    
    - **limit**: Número máximo de juzgados a retornar (default: 20)
    
    Retorna:
    - **labels**: Lista de nombres de juzgados/tribunales
    - **data**: Lista de cantidad de causas en trámite por juzgado
    - **juzgados**: Lista completa con todos los datos de cada juzgado
    - **total_causas_en_tramite**: Total general de causas en trámite
    
    Los datos están listos para usar directamente en librerías como Chart.js, D3, etc.
    Ideal para gráficos de barras horizontales o verticales.
    """
    # Crear el service con el repository inyectado
    service = CausasEnTramitePorJuzgadoService(expediente_repo)
    
    return service.get_datos_grafico(limit=limit)

