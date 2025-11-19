from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse
from app.services.exportacion_service import (
    ExportacionService,
    get_exportacion_service
)

router = APIRouter(prefix="/exportacion", tags=["exportacion"])


@router.get(
    "/descargar-base-de-datos",
    summary="Descargar base de datos completa en formato ZIP",
    description="Exporta todas las tablas de la base de datos como archivos CSV "
                "y los comprime en un archivo ZIP. Todo el proceso se realiza en memoria. "
                "El archivo incluye las siguientes tablas: fuero, jurisdiccion, tribunal, "
                "secretaria, expediente, radicacion, resolucion, parte, rol_parte, letrado, "
                "representacion, expediente_delito, tipo_delito, plazo, juez, tribunal_juez."
)
def descargar_base_de_datos(
    service: ExportacionService = Depends(get_exportacion_service)
):
    """
    Endpoint para descargar toda la base de datos como un archivo ZIP.
    
    Retorna:
    - Un archivo ZIP que contiene todos los datos de la base de datos
    - Cada tabla se exporta como un archivo CSV individual
    - El nombre del archivo es: base_corrupcion.zip
    
    El proceso se realiza completamente en memoria, sin escribir archivos en disco.
    """
    # Generar el ZIP en memoria
    zip_buffer = service.generar_zip_completo()
    
    # Retornar como StreamingResponse
    return StreamingResponse(
        zip_buffer,
        media_type="application/zip",
        headers={
            "Content-Disposition": "attachment; filename=base_corrupcion.zip"
        }
    )

