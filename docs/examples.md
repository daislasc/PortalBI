# Ejemplos de Uso y Extensión

## 📚 Casos de Uso Comunes

### 1. Agregar un Nuevo Dashboard

**Escenario**: Necesitas agregar un dashboard de "Recursos Humanos"

**Solución**: Edita `src/config/dashboards.yaml`

```yaml
dashboards:
  # ... secciones existentes ...
  
  Recursos Humanos:
    - title: "Plantilla de Personal"
      url_dashboard: "https://lookerstudio.google.com/..."
      url_docu: "https://docs.company.com/..."
      color: "#18515F"
    
    - title: "Evaluación de Desempeño"
      url_dashboard: "https://lookerstudio.google.com/..."
      url_docu: "https://docs.company.com/..."
      color: "#18515F"
```

**Resultado**: Nueva sección aparecerá automáticamente en el sidebar

---

### 2. Cambiar Colores del Portal

**Escenario**: Actualizar los colores corporativos

**Solución**: Edita `src/config/settings.py`

```python
BRAND_COLORS = {
    "primary": "#1A5F7A",      # Nuevo color primario
    "secondary": "#2D89A3",    # Nuevo color secundario
    "accent": "#57C4E5",       # Nuevo color de acento
    "background": "#FFFFFF",
    "border": "#CCCCCC"
}
```

**Resultado**: Aplica los nuevos colores en toda la aplicación

---

### 3. Personalizar el Logo

**Escenario**: Actualizar el logo corporativo

**Solución**: 

1. Reemplaza la imagen en `assets/images/ingetek-logo-completo.png`
2. Ajusta el tamaño en `src/config/settings.py`:

```python
UI_CONFIG = {
    "logo_path": str(IMAGES_DIR / "ingetek-logo-completo.png"),
    "logo_width": 400,  # Cambiar tamaño
    ...
}
```

---

### 4. Cambiar Layout de Grid

**Escenario**: Mostrar 4 tarjetas por fila en lugar de 3

**Solución**: Edita `src/config/settings.py`

```python
UI_CONFIG = {
    ...
    "cards_per_row": 4,  # Cambiar de 3 a 4
}
```

---

## 🚀 Ejemplos de Extensión Avanzada

### Ejemplo 1: Agregar Sistema de Favoritos

#### Paso 1: Crear Servicio de Favoritos

Crea `src/services/favorites_service.py`:

```python
"""
Servicio para gestión de favoritos
"""
from typing import List, Set
from pathlib import Path
import json


class FavoritesService:
    """Gestiona los dashboards favoritos del usuario"""
    
    def __init__(self, storage_file: str = "favorites.json"):
        self.storage_path = Path(__file__).parent.parent.parent / storage_file
        self._favorites: Set[str] = self._load_favorites()
    
    def _load_favorites(self) -> Set[str]:
        """Carga favoritos desde archivo JSON"""
        if not self.storage_path.exists():
            return set()
        
        with open(self.storage_path, 'r') as f:
            data = json.load(f)
            return set(data.get('favorites', []))
    
    def _save_favorites(self) -> None:
        """Guarda favoritos a archivo JSON"""
        with open(self.storage_path, 'w') as f:
            json.dump({'favorites': list(self._favorites)}, f)
    
    def add_favorite(self, dashboard_title: str) -> None:
        """Agrega un dashboard a favoritos"""
        self._favorites.add(dashboard_title)
        self._save_favorites()
    
    def remove_favorite(self, dashboard_title: str) -> None:
        """Remueve un dashboard de favoritos"""
        self._favorites.discard(dashboard_title)
        self._save_favorites()
    
    def is_favorite(self, dashboard_title: str) -> bool:
        """Verifica si un dashboard es favorito"""
        return dashboard_title in self._favorites
    
    def get_all_favorites(self) -> List[str]:
        """Obtiene todos los favoritos"""
        return list(self._favorites)
```

#### Paso 2: Actualizar Componente de Tarjeta

Modifica `src/components/dashboard_card.py`:

