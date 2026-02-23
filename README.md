<h1 align="center">Field Excitation Simulation</h1>

<p align="center">
A numerical simulation demonstrating how a localized field excitation propagates in space.
</p>

<hr>

<h2>📌 Project Overview</h2>

<p>
This project simulates the propagation of a localized excitation in a two-dimensional scalar field.
The simulation numerically solves the classical 2D wave equation and visualizes how a disturbance
evolves over time.
</p>

<p>
The purpose of this project is to illustrate a core idea of modern particle physics:
particles can be interpreted as excitations of underlying fields.
</p>

<hr>

<h2>🧠 Physical Background</h2>

<p>
In classical field theory, a field is a quantity defined at every point in space and time.
In quantum field theory, fundamental particles are understood as quantized excitations
of their respective fields.
</p>

<p>
This simulation evolves the scalar field using the 2D wave equation:
</p>

<p align="center">
∂²φ / ∂t² = c² ∇²φ
</p>

<ul>
<li><b>φ(x, y, t)</b> – scalar field</li>
<li><b>∇²φ</b> – spatial Laplacian (curvature of the field)</li>
<li><b>c</b> – propagation speed of disturbances</li>
</ul>

<hr>

<h2>🎯 What This Simulation Demonstrates</h2>

<ul>
<li>The field exists everywhere in space.</li>
<li>A localized Gaussian disturbance represents a particle-like excitation.</li>
<li>The excitation propagates according to the wave equation.</li>
<li>Energy spreads through the field over time.</li>
</ul>

<p>
This provides a classical analogy for the fundamental idea of 
Quantum Field Theory: particles are excitations of fields.
</p>

<hr>

<h2>🛠 Technologies Used</h2>

<ul>
<li>Python</li>
<li>NumPy</li>
<li>Matplotlib</li>
<li>Pillow (for GIF export)</li>
</ul>

<hr>

<h2>▶ How to Run</h2>

<pre>
pip install numpy matplotlib pillow
python simulation.py
</pre>

<p>
The script will generate an animated GIF showing the propagation of the field excitation.
</p>

<hr>

<h2>📊 Output</h2>

<p>
The output is an animated visualization of a localized excitation propagating
across a 2D field grid.
</p>

<hr>

<h2>⚠ Important Note</h2>

<p>
This simulation represents a classical field model.
It does not include quantum quantization effects or particle creation.
It is intended as a conceptual and educational demonstration.
</p>

<hr>

<h2>📚 Academic Context</h2>

<p>
This project was developed as part of a study in particle physics and field theory,
focusing on understanding interactions and fields at a conceptual and computational level.
</p>

<hr>

<h3 align="center">Author</h3>

<p align="center">
MSc Physics Student <br>
Computational Physics | Particle Physics | Field Theory
</p>
