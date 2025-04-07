# Binet Formula Visualization

A 4D visualization of the Fibonacci function extended to complex inputs using **Binet Formula**, inspired by the Stand-up Maths [video](https://youtu.be/ghxQA3vvhsk). The interactive plot can be found [here](https://dnshkmr7.github.io/complex-fibonacci/).

This project visualizes:

- **x & y axis** represent real and imaginary parts of a complex number.
- **z axes & colorbar** represent real and imaginary parts of the Fibonacci function evaluated at that complex number.


## Binet Formula (Extended to Complex Inputs)

<div align="center">

$$
F(z) = \frac{\phi^z - \psi^z}{\sqrt{5}}
$$

</div>

<div align="center">

$$
\phi = \frac{1 + \sqrt{5}}{2}, \quad 
\psi = \frac{1 - \sqrt{5}}{2}, \quad 
z = x + iy
$$

</div>


## Scaling

To keep the visualization both smooth and pretty, especially for large oscillating values I apply the **inverse hyperbolic sine function** on the real and imaginary parts of the result.

<div align="center">

$$
\sin^{-1}h(x) = \ln\left(x + \sqrt{x^2 + 1}\right)
$$

</div>

---