```python
import streamlit as st
from ..models import Dashboard

def render_dashboard_card(dashboard: Dashboard, is_favorite: bool = False, 
                         on_favorite_click=None) -> None:
    """
    Renderiza una tarjeta de dashboard con botón de favorito
    """
    favorite_icon = "⭐" if is_favorite else "☆"
    
    col1, col2 = st.columns([4, 1])
    
    with col1:
        st.markdown(f"### {dashboard.title}")
    
    with col2:
        if st.button(favorite_icon, key=f"fav_{dashboard.title}"):
            if on_favorite_click:
                on_favorite_click(dashboard.title)
    
    # ... resto del código de tarjeta ...
```

#### Paso 3: Integrar en App Principal

Actualiza `src/app.py`:

```python
from services import DashboardService
from services.favorites_service import FavoritesService
from components import render_sidebar, render_dashboard_card

def main():
    initialize_page()
    render_header()
    
    # Inicializar servicios
    dashboard_service = DashboardService()
    favorites_service = FavoritesService()
    
    # Callback para favoritos
    def toggle_favorite(dashboard_title: str):
        if favorites_service.is_favorite(dashboard_title):
            favorites_service.remove_favorite(dashboard_title)
        else:
            favorites_service.add_favorite(dashboard_title)
        st.rerun()
    
    # Renderizar con favoritos
    section_data = dashboard_service.get_section(selected_section)
    
    for dashboard in section_data.dashboards:
        is_fav = favorites_service.is_favorite(dashboard.title)
        render_dashboard_card(dashboard, is_fav, toggle_favorite)
```

---

### Ejemplo 2: Agregar Autenticación Simple

#### Paso 1: Crear Servicio de Autenticación

Crea `src/services/auth_service.py`:

```python
"""
Servicio de autenticación básica
"""
import hashlib
from typing import Optional, Dict


class AuthService:
    """Gestiona autenticación de usuarios"""
    
    def __init__(self):
        # En producción, usar base de datos
        self._users: Dict[str, str] = {
            "admin": self._hash_password("admin123"),
            "user": self._hash_password("user123")
        }
    
    def _hash_password(self, password: str) -> str:
        """Hashea una contraseña"""
        return hashlib.sha256(password.encode()).hexdigest()
    
    def authenticate(self, username: str, password: str) -> bool:
        """
        Autentica un usuario
        
        Returns:
            True si las credenciales son válidas
        """
        if username not in self._users:
            return False
        
        hashed_password = self._hash_password(password)
        return self._users[username] == hashed_password
    
    def get_user_role(self, username: str) -> str:
        """Obtiene el rol del usuario"""
        if username == "admin":
            return "admin"
        return "user"
```

#### Paso 2: Crear Componente de Login

Crea `src/components/login.py`:

```python
"""
Componente de login
"""
import streamlit as st


def render_login_form() -> tuple[str, str]:
    """
    Renderiza formulario de login
    
    Returns:
        Tupla (username, password)
    """
    st.markdown("## 🔐 Portal BI - Login")
    
    with st.form("login_form"):
        username = st.text_input("Usuario")
        password = st.text_input("Contraseña", type="password")
        submit = st.form_submit_button("Ingresar")
        
        if submit:
            return username, password
    
    return None, None
```

#### Paso 3: Integrar en App

Actualiza `src/app.py`:

```python
import streamlit as st
from services.auth_service import AuthService
from components.login import render_login_form

def main():
    # Inicializar servicio de auth
    auth_service = AuthService()
    
    # Verificar sesión
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
    
    # Si no está autenticado, mostrar login
    if not st.session_state.authenticated:
        username, password = render_login_form()
        
        if username and password:
            if auth_service.authenticate(username, password):
                st.session_state.authenticated = True
                st.session_state.username = username
                st.rerun()
            else:
                st.error("❌ Credenciales inválidas")
        return
    
    # Usuario autenticado - mostrar portal normal
    initialize_page()
    render_header()
    
    # Botón de logout
    if st.sidebar.button("🚪 Cerrar Sesión"):
        st.session_state.authenticated = False
        st.rerun()
    
    # ... resto del código del portal ...
```

---

### Ejemplo 3: Agregar Analytics de Uso

