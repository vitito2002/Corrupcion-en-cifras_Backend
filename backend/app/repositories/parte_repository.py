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
        Normaliza los nombres para evitar duplicados (ej: diferentes variantes de CFK, Macri, etc.).
        
        Args:
            limit: Número máximo de resultados a retornar (default: 20)
            
        Returns:
            Lista de diccionarios con:
            - persona: Nombre normalizado de la persona
            - cantidad_causas: Cantidad de causas donde aparece como denunciado (usando COUNT DISTINCT)
        """
        query = text("""
            SELECT 
                REGEXP_REPLACE(
                    REPLACE(
                        REPLACE(
                            CASE 
                                WHEN UPPER(TRIM(p.nombre_razon_social)) IN (
                                    'FERNANDEZ CRISTINA',
                                    'FERNANDEZ CRISTINA ELISABET',
                                    'KIRCHNER CRISTINA ELISABET',
                                    'KIRCHNER CRTISTINA ELISABET',
                                    'FERNANDEZ DE KIRCHNER CRISTINA',
                                    'FERNANDEZ DE KIRCHNER CRISTINA ELISABET',
                                    'CFK',
                                    'CRISTINA FERNANDEZ',
                                    'CRISTINA FERNANDEZ DE KIRCHNER',
                                    'CRISTINA ELISABET FERNANDEZ'
                                ) THEN 'FERNANDEZ DE KIRCHNER CRISTINA ELISABET'
                                
                                -- Mauricio Macri
                                WHEN UPPER(TRIM(p.nombre_razon_social)) IN (
                                    'MACRI MAURICIO',
                                    'MACRI MAURICIO JOSE',
                                    'MACRI M',
                                    'MAURICIO MACRI',
                                    'MACRI'
                                ) THEN 'MACRI MAURICIO'
                                
                                -- Amado Boudou
                                WHEN UPPER(TRIM(p.nombre_razon_social)) IN (
                                    'BOUDOU AMADO',
                                    'BOUDOU AMADO JOSE',
                                    'AMADO BOUDOU'
                                ) THEN 'BOUDOU AMADO'
                                
                                -- Julio De Vido
                                WHEN UPPER(TRIM(p.nombre_razon_social)) IN (
                                    'DE VIDO JULIO',
                                    'DE VIDO JULIO MIGUEL',
                                    'DEVIDO JULIO',
                                    'JULIO DE VIDO'
                                ) THEN 'DE VIDO JULIO MIGUEL'
                                
                                -- Ricardo Jaime
                                WHEN UPPER(TRIM(p.nombre_razon_social)) IN (
                                    'JAIME RICARDO',
                                    'JAIME RICARDO RUBEN',
                                    'RICARDO JAIME'
                                ) THEN 'JAIME RICARDO'
                                
                                -- José López
                                WHEN UPPER(TRIM(p.nombre_razon_social)) IN (
                                    'LOPEZ JOSE',
                                    'LOPEZ JOSE FRANCISCO',
                                    'JOSE LOPEZ'
                                ) THEN 'LOPEZ JOSE'
                                
                                -- Carlos Zannini
                                WHEN UPPER(TRIM(p.nombre_razon_social)) IN (
                                    'ZANNINI CARLOS',
                                    'ZANNINI CARLOS ALBERTO',
                                    'CARLOS ZANNINI'
                                ) THEN 'ZANNINI CARLOS'
                                
                                -- Lázaro Báez
                                WHEN UPPER(TRIM(p.nombre_razon_social)) IN (
                                    'BAEZ LAZARO',
                                    'BAEZ LAZARO ANTONIO',
                                    'LAZARO BAEZ',
                                    'BÁEZ LÁZARO'
                                ) THEN 'BAEZ LAZARO'
                                
                                -- Néstor Kirchner
                                WHEN UPPER(TRIM(p.nombre_razon_social)) IN (
                                    'KIRCHNER NESTOR',
                                    'KIRCHNER NESTOR CARLOS',
                                    'NESTOR KIRCHNER'
                                ) THEN 'KIRCHNER NESTOR'
                                
                                -- Oscar Parrilli
                                WHEN UPPER(TRIM(p.nombre_razon_social)) IN (
                                    'PARRILLI OSCAR',
                                    'PARRILLI OSCAR ISIDRO',
                                    'OSCAR PARRILLI'
                                ) THEN 'PARRILLI OSCAR'
                                
                                -- Héctor Timerman
                                WHEN UPPER(TRIM(p.nombre_razon_social)) IN (
                                    'TIMERMAN HECTOR',
                                    'TIMERMAN HECTOR MARCOS',
                                    'HECTOR TIMERMAN'
                                ) THEN 'TIMERMAN HECTOR'
                                
                                -- Axel Kicillof
                                WHEN UPPER(TRIM(p.nombre_razon_social)) IN (
                                    'KICILLOF AXEL',
                                    'KICILLOF AXEL JAVIER',
                                    'AXEL KICILLOF'
                                ) THEN 'KICILLOF AXEL'
                                
                                -- Roberto Baratta
                                WHEN UPPER(TRIM(p.nombre_razon_social)) IN (
                                    'BARATTA ROBERTO',
                                    'BARATTA ROBERTO ESTEBAN',
                                    'ROBERTO BARATTA'
                                ) THEN 'BARATTA ROBERTO'
                                
                                -- Luis D'Elía
                                WHEN UPPER(TRIM(p.nombre_razon_social)) IN (
                                    'D''ELIA LUIS',
                                    'D ELIA LUIS',
                                    'DELIA LUIS',
                                    'LUIS D''ELIA'
                                ) THEN 'D''ELIA LUIS'
                                
                                -- Guillermo Moreno
                                WHEN UPPER(TRIM(p.nombre_razon_social)) IN (
                                    'MORENO GUILLERMO',
                                    'MORENO GUILLERMO DANIEL',
                                    'GUILLERMO MORENO'
                                ) THEN 'MORENO GUILLERMO'
                                
                                -- Carlos Menem
                                WHEN UPPER(TRIM(p.nombre_razon_social)) IN (
                                    'MENEM CARLOS',
                                    'MENEM CARLOS SAUL',
                                    'CARLOS MENEM'
                                ) THEN 'MENEM CARLOS'
                                
                                -- Aníbal Fernández
                                WHEN UPPER(TRIM(p.nombre_razon_social)) IN (
                                    'FERNANDEZ ANIBAL',
                                    'FERNANDEZ ANIBAL DOMINGO',
                                    'ANIBAL FERNANDEZ'
                                ) THEN 'FERNANDEZ ANIBAL'
                                
                                -- Alberto Fernández
                                WHEN UPPER(TRIM(p.nombre_razon_social)) IN (
                                    'FERNANDEZ ALBERTO',
                                    'FERNANDEZ ALBERTO ANGEL',
                                    'ALBERTO FERNANDEZ'
                                ) THEN 'FERNANDEZ ALBERTO'
                                
                                -- Jorge Capitanich
                                WHEN UPPER(TRIM(p.nombre_razon_social)) IN (
                                    'CAPITANICH JORGE',
                                    'CAPITANICH JORGE MILTON',
                                    'JORGE CAPITANICH'
                                ) THEN 'CAPITANICH JORGE'
                                
                                -- Fernando De la Rúa
                                WHEN UPPER(TRIM(p.nombre_razon_social)) IN (
                                    'DE LA RUA FERNANDO',
                                    'DE LA RUA FERNANDO JOSE',
                                    'DELARUA FERNANDO',
                                    'FERNANDO DE LA RUA',
                                    'DE LA RÚA FERNANDO'
                                ) THEN 'DE LA RUA FERNANDO'
                                
                                -- Domingo Cavallo
                                WHEN UPPER(TRIM(p.nombre_razon_social)) IN (
                                    'CAVALLO DOMINGO',
                                    'CAVALLO DOMINGO FELIPE',
                                    'DOMINGO CAVALLO'
                                ) THEN 'CAVALLO DOMINGO'
                                
                                -- María Julia Alsogaray
                                WHEN UPPER(TRIM(p.nombre_razon_social)) IN (
                                    'ALSOGARAY MARIA JULIA',
                                    'MARIA JULIA ALSOGARAY',
                                    'ALSOGARAY JULIA'
                                ) THEN 'ALSOGARAY MARIA JULIA'
                                
                                -- Si no coincide con ninguno, devolver el nombre limpio
                                ELSE UPPER(TRIM(p.nombre_razon_social))
                            END,
                            ' DE LA ', ' De La '
                        ),
                        ' DE ', ' De '
                    ),
                    '^DE ', 'De ', 'g'
                ) AS persona,
                
                -- Contar DISTINCT parte_id para evitar duplicados por múltiples roles
                COUNT(DISTINCT p.parte_id) AS cantidad_causas
            FROM parte p
            JOIN rol_parte rp ON rp.parte_id = p.parte_id
            WHERE LOWER(rp.nombre) = 'denunciado'
              AND p.nombre_razon_social IS NOT NULL
              AND p.nombre_razon_social != ''
              AND UPPER(TRIM(p.nombre_razon_social)) != 'NAN'
              -- ✅ Excluir homónimos conocidos
              AND UPPER(TRIM(p.nombre_razon_social)) NOT IN (
                  'FERNANDEZ DELIA CRISTINA',
                  'FERNANDEZ MOLINA MARIA CRISTINA',
                  'MACRI FRANCO',
                  'MACRI GIANFRANCO'
              )
            GROUP BY persona  -- ✅ Agrupar por el nombre normalizado
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

