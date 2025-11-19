from fastapi import APIRouter, Depends
from app.services.personas_que_mas_denunciaron_service import PersonasQueMasDenunciaronService
from app.repositories.parte_repository import (
    ParteRepository,
    get_parte_repository
)
from app.schemas.personas_que_mas_denunciaron_schema import PersonasQueMasDenunciaronResponse

router = APIRouter(prefix="/analytics", tags=["analytics"])


@router.get(
    "/personas-que-mas-denunciaron",
    response_model=PersonasQueMasDenunciaronResponse,
    summary="Obtener personas que más denunciaron",
    description="Endpoint que devuelve datos agregados listos para graficar. "
                "Muestra las personas que aparecen más veces como denunciantes o querellantes en causas. "
                "Incluye labels (nombres de personas), datos (cantidades) y total. "
                "No requiere procesamiento adicional en el frontend."
)
def get_personas_que_mas_denunciaron(
    limit: int = 20,
    parte_repo: ParteRepository = Depends(get_parte_repository)
):
    """
    Obtiene datos procesados de personas que más denunciaron listos para graficar.
    
    - **limit**: Número máximo de personas a retornar (default: 20)
    
    Retorna:
    - **labels**: Lista de nombres de personas
    - **data**: Lista de cantidad de denuncias por persona
    - **personas**: Lista completa con todos los datos de cada persona
    - **total_denuncias**: Total general de denuncias
    
    Los datos están listos para usar directamente en librerías como Chart.js, D3, etc.
    Ideal para gráficos de barras horizontales o verticales.
    """
    # Crear el service con el repository inyectado
    service = PersonasQueMasDenunciaronService(parte_repo)
    
    return service.get_datos_grafico(limit=limit)

