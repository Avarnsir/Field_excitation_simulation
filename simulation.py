import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# -----------------------------
# Parameters
# -----------------------------
nx, ny = 100, 100     # grid size
dx = 1.0              # spatial step
dt = 0.1              # time step
c = 1.0               # wave speed

# -----------------------------
# Create spatial grid
# -----------------------------
x = np.linspace(-5, 5, nx)
y = np.linspace(-5, 5, ny)
X, Y = np.meshgrid(x, y)

# -----------------------------
# Initial Gaussian excitation
# -----------------------------
sigma = 0.5
u = np.exp(-(X**2 + Y**2) / (2 * sigma**2))
u_prev = np.copy(u)

# -----------------------------
# Setup figure
# -----------------------------
fig, ax = plt.subplots()
im = ax.imshow(u, extent=[-5,5,-5,5], animated=True)
ax.set_title("Field Excitation Propagation")
ax.set_xlabel("Space")
ax.set_ylabel("Space")

# -----------------------------
# Update function (Wave equation)
# -----------------------------
def update(frame):
    global u, u_prev

    u_next = (2*u - u_prev +
              (c**2 * dt**2 / dx**2) *
              (np.roll(u,1,axis=0) + np.roll(u,-1,axis=0) +
               np.roll(u,1,axis=1) + np.roll(u,-1,axis=1) - 4*u))

    u_prev = u
    u = u_next

    im.set_array(u)
    return [im]

# -----------------------------
# Animate
# -----------------------------
ani = animation.FuncAnimation(fig, update, frames=120, interval=50)

# -----------------------------
# Save as GIF
# -----------------------------
ani.save("Field_Excitation_Simulation.gif", writer="pillow")

plt.show()
