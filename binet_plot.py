# --- Import stuff ---
import numpy as np
import plotly.graph_objects as go

# --- Useful functions ---
def binet(z):
    sqrt5 = np.sqrt(5)
    phi = (1 + sqrt5) / 2
    psi = (1 - sqrt5) / 2
    return (np.power(phi, z) - np.power(psi, z)) / np.sqrt(5)

def generate_ticks(transformed_data, num_ticks=5):
    min_val = np.min(transformed_data)
    max_val = np.max(transformed_data)
    
    tick_positions = np.linspace(min_val, max_val, num_ticks)
    tick_labels = [f"{np.sinh(pos):.1e}" for pos in tick_positions]
    
    return tick_positions, tick_labels

# --- Execute Binet ---
x = np.linspace(-10, 20, 250)
y = np.linspace(-10, 20, 250)
X, Y = np.meshgrid(x, y)
Z_complex = X + 1j * Y

Fz = binet(Z_complex)

Z_real = np.real(Fz)    
Z_imag = np.imag(Fz)  

# --- Scaling to make it look pretty ---
Z_real_transformed = np.arcsinh(Z_real)
Z_imag_transformed = np.arcsinh(Z_imag)

# --- Plotting it all ---
z_tick_positions, z_tick_labels = generate_ticks(Z_real_transformed, num_ticks = 7)
c_tick_positions, c_tick_labels = generate_ticks(Z_imag_transformed, num_ticks = 7)

fig = go.Figure(data = [go.Surface(x = X, y = Y, z = Z_real_transformed,       
                                   surfacecolor = Z_imag_transformed,  
                                   colorscale = 'Turbo',
                                   colorbar = dict(title = "Imag(F(x))",
                                                   tickvals = c_tick_positions,
                                                   ticktext = c_tick_labels,
                                                   tickmode = 'array'),
                                   )])

fig.update_layout(
    title = "Binet Formula (sin^-1h scaled)",
    scene = dict(xaxis_title = 'Real(x)', yaxis_title = 'Imag(x)', zaxis_title = 'Real(F(x))',
                 zaxis = dict(tickvals = z_tick_positions,
                              ticktext = z_tick_labels,
                              tickmode = 'array'),
                 aspectmode = 'cube'),
    autosize = True,
    margin = dict(l = 0, r = 0, b = 0, t = 40)
    )

fig.show()
fig.write_html("binet_plot_arcsinh.html")