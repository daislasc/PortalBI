# Changelog - Portal BI

## [2.0.0] - 2025-10-28

### 🎉 Restructuración Completa del Proyecto

#### ✨ Agregado
- **Arquitectura modular escalable**: Separación clara de componentes, servicios, modelos y configuración
- **Configuración externalizada**: Dashboards definidos en YAML (`src/config/dashboards.yaml`)
- **Modelos de datos**: Classes `Dashboard` y `DashboardSection` con validación
- **Servicios reutilizables**: `DashboardService` para gestión de dashboards
- **Componentes UI modulares**: 
  - `dashboard_card.py`: Tarjetas reutilizables
  - `sidebar.py`: Navegación modular
- **Documentación completa**:
  - `README.md`: Guía de uso e instalación
  - `docs/architecture.md`: Arquitectura y extensiones
  - `docs/instructivo_dashboards.md`: Instructivo de dashboards
- **Gestión de dependencias**: `requirements.txt` con versiones especificadas
- **Configuración de proyecto**:
  - `.gitignore`: Ignorar archivos innecesarios
  - `.streamlit/config.toml`: Configuración de Streamlit
  - `run.py`: Script de ejecución simplificado
- **Estructura de tests**: Carpeta preparada para testing futuro

#### 📁 Nueva Estructura de Directorios
```
PortalBI/
├── src/                        # Código fuente
│   ├── app.py                  # Entry point
│   ├── config/                 # Configuración
│   ├── components/             # Componentes UI
│   ├── models/                 # Modelos de datos
│   ├── services/               # Lógica de negocio
│   └── utils/                  # Utilidades
├── assets/                     # Assets estáticos
│   ├── images/                 # Logos e imágenes
│   └── styles/                 # CSS personalizado
├── docs/                       # Documentación
├── tests/                      # Tests unitarios
├── requirements.txt            # Dependencias
├── run.py                      # Script de ejecución
├── .gitignore                  # Git ignore
└── README.md                   # Documentación principal
```

#### 🔄 Migrado
- Dashboards de código Python a configuración YAML
- Imágenes a `assets/images/`
- Documentación a `docs/`
- Código monolítico a arquitectura modular

#### 🗑️ Eliminado
- Carpeta `portal-bi/` (código legacy)
- Carpeta `models/` vacía de raíz
- Código duplicado y hardcodeado

#### 🎨 Mantenido
- **UI/UX idéntico**: Misma interfaz de usuario
- **Funcionalidad completa**: Todos los dashboards funcionan igual
- **Navegación**: Mismo flujo de usuario

#### 🚀 Mejoras de Escalabilidad
- **Agregar dashboards**: Solo editar YAML, sin tocar código
- **Extensible**: Fácil agregar autenticación, favoritos, analytics
- **Mantenible**: Código organizado y documentado
- **Testeable**: Estructura preparada para tests
- **Configurable**: Separación de configuración y código

### 🔧 Detalles Técnicos

#### Dependencias
- `streamlit >= 1.28.0`: Framework web
- `PyYAML >= 6.0.1`: Parsing de configuración

#### Compatibilidad
- Python 3.8+
- Windows, Linux, macOS

#### Comandos de Ejecución
```bash
# Método 1: Script directo
python run.py

# Método 2: Streamlit directo
streamlit run src/app.py
```

---

## [1.0.0] - Versión Original

### Características
- Portal BI básico con Streamlit
- Dashboards hardcodeados en código Python
- Estructura monolítica en un solo archivo
- UI funcional con tarjetas y navegación

