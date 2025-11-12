from typing import List, Optional, Generator
from sqlalchemy.orm import Session
from sqlalchemy import and_, or_, desc, asc
from datetime import date, datetime

from app.core.database import SessionLocal
from app.models.expediente import Expediente


class ExpedienteRepository:
    """
    Repository para consultas de solo lectura de Expediente.
    Solo proporciona métodos para obtener datos, no para modificar.
    """
    
    def __init__(self, db: Session):
        """
        Inicializa el repository con una sesión de base de datos.
        
        Args:
            db: Sesión de SQLAlchemy
        """
        self.db = db
    
    def get_by_numero(self, numero_expediente: str) -> Optional[Expediente]:
        """
        Obtiene un expediente por su número de expediente.
        
        Args:
            numero_expediente: Número del expediente (PK)
            
        Returns:
            Expediente o None si no existe
        """
        return self.db.query(Expediente).filter(
            Expediente.numero_expediente == numero_expediente
        ).first()
    
    def get_all(self, skip: int = 0, limit: int = 100) -> List[Expediente]:
        """
        Obtiene todos los expedientes con paginación.
        
        Args:
            skip: Número de registros a saltar
            limit: Número máximo de registros a retornar
            
        Returns:
            Lista de expedientes
        """
        return self.db.query(Expediente).offset(skip).limit(limit).all()
    
    def get_by_estado_procesal(
        self, 
        estado_procesal: str, 
        skip: int = 0, 
        limit: int = 100
    ) -> List[Expediente]:
        """
        Obtiene expedientes filtrados por estado procesal.
        
        Args:
            estado_procesal: Estado procesal ('En trámite' o 'Terminada')
            skip: Número de registros a saltar
            limit: Número máximo de registros a retornar
            
        Returns:
            Lista de expedientes con el estado procesal especificado
        """
        return self.db.query(Expediente).filter(
            Expediente.estado_procesal == estado_procesal
        ).offset(skip).limit(limit).all()
    
    def get_by_tribunal(
        self, 
        tribunal_id: int, 
        skip: int = 0, 
        limit: int = 100
    ) -> List[Expediente]:
        """
        Obtiene expedientes filtrados por tribunal.
        
        Args:
            tribunal_id: ID del tribunal
            skip: Número de registros a saltar
            limit: Número máximo de registros a retornar
            
        Returns:
            Lista de expedientes del tribunal
        """
        return self.db.query(Expediente).filter(
            Expediente.id_tribunal == tribunal_id
        ).offset(skip).limit(limit).all()
    
    def get_by_jurisdiccion(
        self, 
        jurisdiccion: str, 
        skip: int = 0, 
        limit: int = 100
    ) -> List[Expediente]:
        """
        Obtiene expedientes filtrados por jurisdicción.
        
        Args:
            jurisdiccion: Nombre de la jurisdicción
            skip: Número de registros a saltar
            limit: Número máximo de registros a retornar
            
        Returns:
            Lista de expedientes de la jurisdicción
        """
        return self.db.query(Expediente).filter(
            Expediente.jurisdiccion.ilike(f"%{jurisdiccion}%")
        ).offset(skip).limit(limit).all()
    
    def search_by_numero(self, numero: str) -> List[Expediente]:
        """
        Busca expedientes por número de expediente (búsqueda parcial).
        
        Args:
            numero: Número o parte del número de expediente
            
        Returns:
            Lista de expedientes que coinciden
        """
        return self.db.query(Expediente).filter(
            Expediente.numero_expediente.ilike(f"%{numero}%")
        ).all()
    
    def search_by_caratula(self, caratula: str, skip: int = 0, limit: int = 100) -> List[Expediente]:
        """
        Busca expedientes por carátula (búsqueda parcial).
        
        Args:
            caratula: Texto a buscar en la carátula
            skip: Número de registros a saltar
            limit: Número máximo de registros a retornar
            
        Returns:
            Lista de expedientes que coinciden
        """
        return self.db.query(Expediente).filter(
            Expediente.caratula.ilike(f"%{caratula}%")
        ).offset(skip).limit(limit).all()
    
    def get_by_fecha_inicio_range(
        self, 
        fecha_inicio: date, 
        fecha_fin: date, 
        skip: int = 0, 
        limit: int = 100
    ) -> List[Expediente]:
        """
        Obtiene expedientes en un rango de fechas de inicio.
        
        Args:
            fecha_inicio: Fecha de inicio
            fecha_fin: Fecha de fin
            skip: Número de registros a saltar
            limit: Número máximo de registros a retornar
            
        Returns:
            Lista de expedientes en el rango de fechas
        """
        return self.db.query(Expediente).filter(
            and_(
                Expediente.fecha_inicio >= fecha_inicio,
                Expediente.fecha_inicio <= fecha_fin
            )
        ).offset(skip).limit(limit).all()
    
    def get_by_ano_inicio(
        self, 
        ano: int, 
        skip: int = 0, 
        limit: int = 100
    ) -> List[Expediente]:
        """
        Obtiene expedientes por año de inicio.
        
        Args:
            ano: Año de inicio
            skip: Número de registros a saltar
            limit: Número máximo de registros a retornar
            
        Returns:
            Lista de expedientes del año especificado
        """
        return self.db.query(Expediente).filter(
            Expediente.ano_inicio == ano
        ).offset(skip).limit(limit).all()
    
    def get_by_fiscal(
        self, 
        fiscal: str, 
        skip: int = 0, 
        limit: int = 100
    ) -> List[Expediente]:
        """
        Obtiene expedientes filtrados por fiscal.
        
        Args:
            fiscal: Nombre del fiscal
            skip: Número de registros a saltar
            limit: Número máximo de registros a retornar
            
        Returns:
            Lista de expedientes del fiscal
        """
        return self.db.query(Expediente).filter(
            Expediente.fiscal.ilike(f"%{fiscal}%")
        ).offset(skip).limit(limit).all()
    
    def get_by_fiscalia(
        self, 
        fiscalia: str, 
        skip: int = 0, 
        limit: int = 100
    ) -> List[Expediente]:
        """
        Obtiene expedientes filtrados por fiscalía.
        
        Args:
            fiscalia: Nombre de la fiscalía
            skip: Número de registros a saltar
            limit: Número máximo de registros a retornar
            
        Returns:
            Lista de expedientes de la fiscalía
        """
        return self.db.query(Expediente).filter(
            Expediente.fiscalia.ilike(f"%{fiscalia}%")
        ).offset(skip).limit(limit).all()
    
    def count(self) -> int:
        """
        Cuenta el total de expedientes.
        
        Returns:
            Número total de expedientes
        """
        return self.db.query(Expediente).count()
    
    def count_by_estado_procesal(self, estado_procesal: str) -> int:
        """
        Cuenta expedientes por estado procesal.
        
        Args:
            estado_procesal: Estado procesal ('En trámite' o 'Terminada')
            
        Returns:
            Número de expedientes con el estado especificado
        """
        return self.db.query(Expediente).filter(
            Expediente.estado_procesal == estado_procesal
        ).count()
    
    def count_by_tribunal(self, tribunal_id: int) -> int:
        """
        Cuenta expedientes por tribunal.
        
        Args:
            tribunal_id: ID del tribunal
            
        Returns:
            Número de expedientes del tribunal
        """
        return self.db.query(Expediente).filter(
            Expediente.id_tribunal == tribunal_id
        ).count()
    
    def count_by_ano_inicio(self, ano: int) -> int:
        """
        Cuenta expedientes por año de inicio.
        
        Args:
            ano: Año de inicio
            
        Returns:
            Número de expedientes del año especificado
        """
        return self.db.query(Expediente).filter(
            Expediente.ano_inicio == ano
        ).count()
    
    def get_estadisticas_estado_procesal(self) -> dict:
        """
        Obtiene estadísticas de expedientes por estado procesal.
        
        Returns:
            Diccionario con conteos por estado procesal
        """
        total = self.count()
        en_tramite = self.count_by_estado_procesal('En trámite')
        terminada = self.count_by_estado_procesal('Terminada')
        
        return {
            'total': total,
            'en_tramite': en_tramite,
            'terminada': terminada,
            'porcentaje_en_tramite': (en_tramite / total * 100) if total > 0 else 0,
            'porcentaje_terminada': (terminada / total * 100) if total > 0 else 0
        }


def get_expediente_repository() -> Generator[ExpedienteRepository, None, None]:
    """
    Dependency de FastAPI para obtener una instancia del repository.
    Crea una nueva sesión de base de datos y la cierra automáticamente.
    
    Yields:
        Instancia de ExpedienteRepository
        
    Usage en FastAPI:
        @app.get("/expedientes")
        def get_expedientes(repo: ExpedienteRepository = Depends(get_expediente_repository)):
            return repo.get_all()
    """
    db = SessionLocal()
    try:
        yield ExpedienteRepository(db)
    finally:
        db.close()
