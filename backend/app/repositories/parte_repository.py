from typing import List, Generator, Dict, Any
from sqlalchemy.orm import Session
from sqlalchemy import text

from app.core.database import SessionLocal


class ParteRepository:
    """
    Repository para consultas de solo lectura relacionadas con Parte.
    Solo proporciona métodos para obtener datos, no para modificar.
    """
    
    def __init__(self, db: Session):
        """
        Inicializa el repository con una sesión de base de datos.
        
        Args:
            db: Sesión de SQLAlchemy
        """
        self.db = db
    
    def get_personas_mas_denunciadas(self, limit: int = 20) -> List[Dict[str, Any]]:
        """
        Obtiene las personas más denunciadas (con rol 'denunciado').
        
        Args:
            limit: Número máximo de resultados a retornar (default: 20)
            
        Returns:
            Lista de diccionarios con:
            - persona: Nombre o razón social de la persona
            - cantidad_causas: Cantidad de causas donde aparece como denunciado
        """
        query = text("""
            SELECT 
                p.nombre_razon_social AS persona,
                COUNT(p.parte_id) AS cantidad_causas
            FROM parte p
            JOIN rol_parte rp ON rp.parte_id = p.parte_id
            WHERE LOWER(rp.nombre) = 'denunciado'
              AND p.nombre_razon_social IS NOT NULL
              AND p.nombre_razon_social != ''
              AND UPPER(TRIM(p.nombre_razon_social)) != 'NAN'
            GROUP BY p.nombre_razon_social
            ORDER BY cantidad_causas DESC
            LIMIT :limit
        """)
        
        result = self.db.execute(query, {"limit": limit})
        
        # Convertir resultados a lista de diccionarios
        personas = []
        for row in result:
            personas.append({
                "persona": row.persona,
                "cantidad_causas": int(row.cantidad_causas)
            })
        
        return personas
    
    def get_personas_que_mas_denunciaron(self, limit: int = 20) -> List[Dict[str, Any]]:
        """
        Obtiene las personas que más denunciaron (con rol 'denunciante' o 'querellante').
        
        Args:
            limit: Número máximo de resultados a retornar (default: 20)
            
        Returns:
            Lista de diccionarios con:
            - persona: Nombre o razón social de la persona
            - cantidad_denuncias: Cantidad de denuncias realizadas (como denunciante o querellante)
        """
        query = text("""
            SELECT 
                p.nombre_razon_social AS persona,
                COUNT(*) AS cantidad_denuncias
            FROM parte p
            JOIN rol_parte rp ON rp.parte_id = p.parte_id
            WHERE LOWER(rp.nombre) IN ('denunciante', 'querellante')
              AND p.nombre_razon_social IS NOT NULL
              AND p.nombre_razon_social != ''
              AND UPPER(TRIM(p.nombre_razon_social)) != 'NAN'
            GROUP BY p.nombre_razon_social
            ORDER BY cantidad_denuncias DESC
            LIMIT :limit
        """)
        
        result = self.db.execute(query, {"limit": limit})
        
        # Convertir resultados a lista de diccionarios
        personas = []
        for row in result:
            personas.append({
                "persona": row.persona,
                "cantidad_denuncias": int(row.cantidad_denuncias)
            })
        
        return personas


def get_parte_repository() -> Generator[ParteRepository, None, None]:
    """
    Dependency de FastAPI para obtener una instancia del repository.
    Crea una nueva sesión de base de datos y la cierra automáticamente.
    
    Yields:
        Instancia de ParteRepository
        
    Usage en FastAPI:
        @app.get("/personas")
        def get_personas(repo: ParteRepository = Depends(get_parte_repository)):
            return repo.get_personas_mas_denunciadas()
    """
    db = SessionLocal()
    try:
        yield ParteRepository(db)
    finally:
        db.close()

