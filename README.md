# Simple-Gravity-Simulation
**Gravity Sim** is a simple two-planet gravity simulation built with Pygame. In this simulation, planets exert gravitational forces on each other and move according to Newtonian physics.

---

## Features

- Calculates Newton's universal law of gravitation between two planets.  
- Updates planets' positions and velocities based on real physics formulas.  
- Zoom in and out using the mouse wheel.  
- Simple visual representation of gravitational interaction.  

---

## Requirements

- Python 3.x  
- Pygame library  

Install Pygame using:

```
pip install pygame
```

## Installation and Running
1-Download the project files into a folder.
2-Add planet.png image to the project folder (planet icon).
3-Run the simulation with Python:
```python main.py```

## Usage
- Once the simulation starts, the two planets will attract each other due to gravity.
- Scroll the mouse wheel up to zoom in and down to zoom out.
- Close the window by clicking the close button.

## Physics Model
- The force between planets is calculated using Newton's law of universal gravitation:
  $F = G \frac{m_1 m_2}{r^2}$
- The x and y components of the force are used to update the planets' acceleration and velocity.
