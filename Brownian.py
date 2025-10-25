import streamlit as st
import numpy as np
import plotly.express as px

# --- Simulación de movimiento browniano simple con drift ---
def simulate_brownian_motion(sim_number, time, initial_value, min_value, max_value, drift, seed):
    steps = int(time)
    if seed != 0:
        np.random.seed(int(seed))
    
    realizations = np.empty((sim_number, steps))
    
    for i in range(sim_number):
        # Incrementos aleatorios con media = drift y varianza = 1 por unidad de tiempo
        delta = np.random.normal(loc=drift, scale=1, size=steps)
        actual_value = initial_value + np.cumsum(delta)
        # Mantener dentro de los límites, pero sin reflexión (solo recorte)
        actual_value = np.clip(actual_value, min_value, max_value)
        realizations[i, :] = actual_value
    
    mean_simul = np.mean(realizations, axis=0)
    return realizations, mean_simul


# --- Interfaz de Streamlit ---
st.title('Simulación de Movimiento Browniano con Sesgo (Drift)')

st.markdown("""
Este modelo simula un **movimiento browniano discreto** con posibilidad de incorporar un **sesgo (drift)** positivo o negativo.  
Los valores se mantienen dentro de un rango mínimo y máximo mediante recorte (sin reflexión).
""")

# Parámetros
sim_number = st.number_input('Número de simulaciones:', value=1000, min_value=1)
initial_value = st.number_input('Valor inicial:', value=5.0, min_value=0.0)
min_value = st.number_input('Valor mínimo:', value=0.0, min_value=0.0)
max_value = st.number_input('Valor máximo:', value=23.0, min_value=0.0)
time = st.number_input('Duración de la simulación (unidades de tiempo):', value=1000, min_value=1)
drift = st.number_input('Sesgo (drift):', value=0.0, step=0.01,
                        help="Valores positivos generan tendencia ascendente; negativos, descendente.")
seed = st.number_input('Semilla (0 = aleatoria):', value=1973)

# Botón de ejecución
if st.button('Ejecutar simulación'):
    realizations, mean_simul = simulate_brownian_motion(sim_number, time, initial_value, 
                                                        min_value, max_value, drift, seed)
    
    Time = np.arange(1, int(time) + 1)
    
    # --- Visualización con Plotly ---
    n_show = min(10, sim_number)
    fig = px.line(title=f'Movimiento Browniano con drift = {drift}',
                  labels={'x': 'Tiempo', 'y': 'Valor'})
    
    # Muestras de trayectorias individuales
    for i in range(n_show):
        fig.add_scatter(x=Time, y=realizations[i, :], mode='lines', 
                        line=dict(width=1), name=f'Sim {i+1}', opacity=0.4)
    
    # Promedio de todas las simulaciones
    fig.add_scatter(x=Time, y=mean_simul, mode='lines', name='Media', 
                    line=dict(color='black', width=3))
    
    # Línea punteada del valor inicial
    fig.add_hline(y=initial_value, line_dash='dot', line_color='red',
                  annotation_text='Valor inicial', annotation_position='bottom right')
    
    st.plotly_chart(fig, use_container_width=True)
    st.success("Simulación completada correctamente.")
    st.write("Elaboración: Marcelo Cardillo, Prof. Adjunto de ELEMENTOS DE ANTROPOLOGÍA Y ARQUEOLOGÍA EVOLUTIVA, Facultad de Filosofía y Letras, Universidad de Buenos Aires.")

