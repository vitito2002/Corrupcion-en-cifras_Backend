from fastapi import APIRouter, Depends
from app.services.causas_iniciadas_por_ano_service import CausasIniciadasPorAnoService
from app.repositories.expediente_repository import (
    ExpedienteRepository,
    get_expediente_repository
)
from app.schemas.causas_iniciadas_por_ano_schema import CausasIniciadasPorAnoResponse

router = APIRouter(prefix="/analytics", tags=["analytics"])


@router.get(
    "/causas-iniciadas-por-ano",
    response_model=CausasIniciadasPorAnoResponse,
    summary="Obtener datos para gráfico de causas iniciadas por año",
    description="Endpoint que devuelve datos agregados listos para graficar. "
                "Muestra la evolución temporal de cuántas causas se iniciaron por año. "
                "Incluye labels (años), datos (cantidades) y total. "
                "No requiere procesamiento adicional en el frontend."
)
def get_causas_iniciadas_por_ano(
    expediente_repo: ExpedienteRepository = Depends(get_expediente_repository)
):
    """
    Obtiene datos procesados de causas iniciadas por año listos para graficar.
    
    Retorna:
    - **labels**: Lista de años [2010, 2011, 2012, ...]
    - **data**: Lista de cantidad de causas por año [45, 67, 89, ...]
    - **anos**: Lista completa con todos los datos de cada año
    - **total_causas**: Total de causas en todos los años
    
    Los datos están listos para usar directamente en librerías como Chart.js, D3, etc.
    Ideal para gráficos de línea temporal o barras por año.
    """
    # Crear el service con el repository inyectado
    service = CausasIniciadasPorAnoService(expediente_repo)
    
    return service.get_datos_grafico()

