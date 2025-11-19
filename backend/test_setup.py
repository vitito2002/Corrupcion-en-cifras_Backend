#!/usr/bin/env python3
"""
Script de verificación rápida del setup del proyecto.
Ejecutar: python test_setup.py
"""

import sys

def test_imports():
    """Verifica que todas las importaciones funcionan"""
    print("🔍 Verificando importaciones...")
    
    try:
        from app.core.config import settings
        print("  ✅ app.core.config")
    except Exception as e:
        print(f"  ❌ app.core.config: {e}")
        return False
    
    try:
        from app.core.database import engine, SessionLocal, Base
        print("  ✅ app.core.database")
    except Exception as e:
        print(f"  ❌ app.core.database: {e}")
        return False
    
    try:
        from app.main import app
        print("  ✅ app.main")
    except Exception as e:
        print(f"  ❌ app.main: {e}")
        return False
    
    return True

def test_config():
    """Verifica que la configuración se carga correctamente"""
    print("\n🔍 Verificando configuración...")
    
    try:
        from app.core.config import settings
        if settings.DATABASE_URL:
            print(f"  ✅ DATABASE_URL configurada: {settings.DATABASE_URL[:50]}...")
            return True
        else:
            print("  ❌ DATABASE_URL vacía")
            return False
    except Exception as e:
        print(f"  ❌ Error cargando configuración: {e}")
        return False

def test_fastapi():
    """Verifica que FastAPI está configurado correctamente"""
    print("\n🔍 Verificando FastAPI...")
    
    try:
        from app.main import app
        if app.title == "Corrupción en Cifras API":
            print(f"  ✅ Título correcto: {app.title}")
        else:
            print(f"  ⚠️  Título inesperado: {app.title}")
        
        # Verificar que tiene el endpoint raíz
        routes = [route.path for route in app.routes]
        if "/" in routes:
            print("  ✅ Endpoint raíz '/' configurado")
            return True
        else:
            print("  ❌ Endpoint raíz '/' no encontrado")
            return False
    except Exception as e:
        print(f"  ❌ Error verificando FastAPI: {e}")
        return False

if __name__ == "__main__":
    print("=" * 50)
    print("🧪 Verificación del Setup del Proyecto")
    print("=" * 50)
    
    all_ok = True
    all_ok &= test_imports()
    all_ok &= test_config()
    all_ok &= test_fastapi()
    
    print("\n" + "=" * 50)
    if all_ok:
        print("✅ Todas las verificaciones pasaron correctamente!")
        print("\n📝 Próximos pasos:")
        print("   1. Instalar dependencias: pip install -r requirements.txt")
        print("   2. Ejecutar: uvicorn app.main:app --reload")
        print("   3. Abrir: http://localhost:8000")
        sys.exit(0)
    else:
        print("❌ Algunas verificaciones fallaron")
        sys.exit(1)

