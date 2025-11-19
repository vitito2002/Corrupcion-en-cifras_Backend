from fastapi import APIRouter, Depends
from app.services.duracion_instruccion_service import DuracionInstruccionService
from app.repositories.expediente_repository import (
    ExpedienteRepository,
    get_expediente_repository
)
from app.schemas.duracion_instruccion_schema import DuracionInstruccionResponse

router = APIRouter(prefix="/analytics", tags=["analytics"])


@router.get(
    "/duracion-instruccion",
    response_model=DuracionInstruccionResponse,
    summary="Obtener duración de instrucción de causas",
    description="Endpoint que devuelve datos agregados listos para graficar. "
                "Muestra las causas ordenadas por duración de instrucción (de más larga a más corta). "
                "La duración se calcula como la diferencia entre fecha_ultimo_movimiento y fecha_inicio. "
                "Incluye labels, datos y estadísticas (promedio, máximo, mínimo). "
                "No requiere procesamiento adicional en el frontend."
)
def get_duracion_instruccion(
    limit: int = 50,
    expediente_repo: ExpedienteRepository = Depends(get_expediente_repository)
):
    """
    Obtiene datos procesados de duración de instrucción listos para graficar.
    
    - **limit**: Número máximo de causas a retornar (default: 50)
    
    Retorna:
    - **labels**: Lista de carátulas o números de expediente (truncadas si son muy largas)
    - **data**: Lista de duración en días
    - **causas**: Lista completa con todos los datos de cada causa
    - **duracion_promedio_dias**: Duración promedio en días
    - **duracion_maxima_dias**: Duración máxima en días
    - **duracion_minima_dias**: Duración mínima en días
    - **total_causas**: Total de causas analizadas
    
    Los datos están listos para usar directamente en librerías como Chart.js, D3, etc.
    Ideal para gráficos de barras horizontales o verticales ordenadas por duración.
    """
    # Crear el service con el repository inyectado
    service = DuracionInstruccionService(expediente_repo)
    
    return service.get_datos_grafico(limit=limit)