#### Paso 1: Crear Servicio de Analytics

Crea `src/services/analytics_service.py`:

```python
"""
Servicio de analytics
"""
from datetime import datetime
from pathlib import Path
import json
from typing import List, Dict


class AnalyticsService:
    """Rastrea el uso de dashboards"""
    
    def __init__(self, storage_file: str = "analytics.json"):
        self.storage_path = Path(__file__).parent.parent.parent / storage_file
        self._views: List[Dict] = self._load_views()
    
    def _load_views(self) -> List[Dict]:
        """Carga historial de vistas"""
        if not self.storage_path.exists():
            return []
        
        with open(self.storage_path, 'r') as f:
            data = json.load(f)
            return data.get('views', [])
    
    def _save_views(self) -> None:
        """Guarda historial de vistas"""
        with open(self.storage_path, 'w') as f:
            json.dump({'views': self._views}, f, indent=2)
    
    def track_view(self, dashboard_title: str, section: str, 
                   user: str = "anonymous") -> None:
        """
        Registra una vista de dashboard
        
        Args:
            dashboard_title: Título del dashboard
            section: Sección a la que pertenece
            user: Usuario que vio el dashboard
        """
        view = {
            "dashboard": dashboard_title,
            "section": section,
            "user": user,
            "timestamp": datetime.now().isoformat()
        }
        
        self._views.append(view)
        self._save_views()
    
    def get_most_viewed(self, limit: int = 10) -> List[tuple[str, int]]:
        """
        Obtiene los dashboards más vistos
        
        Returns:
            Lista de tuplas (dashboard_title, view_count)
        """
        from collections import Counter
        
        dashboard_views = Counter(
            view['dashboard'] for view in self._views
        )
        
        return dashboard_views.most_common(limit)
    
    def get_views_by_section(self) -> Dict[str, int]:
        """Obtiene vistas agrupadas por sección"""
        from collections import Counter
        
        return dict(Counter(
            view['section'] for view in self._views
        ))
```

#### Paso 2: Integrar Tracking en Tarjetas

Modifica `src/components/dashboard_card.py`:

```python
def render_dashboard_card(dashboard: Dashboard, on_click=None) -> None:
    """Renderiza tarjeta con tracking"""
    
    # ... código de renderizado ...
    
    # Agregar tracking al botón
    if st.button("Abrir Dashboard", key=f"open_{dashboard.title}"):
        if on_click:
            on_click(dashboard)
        # Abrir en nueva pestaña
        st.markdown(
            f'<meta http-equiv="refresh" content="0; url={dashboard.url_dashboard}" />',
            unsafe_allow_html=True
        )
```

#### Paso 3: Usar en App

```python
from services.analytics_service import AnalyticsService

def main():
    # ...
    analytics_service = AnalyticsService()
    
    def handle_dashboard_click(dashboard):
        """Callback cuando se abre un dashboard"""
        analytics_service.track_view(
            dashboard.title,
            selected_section,
            st.session_state.get('username', 'anonymous')
        )
    
    # Renderizar con tracking
    for dashboard in section_data.dashboards:
        render_dashboard_card(dashboard, on_click=handle_dashboard_click)
    
    # Mostrar estadísticas en sidebar
    if st.sidebar.checkbox("📊 Mostrar Estadísticas"):
        st.sidebar.subheader("Dashboards Más Vistos")
        most_viewed = analytics_service.get_most_viewed(5)
        for title, count in most_viewed:
            st.sidebar.text(f"{title}: {count} vistas")
```

---

## 🎨 Personalización de UI

### Ejemplo: Agregar Tema Oscuro

#### Paso 1: Definir Temas

Edita `src/config/settings.py`:

```python
THEMES = {
    "light": {
        "primary": "#18515F",
        "background": "#FFFFFF",
        "card_bg": "#FFFFFF",
        "text": "#262730",
        "border": "#DDDDDD"
    },
    "dark": {
        "primary": "#4A9FB0",
        "background": "#1E1E1E",
        "card_bg": "#2D2D2D",
        "text": "#FFFFFF",
        "border": "#444444"
    }
}
```

