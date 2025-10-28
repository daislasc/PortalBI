"""
Script de verificación de estructura del Portal BI
Ejecuta: python test_structure.py
"""
import sys
from pathlib import Path

# Agregar src al path
sys.path.insert(0, str(Path(__file__).parent / "src"))

def test_imports():
    """Verifica que todos los módulos se puedan importar"""
    print("🔍 Verificando imports...")
    
    try:
        from config import PAGE_CONFIG, UI_CONFIG, BRAND_COLORS
        print("✓ Config module OK")
    except Exception as e:
        print(f"✗ Config module ERROR: {e}")
        return False
    
    try:
        from models import Dashboard, DashboardSection
        print("✓ Models module OK")
    except Exception as e:
        print(f"✗ Models module ERROR: {e}")
        return False
    
    try:
        from services import DashboardService
        print("✓ Services module OK")
    except Exception as e:
        print(f"✗ Services module ERROR: {e}")
        return False
    
    try:
        from components import render_dashboard_card, render_sidebar
        print("✓ Components module OK")
    except Exception as e:
        print(f"✗ Components module ERROR: {e}")
        return False
    
    try:
        from utils import load_markdown_file
        print("✓ Utils module OK")
    except Exception as e:
        print(f"✗ Utils module ERROR: {e}")
        return False
    
    return True


def test_files():
    """Verifica que los archivos necesarios existan"""
    print("\n📁 Verificando archivos...")
    
    required_files = [
        "src/app.py",
        "src/config/settings.py",
        "src/config/dashboards.yaml",
        "src/models/dashboard.py",
        "src/services/dashboard_service.py",
        "src/components/dashboard_card.py",
        "src/components/sidebar.py",
        "assets/images/ingetek-logo.png",
        "assets/images/ingetek-logo-completo.png",
        "docs/instructivo_dashboards.md",
        "docs/architecture.md",
        "docs/migration_guide.md",
        "docs/examples.md",
        "requirements.txt",
        "README.md",
        ".gitignore",
        "run.py"
    ]
    
    all_exist = True
    for file_path in required_files:
        path = Path(file_path)
        if path.exists():
            print(f"✓ {file_path}")
        else:
            print(f"✗ {file_path} NO ENCONTRADO")
            all_exist = False
    
    return all_exist


def test_dashboard_service():
    """Verifica que el servicio de dashboards funcione"""
    print("\n🔧 Verificando DashboardService...")
    
    try:
        from services import DashboardService
        
        service = DashboardService()
        sections = service.get_sections()
        
        print(f"✓ Secciones cargadas: {len(sections)}")
        print(f"  Secciones: {', '.join(sections)}")
        
        # Verificar primera sección
        if sections:
            section_data = service.get_section(sections[0])
            print(f"✓ Dashboards en '{sections[0]}': {len(section_data.dashboards)}")
        
        return True
    except Exception as e:
        print(f"✗ DashboardService ERROR: {e}")
        return False


def main():
    """Ejecuta todas las verificaciones"""
    print("=" * 60)
    print("🚀 PORTAL BI - VERIFICACIÓN DE ESTRUCTURA")
    print("=" * 60)
    
    results = {
        "Imports": test_imports(),
        "Archivos": test_files(),
        "DashboardService": test_dashboard_service()
    }
    
    print("\n" + "=" * 60)
    print("📊 RESUMEN")
    print("=" * 60)
    
    for test_name, passed in results.items():
        status = "✓ PASS" if passed else "✗ FAIL"
        print(f"{test_name}: {status}")
    
    all_passed = all(results.values())
    
    if all_passed:
        print("\n🎉 ¡TODAS LAS VERIFICACIONES PASARON!")
        print("\n▶️  Para ejecutar el portal:")
        print("   python run.py")
        print("   o")
        print("   streamlit run src/app.py")
    else:
        print("\n⚠️  ALGUNAS VERIFICACIONES FALLARON")
        print("   Revisa los errores arriba")
    
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())

