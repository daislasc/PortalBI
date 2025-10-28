"""
Componente de tarjeta de dashboard
"""
import streamlit as st
from models import Dashboard


def render_dashboard_card(dashboard: Dashboard) -> None:
    """
    Renderiza una tarjeta de dashboard con su información
    
    Args:
        dashboard: Objeto Dashboard con la información a mostrar
    """
    st.markdown(f"""
    <div style="
        border: 1px solid #ddd; 
        border-radius: 12px; 
        padding: 20px; 
        margin: 10px 0; 
        box-shadow: 0 4px 12px rgba(0,0,0,0.15); 
        background-color: #fff;
        min-height: 160px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    ">
        <h3 style="color:{dashboard.color}; margin-bottom:8px;">{dashboard.title}</h3>
        <p style="font-size:14px; color:#18515F; font-weight:bold;">
            <a href="{dashboard.url_docu}" target="_blank" style="color:{dashboard.color}; text-decoration:underline;">
                Documentación y Autoservicio
            </a>
        </p>
        <a href="{dashboard.url_dashboard}" target="_blank" style="
            text-decoration:none; 
            color:white; 
            background-color:{dashboard.color}; 
            padding:10px 14px; 
            border-radius:6px;
            font-weight:bold;
            text-align:center;
            display:block;
        ">Abrir Dashboard</a>
    </div>
    """, unsafe_allow_html=True)


def render_dashboard_grid(dashboards: list[Dashboard], columns: int = 3) -> None:
    """
    Renderiza una grilla de tarjetas de dashboards
    
    Args:
        dashboards: Lista de dashboards a renderizar
        columns: Número de columnas en la grilla
    """
    if not dashboards:
        st.info("No hay dashboards disponibles en esta sección.")
        return
    
    for i in range(0, len(dashboards), columns):
        cols = st.columns(columns)
        for j, dashboard in enumerate(dashboards[i:i+columns]):
            with cols[j]:
                render_dashboard_card(dashboard)