#### Paso 2: Crear Selector de Tema

Crea `src/components/theme_selector.py`:

```python
import streamlit as st

def render_theme_selector():
    """Renderiza selector de tema"""
    if "theme" not in st.session_state:
        st.session_state.theme = "light"
    
    theme = st.sidebar.selectbox(
        "🎨 Tema",
        ["light", "dark"],
        index=0 if st.session_state.theme == "light" else 1
    )
    
    if theme != st.session_state.theme:
        st.session_state.theme = theme
        st.rerun()
    
    return theme
```

#### Paso 3: Aplicar Tema

Modifica `src/components/dashboard_card.py`:

```python
from ..config import THEMES

def render_dashboard_card(dashboard: Dashboard, theme: str = "light") -> None:
    """Renderiza tarjeta con tema aplicado"""
    colors = THEMES[theme]
    
    st.markdown(f"""
    <div style="
        background-color: {colors['card_bg']};
        color: {colors['text']};
        border: 1px solid {colors['border']};
        ...
    ">
        <h3 style="color:{colors['primary']};">{dashboard.title}</h3>
        ...
    </div>
    """, unsafe_allow_html=True)
```

---

## 📱 Ejemplos de Integración

### Integración con Base de Datos

```python
# src/services/database_service.py
import sqlite3
from pathlib import Path

class DatabaseService:
    def __init__(self, db_path: str = "portal.db"):
        self.db_path = Path(__file__).parent.parent.parent / db_path
        self._init_db()
    
    def _init_db(self):
        """Inicializa base de datos"""
        conn = sqlite3.connect(self.db_path)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS dashboards (
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                url_dashboard TEXT NOT NULL,
                url_docu TEXT NOT NULL,
                section TEXT NOT NULL,
                color TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.close()
    
    def get_dashboards_by_section(self, section: str):
        """Obtiene dashboards de una sección"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.execute(
            "SELECT * FROM dashboards WHERE section = ?", (section,)
        )
        results = cursor.fetchall()
        conn.close()
        return results
```

---

## 🧪 Ejemplos de Tests

```python
# tests/test_dashboard_service.py
import unittest
from src.services.dashboard_service import DashboardService
from src.models import Dashboard

class TestDashboardService(unittest.TestCase):
    
    def setUp(self):
        """Setup antes de cada test"""
        self.service = DashboardService()
    
    def test_get_sections(self):
        """Test obtener secciones"""
        sections = self.service.get_sections()
        self.assertIsInstance(sections, list)
        self.assertGreater(len(sections), 0)
    
    def test_get_section(self):
        """Test obtener dashboards de sección"""
        section = self.service.get_section("Operación")
        self.assertGreater(len(section.dashboards), 0)
    
    def test_dashboard_structure(self):
        """Test estructura de dashboard"""
        section = self.service.get_section("Operación")
        dashboard = section.dashboards[0]
        
        self.assertIsInstance(dashboard, Dashboard)
        self.assertTrue(hasattr(dashboard, 'title'))
        self.assertTrue(hasattr(dashboard, 'url_dashboard'))
        self.assertTrue(hasattr(dashboard, 'url_docu'))
        self.assertTrue(hasattr(dashboard, 'color'))
```

---

## 💡 Tips y Mejores Prácticas

### 1. Manejo de Errores

```python
# Siempre manejar excepciones
try:
    dashboard_service = DashboardService()
except Exception as e:
    st.error(f"Error al cargar dashboards: {str(e)}")
    st.stop()
```

### 2. Logging

```python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info("Portal iniciado")
logger.error("Error al cargar configuración")
```

### 3. Cache de Streamlit

```python
@st.cache_data
def load_dashboards():
    """Cachea la carga de dashboards"""
    service = DashboardService()
    return service.get_all_dashboards()
```

### 4. Variables de Entorno

```python
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///portal.db")
SECRET_KEY = os.getenv("SECRET_KEY", "change-me-in-production")
```

---

¿Necesitas más ejemplos? Revisa:
- `docs/architecture.md` para extensiones sugeridas
- `src/` para código de referencia
- `README.md` para guías de instalación

