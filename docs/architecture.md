# Arquitectura del Portal BI

## 📐 Principios de Diseño

El Portal BI ha sido estructurado siguiendo principios de arquitectura limpia y escalable:

### 1. Separación de Responsabilidades
- **Presentación** (`components/`): Componentes UI reutilizables
- **Lógica de Negocio** (`services/`): Servicios que manejan la lógica
- **Modelos** (`models/`): Estructuras de datos y schemas
- **Configuración** (`config/`): Parámetros y datos externos
- **Utilidades** (`utils/`): Funciones auxiliares

### 2. Configuración Externalizada
Los dashboards se definen en `config/dashboards.yaml`, permitiendo:
- Agregar/modificar dashboards sin cambiar código
- Mantener configuración versionada
- Fácil gestión por no-desarrolladores

### 3. Modularidad
Cada componente es independiente y puede ser:
- Probado individualmente
- Reutilizado en diferentes contextos
- Modificado sin afectar otros módulos

## 🏛️ Estructura de Capas

```
┌─────────────────────────────────────┐
│         app.py (Entry Point)        │
│     Orquesta la aplicación          │
└─────────────────┬───────────────────┘
                  │
    ┌─────────────┼─────────────┐
    │             │             │
┌───▼────┐   ┌───▼────┐   ┌───▼────┐
│Components│   │Services│   │ Config │
│  (UI)    │   │(Logic) │   │(Data)  │
└───┬────┘   └───┬────┘   └────────┘
    │             │
    └──────┬──────┘
           │
      ┌────▼────┐
      │  Models │
      │ (Schema)│
      └─────────┘
```

## 📦 Módulos Principales

### `app.py`
Punto de entrada de la aplicación. Orquesta:
- Configuración de página
- Inicialización de servicios
- Renderizado de componentes
- Flujo de navegación

**Diseño**: Mantener limpio, delegar lógica a servicios

### `services/dashboard_service.py`
Gestiona la carga y acceso a dashboards:
- Lee configuración YAML
- Crea objetos Dashboard
- Proporciona métodos de consulta
- Maneja errores de configuración

**Extensión**: Agregar cache, validaciones, logging

### `models/dashboard.py`
Define las estructuras de datos:
- `Dashboard`: Representa un dashboard individual
- `DashboardSection`: Agrupa dashboards por sección

**Extensión**: Agregar metadatos, permisos, favoritos

### `components/`
Componentes UI reutilizables:
- `dashboard_card.py`: Tarjeta individual de dashboard
- `sidebar.py`: Menú de navegación

**Extensión**: Agregar filtros, búsqueda, temas

### `config/`
Configuración centralizada:
- `settings.py`: Parámetros generales
- `dashboards.yaml`: Definición de dashboards

**Extensión**: Agregar múltiples ambientes (dev/prod)

## 🔧 Flujo de Datos

```
1. Usuario inicia app
   └─> app.py carga PAGE_CONFIG
   
2. app.py inicializa DashboardService
   └─> DashboardService lee dashboards.yaml
       └─> Crea objetos Dashboard
       
3. Usuario navega por secciones
   └─> sidebar.py renderiza opciones
       └─> Usuario selecciona sección
       
4. app.py obtiene dashboards de la sección
   └─> DashboardService retorna DashboardSection
       └─> dashboard_card.py renderiza cada tarjeta
```

## 🚀 Cómo Extender el Portal

### Agregar Autenticación

1. Crear `services/auth_service.py`:
```python
class AuthService:
    def authenticate(self, username, password):
        # Lógica de autenticación
        pass
    
    def get_user_permissions(self, user):
        # Obtener permisos del usuario
        pass
```

2. Actualizar `models/dashboard.py`:
```python
@dataclass
class Dashboard:
    # ... campos existentes ...
    required_permissions: List[str] = field(default_factory=list)
```

3. Modificar `app.py` para incluir login

### Agregar Favoritos

1. Crear `services/favorites_service.py`:
```python
class FavoritesService:
    def add_favorite(self, user_id, dashboard_id):
        pass
    
    def get_user_favorites(self, user_id):
        pass
```

2. Agregar componente `components/favorites.py`

3. Integrar en `app.py`

### Agregar Analytics

1. Crear `services/analytics_service.py`:
```python
class AnalyticsService:
    def track_dashboard_view(self, dashboard_id, user_id):
        pass
    
    def get_dashboard_stats(self):
        pass
```

2. Integrar tracking en `dashboard_card.py`

### Agregar Base de Datos

1. Crear `services/database_service.py`
2. Modificar `DashboardService` para leer de DB
3. Agregar modelos ORM en `models/`

### Agregar Tests

Estructura en `tests/`:
```
tests/
├── test_models.py
├── test_services.py
├── test_components.py
└── test_integration.py
```

## 🎨 Personalización UI

### Temas Dinámicos

1. Agregar en `config/settings.py`:
```python
THEMES = {
    "light": {...},
    "dark": {...}
}
```

2. Crear `components/theme_selector.py`

### Layouts Personalizados

1. Crear `components/layouts.py`:
```python
def grid_layout(items, columns):
    pass

def list_layout(items):
    pass
```

2. Permitir usuario seleccionar layout

## 📊 Monitoreo y Logging

### Agregar Logging

1. Crear `utils/logger.py`:
```python
import logging

def get_logger(name):
    logger = logging.getLogger(name)
    # Configurar handlers
    return logger
```

2. Usar en servicios:
```python
from utils.logger import get_logger

logger = get_logger(__name__)
logger.info("Dashboard loaded")
```

## 🔐 Buenas Prácticas

1. **Nunca hardcodear credenciales**: Usar variables de entorno
2. **Validar inputs**: Especialmente en archivos de configuración
3. **Manejar errores**: Try-except en puntos críticos
4. **Documentar cambios**: Actualizar README y docs
5. **Versionar configuración**: Commit de dashboards.yaml
6. **Tests antes de deploy**: Ejecutar suite de tests

## 📚 Recursos Adicionales

- [Documentación Streamlit](https://docs.streamlit.io/)
- [Clean Architecture](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)
- [Python Best Practices](https://realpython.com/tutorials/best-practices/)

