from fastapi import APIRouter, Depends
from app.services.causas_por_fiscalia_service import CausasPorFiscaliaService
from app.repositories.expediente_repository import (
    ExpedienteRepository,
    get_expediente_repository
)
from app.schemas.causas_por_fiscalia_schema import CausasPorFiscaliaResponse

router = APIRouter(prefix="/analytics", tags=["analytics"])


@router.get(
    "/causas-por-fiscal",
    response_model=CausasPorFiscaliaResponse,
    summary="Obtener cantidad de causas por fiscalía clasificadas por abiertas y terminadas",
    description="Endpoint que devuelve datos agregados listos para graficar. "
                "Muestra la cantidad de causas agrupadas por fiscalía, clasificadas según su estado procesal "
                "(abiertas: 'En trámite', terminadas: 'Terminada'). "
                "Incluye labels (nombres de fiscalías), datos separados por estado y totales. "
                "No requiere procesamiento adicional en el frontend."
)
def get_causas_por_fiscal(
    limit: int = 20,
    expediente_repo: ExpedienteRepository = Depends(get_expediente_repository)
):
    """
    Obtiene datos procesados de causas por fiscalía listos para graficar.
    
    - **limit**: Número máximo de fiscalías a retornar (default: 20)
    
    Retorna:
    - **labels**: Lista de nombres de fiscalías
    - **causas_abiertas**: Lista de cantidad de causas abiertas (En trámite) por fiscalía
    - **causas_terminadas**: Lista de cantidad de causas terminadas por fiscalía
    - **fiscalias**: Lista completa con todos los datos de cada fiscalía
    - **total_causas_abiertas**: Total general de causas abiertas
    - **total_causas_terminadas**: Total general de causas terminadas
    - **total_causas**: Total general de causas
    
    Los datos están listos para usar directamente en librerías como Chart.js, D3, etc.
    Ideal para gráficos de barras agrupadas o apiladas.
    """
    # Crear el service con el repository inyectado
    service = CausasPorFiscaliaService(expediente_repo)
    
    return service.get_datos_grafico(limit=limit)





