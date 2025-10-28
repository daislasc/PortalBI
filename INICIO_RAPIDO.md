# 🚀 Portal BI - Inicio Rápido

## ⚡ Comenzar en 3 Pasos

### 1️⃣ Instalar Dependencias
```bash
pip install -r requirements.txt
```

### 2️⃣ Verificar Estructura (Opcional)
```bash
python test_structure.py
```

### 3️⃣ Ejecutar Portal
```bash
python run.py
```

**¡Listo!** El portal se abrirá en `http://localhost:8501`

---

## 📖 ¿Qué cambió?

✅ **Misma UI/UX** - Experiencia idéntica para usuarios  
✅ **Código organizado** - Arquitectura modular y escalable  
✅ **Fácil mantenimiento** - Agregar dashboards sin tocar código  

---

## 🎯 Tareas Comunes

### Agregar Dashboard
1. Abrir: `src/config/dashboards.yaml`
2. Agregar:
```yaml
Sección:
  - title: "Nombre"
    url_dashboard: "https://..."
    url_docu: "https://..."
    color: "#18515F"
```
3. Guardar y recargar el portal

### Cambiar Logo
1. Reemplazar: `assets/images/ingetek-logo-completo.png`
2. Recargar el portal

### Cambiar Colores
1. Editar: `src/config/settings.py`
2. Modificar valores en `BRAND_COLORS`
3. Recargar el portal

---

## 📚 Documentación Completa

| Archivo | Contenido |
|---------|-----------|
| `README.md` | Guía completa de instalación y uso |
| `docs/architecture.md` | Arquitectura y cómo extender |
| `docs/migration_guide.md` | Detalles de la migración |
| `docs/examples.md` | Ejemplos de código |
| `ESTRUCTURA_NUEVA.md` | Resumen de estructura |

---

## 🆘 Problemas Comunes

### "Module not found"
**Solución**: Usar `python run.py` en lugar de `streamlit run src/app.py`

### "File not found: dashboards.yaml"
**Solución**: Verificar que existe `src/config/dashboards.yaml`

### Imágenes no cargan
**Solución**: Verificar que existen en `assets/images/`

---

## 💡 Siguiente Nivel

Para agregar features avanzados:
- 🔐 Autenticación → Ver `docs/examples.md`
- ⭐ Favoritos → Ver `docs/examples.md`
- 📊 Analytics → Ver `docs/examples.md`
- 🎨 Temas → Ver `docs/examples.md`

---

**¿Preguntas?** Consulta `README.md` o `docs/architecture.md`

