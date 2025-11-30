import csv
import io
import zipfile
from typing import Generator
from sqlalchemy.orm import Session
from sqlalchemy import text

from app.core.database import SessionLocal


class ExportacionService:
    """Service para exportar la base de datos completa a un archivo ZIP."""
    
    TABLAS = [
        "fuero",
        "jurisdiccion",
        "tribunal",
        "secretaria",
        "expediente",
        "radicacion",
        "resolucion",
        "parte",
        "rol_parte",
        "letrado",
        "representacion",
        "expediente_delito",
        "tipo_delito",
        "plazo",
        "juez",
        "tribunal_juez"
    ]
    
    def __init__(self, db: Session):
        """
        Inicializa el service con una sesión de base de datos.
        
        Args:
            db: Sesión de SQLAlchemy
        """
        self.db = db
    
    def _tabla_a_csv(self, nombre_tabla: str) -> str:
        """
        Convierte una tabla de la base de datos a CSV en memoria.
        
        Args:
            nombre_tabla: Nombre de la tabla a exportar
            
        Returns:
            String con el contenido CSV de la tabla
        """
        query = text(f"SELECT * FROM {nombre_tabla}")
        result = self.db.execute(query)
        columns = result.keys()
        
        output = io.StringIO()
        writer = csv.writer(output)
        writer.writerow(columns)
        
        for row in result:
            writer.writerow(row)
        
        return output.getvalue()
    
    def generar_zip_completo(self) -> io.BytesIO:
        """
        Genera un archivo ZIP con todas las tablas exportadas como CSV.
        
        Returns:
            BytesIO con el contenido del archivo ZIP
        """
        zip_buffer = io.BytesIO()
        
        with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
            for tabla in self.TABLAS:
                try:
                    csv_content = self._tabla_a_csv(tabla)
                    zip_file.writestr(f"{tabla}.csv", csv_content)
                except Exception as e:
                    print(f"Error exportando tabla {tabla}: {e}")
                    error_content = f"Error al exportar esta tabla: {str(e)}"
                    zip_file.writestr(f"{tabla}_ERROR.txt", error_content)
        
        zip_buffer.seek(0)
        
        return zip_buffer


def get_exportacion_service() -> Generator[ExportacionService, None, None]:
    """
    Dependency de FastAPI para obtener una instancia del ExportacionService.
    Crea una nueva sesión de base de datos y la cierra automáticamente.
    
    Yields:
        Instancia de ExportacionService
        
    Usage en FastAPI:
        @app.get("/exportar")
        def exportar(service: ExportacionService = Depends(get_exportacion_service)):
            return service.generar_zip_completo()
    """
    db = SessionLocal()
    try:
        yield ExportacionService(db)
    finally:
        db.close()

