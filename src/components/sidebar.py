"""
Componente del sidebar de navegación
"""
import streamlit as st
from typing import List


def render_sidebar(sections: List[str], title: str = "Menú de Navegación") -> str:
    """
    Renderiza el sidebar con las secciones disponibles
    
    Args:
        sections: Lista de secciones disponibles
        title: Título del sidebar
        
    Returns:
        Sección seleccionada por el usuario
    """
    st.sidebar.title(title)
    selected_section = st.sidebar.radio("Secciones:", sections)
    return selected_section

