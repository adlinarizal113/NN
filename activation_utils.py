import numpy as np
import matplotlib.pyplot as plt
import streamlit as st


def relu(x):
    return np.maximum(0.0, x)


def sigmoid(x):
    return np.where(x >= 0, 1 / (1 + np.exp(-np.clip(x, -700, 700))), np.exp(np.clip(x, -700, 700)) / (1 + np.exp(np.clip(x, -700, 700))))


def tanh(x):
    return np.tanh(x)


def show_app(name, function, formula, description):
    st.set_page_config(page_title=f'{name} Activation', layout='centered')
    st.title(f'{name} Activation Function')
    st.write(description)
    st.latex(formula)
    x_min, x_max = st.slider('Graph x-axis range', -15.0, 15.0, (-6.0, 6.0), step=0.5)
    if x_min >= x_max:
        st.error('Minimum must be smaller than maximum.')
        st.stop()
    value = st.slider('Choose an input x', float(x_min), float(x_max), 0.0, step=0.1)
    x = np.linspace(x_min, x_max, 500)
    y = function(x)
    result = float(function(np.array([value]))[0])
    fig, ax = plt.subplots(figsize=(8, 4.5))
    ax.plot(x, y, label=name, linewidth=2)
    ax.scatter([value], [result], color='darkorange', s=65, zorder=5, label='Selected input')
    ax.axhline(0, color='gray', linewidth=0.7)
    ax.axvline(0, color='gray', linewidth=0.7)
    ax.set(xlabel='Input (x)', ylabel='Output f(x)', title=f'{name} function')
    ax.grid(alpha=0.25)
    ax.legend()
    st.pyplot(fig)
    plt.close(fig)
    st.metric('Calculated output', f'{result:.4f}')
    st.write(f'For x = {value:.1f}, {name}(x) = {result:.4f}.')
    st.caption('BSD3513 Chapter 4')
