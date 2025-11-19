from fastapi import APIRouter, Depends
from app.services.causas_por_fiscal_service import CausasPorFiscalService
from app.repositories.expediente_repository import (
    ExpedienteRepository,
    get_expediente_repository
)
from app.schemas.causas_por_fiscal_schema import CausasPorFiscalResponse

router = APIRouter(prefix="/analytics", tags=["analytics"])


@router.get(
    "/causas-por-fiscal",
    response_model=CausasPorFiscalResponse,
    summary="Obtener cantidad de causas por fiscal clasificadas por abiertas y terminadas",
    description="Endpoint que devuelve datos agregados listos para graficar. "
                "Muestra la cantidad de causas agrupadas por fiscal, clasificadas según su estado procesal "
                "(abiertas: 'En trámite', terminadas: 'Terminada'). "
                "Incluye labels (nombres de fiscales), datos separados por estado y totales. "
                "No requiere procesamiento adicional en el frontend."
)
def get_causas_por_fiscal(
    limit: int = 20,
    expediente_repo: ExpedienteRepository = Depends(get_expediente_repository)
):
    """
    Obtiene datos procesados de causas por fiscal listos para graficar.
    
    - **limit**: Número máximo de fiscales a retornar (default: 20)
    
    Retorna:
    - **labels**: Lista de nombres de fiscales
    - **causas_abiertas**: Lista de cantidad de causas abiertas (En trámite) por fiscal
    - **causas_terminadas**: Lista de cantidad de causas terminadas por fiscal
    - **fiscales**: Lista completa con todos los datos de cada fiscal
    - **total_causas_abiertas**: Total general de causas abiertas
    - **total_causas_terminadas**: Total general de causas terminadas
    - **total_causas**: Total general de causas
    
    Los datos están listos para usar directamente en librerías como Chart.js, D3, etc.
    Ideal para gráficos de barras agrupadas o apiladas.
    """
    # Crear el service con el repository inyectado
    service = CausasPorFiscalService(expediente_repo)
    
    return service.get_datos_grafico(limit=limit)

