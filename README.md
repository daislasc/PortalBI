# Portal BI - Ingetek

Portal de visualización de dashboards de Business Intelligence construido con Streamlit.

## 📋 Descripción

Este portal proporciona acceso centralizado a múltiples dashboards de Looker Studio, organizados por áreas funcionales:
- **Operación**: Dashboards de producción, embarques, órdenes e inventario
- **Contabilidad y Finanzas**: Costos de fabricación
- **Back-Office**: Kardex de documentos
- **Comercial**: Proyectos, deuda comercial y oportunidades de Salesforce
- **Looker Studio Docs**: Documentación y ejemplos

## 🏗️ Estructura del Proyecto

```
PortalBI/
├── src/
│   ├── app.py                 # Aplicación principal
│   ├── config/
│   │   ├── settings.py        # Configuraciones generales
│   │   └── dashboards.yaml    # Definición de dashboards
│   ├── components/
│   │   ├── dashboard_card.py  # Componente de tarjeta
│   │   └── sidebar.py         # Componente de navegación
│   ├── models/
│   │   └── dashboard.py       # Modelos de datos
│   ├── services/
│   │   └── dashboard_service.py  # Lógica de negocio
│   └── utils/
│       └── helpers.py         # Funciones auxiliares
├── assets/
│   ├── images/                # Logos e imágenes
│   └── styles/                # Estilos personalizados
├── docs/
│   └── instructivo_dashboards.md  # Documentación
├── tests/                     # Tests unitarios (futuro)
├── requirements.txt           # Dependencias
└── README.md                  # Este archivo
```

## 🚀 Instalación

1. **Clonar el repositorio**
```bash
git clone <repository-url>
cd PortalBI
```

2. **Crear entorno virtual**
```bash
python -m venv .venv
```

3. **Activar entorno virtual**
- Windows:
```bash
.venv\Scripts\activate
```
- Linux/Mac:
```bash
source .venv/bin/activate
```

4. **Instalar dependencias**
```bash
pip install -r requirements.txt
```

## ▶️ Ejecución

Desde el directorio raíz del proyecto:

```bash
streamlit run src/app.py
```

La aplicación se abrirá automáticamente en `http://localhost:8501`

## 📝 Configuración

### Agregar nuevos dashboards

Edita el archivo `src/config/dashboards.yaml`:

```yaml
dashboards:
  Nueva Sección:
    - title: "Nombre del Dashboard"
      url_dashboard: "URL del dashboard en Looker Studio"
      url_docu: "URL de la documentación"
      color: "#18515F"
```

### Personalizar estilos

Modifica los colores corporativos en `src/config/settings.py`:

```python
BRAND_COLORS = {
    "primary": "#18515F",
    "secondary": "#2A7C8F",
    ...
}
```

## 🎨 Características

- ✅ **Arquitectura modular**: Separación clara de responsabilidades
- ✅ **Configuración externalizada**: Dashboards en YAML
- ✅ **Componentes reutilizables**: Fácil extensión y mantenimiento
- ✅ **Diseño responsivo**: Grid adaptable de tarjetas
- ✅ **Navegación intuitiva**: Sidebar con secciones organizadas
- ✅ **Escalable**: Estructura preparada para crecimiento

## 🔧 Desarrollo

### Agregar nuevos componentes

Crea nuevos archivos en `src/components/` y regístralos en `__init__.py`

### Agregar nuevos servicios

Crea nuevos servicios en `src/services/` para lógica de negocio adicional

### Tests

Los tests se ubicarán en el directorio `tests/` (estructura preparada para futuro)

## 📦 Dependencias

- **Streamlit**: Framework de aplicación web
- **PyYAML**: Manejo de archivos de configuración

## 🤝 Contribución

Para contribuir al proyecto:
1. Crea una rama feature
2. Realiza tus cambios
3. Crea un Pull Request

## 📄 Licencia

© Ingetek - Todos los derechos reservados

## 👥 Contacto

Para soporte o consultas, contacta al equipo de BI de Ingetek.

