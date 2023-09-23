import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats

# Definición de la función para simular la probabilidad de fractura
def simular_probabilidad_fractura(cantidad_simulaciones, numero_replicas, min_prob, max_prob, tiros_interes=None):
    # Usar la distribución uniforme para generar probabilidades de fractura
    probfractura = np.random.uniform(min_prob, max_prob, cantidad_simulaciones)

    # Generar datos de tiros usando la distribución binomial
    tiros = np.random.binomial(numero_replicas, probfractura)

    # Crear un DataFrame uniendo probabilidad de fractura y número de tiros
    prior = pd.DataFrame({'probfractura': probfractura, 'tiros': tiros})

    if tiros_interes is not None:
        # Estimación de la distribución a posteriori para la probabilidad de fractura catastrófica en relación a n tiros
        posterior_tiros = prior[prior['tiros'] == tiros_interes]

        # Calcular la media de la probabilidad de fractura catastrófica en tiros_interes tiros
        mean_probabilidad_fractura = posterior_tiros['probfractura'].mean()

        # Calcular los percentiles 2.5 y 97.5 para el intervalo de confianza del 95%
        lower_percentile = np.percentile(posterior_tiros['probfractura'], 2.5)
        upper_percentile = np.percentile(posterior_tiros['probfractura'], 97.5)

        # Crear un gráfico con la distribución de densidad binomial a posteriori
        plt.hist(posterior_tiros['probfractura'], bins=30, density=True, alpha=0.5)
        plt.axvline(mean_probabilidad_fractura, color='black', linestyle='--', label='Media')
        plt.axvline(lower_percentile, color='red', linestyle='--', label='Percentil 2.5')
        plt.axvline(upper_percentile, color='red', linestyle='--', label='Percentil 97.5')
        plt.xlabel('Probabilidad de fractura')
        plt.ylabel('Densidad')
        plt.title('Distribución a posteriori')
        plt.legend()
        st.pyplot(plt)

        return mean_probabilidad_fractura, lower_percentile, upper_percentile

    return prior

# Streamlit Interface
st.title('Simulación de Probabilidad de Fractura')
st.sidebar.markdown("Esta aplicación permite simular la probabilidad de fractura de un rasgo bajo distintas condiciones iniciales.")
st.sidebar.markdown("Puede configurar el número de simulaciones, réplicas, probabilidad mínima y máxima, y el número de tiros de interés.")
st.sidebar.markdown("Utiliza valores minimos y maximos de la distribucion uniforme para generar los priors.")
st.sidebar.markdown("La distibucion uniforme se utiliza para simular el rango de probabilidades, sobre la que utiliza la distribucion binomial.")
st.sidebar.markdown("Este desarrollo se basa en los resultados obtenidos en los PICT-2015-0411-E1 y PICT 2018- N° 01816.")
st.sidebar.markdown("Haga clic en el botón 'Ejecutar Simulación' para obtener resultados.")

# Ingresar parámetros
cantidad_simulaciones = st.number_input('Número de simulaciones', 1, value=100000)
numero_replicas = st.number_input('Número de réplicas', 1, value=100)
min_prob = st.number_input('Probabilidad mínima', 0.0, 1.0, 0.02)
max_prob = st.number_input('Probabilidad máxima', 0.0, 1.0, 0.44)
tiros_interes = st.number_input('Número de tiros de interés', 1, value=20)

# Botón para ejecutar la simulación
if st.button('Ejecutar Simulación'):
    resultado = simular_probabilidad_fractura(cantidad_simulaciones, numero_replicas, min_prob, max_prob, tiros_interes)
    st.write(f'Media de la probabilidad de fractura en {tiros_interes} tiros: {resultado[0]:.3f}')
    st.write(f'Intervalo de confianza del 95%: [{resultado[1]:.3f}, {resultado[2]:.3f}]')
