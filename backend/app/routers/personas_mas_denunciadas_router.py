from fastapi import APIRouter, Depends
from app.services.personas_mas_denunciadas_service import PersonasMasDenunciadasService
from app.repositories.parte_repository import (
    ParteRepository,
    get_parte_repository
)
from app.schemas.personas_mas_denunciadas_schema import PersonasMasDenunciadasResponse

router = APIRouter(prefix="/analytics", tags=["analytics"])


@router.get(
    "/personas-mas-denunciadas",
    response_model=PersonasMasDenunciadasResponse,
    summary="Obtener personas más denunciadas",
    description="Endpoint que devuelve datos agregados listos para graficar. "
                "Muestra las personas que aparecen más veces como denunciadas en causas. "
                "Incluye labels (nombres de personas), datos (cantidades) y total. "
                "No requiere procesamiento adicional en el frontend."
)
def get_personas_mas_denunciadas(
    limit: int = 20,
    parte_repo: ParteRepository = Depends(get_parte_repository)
):
    """
    Obtiene datos procesados de personas más denunciadas listos para graficar.
    
    - **limit**: Número máximo de personas a retornar (default: 20)
    
    Retorna:
    - **labels**: Lista de nombres de personas
    - **data**: Lista de cantidad de causas por persona
    - **personas**: Lista completa con todos los datos de cada persona
    - **total_causas**: Total general de causas
    
    Los datos están listos para usar directamente en librerías como Chart.js, D3, etc.
    Ideal para gráficos de barras horizontales o verticales.
    """
    # Crear el service con el repository inyectado
    service = PersonasMasDenunciadasService(parte_repo)
    
    return service.get_datos_grafico(limit=limit)

