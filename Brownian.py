import streamlit as st
import numpy as np
import plotly.express as px

# Function to simulate Brownian motion with one observation per year
def simulate_brownian_motion(sim_number, time, initial_value, min_value, max_value, seed):
    # Reduce resolution to one observation per year
    steps_per_time = 1
    steps = int(time * steps_per_time)
    
    # Initialize seed for reproducibility
    np.random.seed(seed)
    
    realizations = np.empty((sim_number, steps))
    
    for i in range(sim_number):
        delta = np.random.normal(loc=0, scale=np.sqrt(1 / steps_per_time), size=steps)
        change = np.cumsum(delta)
        actual_value = initial_value + change
        actual_value = np.minimum(max_value, np.maximum(min_value, actual_value))
        realizations[i, :] = actual_value
    
    mean_simul = np.mean(realizations, axis=0)
    return realizations, mean_simul

# Streamlit Interface
st.title('Brownian Motion Simulation per unit of time')

sim_number = st.number_input('Number of simulations:', value=1000, min_value=1)
initial_value = st.number_input('Initial value:', value=5.0, min_value=0.2)
min_value = st.number_input('Minimum value:', value=0.2, min_value=0.0)
max_value = st.number_input('Maximum value:', value=23.0, min_value=0.0)
time = st.number_input('Simulation duration (years):', value=1000, min_value=1)
seed = st.number_input('Seed:', value=1973)

if st.button('Run Simulation'):
    realizations, mean_simul = simulate_brownian_motion(sim_number, time, initial_value, min_value, max_value, seed)
    
    # Create a Plotly chart
    Time = np.arange(1, time + 1)  # Create a time vector for years
    fig = px.line(x=Time, y=mean_simul, title='Brownian Motion Simulations', labels={'x': 'Time', 'y': 'Mean Value'})
    
    st.plotly_chart(fig)