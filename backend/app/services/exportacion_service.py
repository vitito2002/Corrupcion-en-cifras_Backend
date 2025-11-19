import csv
import io
import zipfile
from typing import Generator
from sqlalchemy.orm import Session
from sqlalchemy import text

from app.core.database import SessionLocal


class ExportacionService:
    """
    Service para exportar la base de datos completa a un archivo ZIP.
    Todas las operaciones se realizan en memoria.
    """
    
    # Lista de tablas a exportar
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
        # Ejecutar query para obtener todos los datos
        query = text(f"SELECT * FROM {nombre_tabla}")
        result = self.db.execute(query)
        
        # Obtener nombres de columnas
        columns = result.keys()
        
        # Crear CSV en memoria
        output = io.StringIO()
        writer = csv.writer(output)
        
        # Escribir encabezados
        writer.writerow(columns)
        
        # Escribir filas
        for row in result:
            writer.writerow(row)
        
        return output.getvalue()
    
    def generar_zip_completo(self) -> io.BytesIO:
        """
        Genera un archivo ZIP con todas las tablas exportadas como CSV.
        Todo se realiza en memoria.
        
        Returns:
            BytesIO con el contenido del archivo ZIP
        """
        # Crear ZIP en memoria
        zip_buffer = io.BytesIO()
        
        with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
            # Exportar cada tabla
            for tabla in self.TABLAS:
                try:
                    # Convertir tabla a CSV
                    csv_content = self._tabla_a_csv(tabla)
                    
                    # Agregar CSV al ZIP
                    zip_file.writestr(f"{tabla}.csv", csv_content)
                except Exception as e:
                    # Si hay un error con una tabla, continuar con las demás
                    print(f"Error exportando tabla {tabla}: {e}")
                    # Agregar un archivo de error al ZIP
                    error_content = f"Error al exportar esta tabla: {str(e)}"
                    zip_file.writestr(f"{tabla}_ERROR.txt", error_content)
        
        # Resetear el buffer al inicio para que pueda ser leído
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

