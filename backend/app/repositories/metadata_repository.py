from typing import Optional, Generator
from datetime import datetime
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.core.database import SessionLocal
from app.models.metadata import Metadata


class MetadataRepository:
    """
    Repository para consultas relacionadas con metadatos del sistema.
    """
    
    def __init__(self, db: Session):
        """
        Inicializa el repository con una sesión de base de datos.
        
        Args:
            db: Sesión de SQLAlchemy
        """
        self.db = db
    
    def get_ultima_actualizacion(self) -> Optional[datetime]:
        """
        Obtiene la fecha de última actualización de los datos.
        
        Returns:
            Fecha de última actualización o None si no existe
        """
        # Intentar obtener de la tabla metadata
        metadata = self.db.query(Metadata).filter(
            Metadata.clave == 'ultima_actualizacion'
        ).first()
        
        if metadata:
            return metadata.valor
        
        # Si no existe en metadata, usar la fecha más reciente de fecha_ultimo_movimiento
        # como fallback
        query = text("""
            SELECT MAX(fecha_ultimo_movimiento) AS ultima_fecha
            FROM expediente
            WHERE fecha_ultimo_movimiento IS NOT NULL
        """)
        
        result = self.db.execute(query).first()
        if result and result.ultima_fecha:
            return result.ultima_fecha
        
        return None
    
    def actualizar_fecha_actualizacion(self, fecha: Optional[datetime] = None) -> None:
        """
        Actualiza la fecha de última actualización.
        Si no se proporciona fecha, usa la fecha actual.
        
        Args:
            fecha: Fecha a guardar (opcional, por defecto usa la fecha actual)
        """
        if fecha is None:
            fecha = datetime.now()
        
        metadata = self.db.query(Metadata).filter(
            Metadata.clave == 'ultima_actualizacion'
        ).first()
        
        if metadata:
            metadata.valor = fecha
        else:
            metadata = Metadata(clave='ultima_actualizacion', valor=fecha)
            self.db.add(metadata)
        
        self.db.commit()


def get_metadata_repository() -> Generator[MetadataRepository, None, None]:
    """
    Dependency de FastAPI para obtener una instancia del MetadataRepository.
    Crea una nueva sesión de base de datos y la cierra automáticamente.
    
    Returns:
        Instancia de MetadataRepository
    """
    db = SessionLocal()
    try:
        yield MetadataRepository(db)
    finally:
        db.close()

