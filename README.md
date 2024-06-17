# Particle Automata

## Overview

This project is a simulation of particle interactions using Pygame. Particles of different types (A, B, and C) are created and their interactions are determined by attraction rules defined in the settings. The simulation visualizes these particles moving within a defined space.

## Requirements

- Python 3.10 or higher
- Poetry for dependency management

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/guilherme-kenzo/particle-automata.git
    cd particle-automata
    ```

2. **Install dependencies using Poetry:**

    ```sh
    poetry install
    ```

## Usage

To start the simulation, run the following command:

```sh
python main.py
```

## Code Structure

### Particle Class

The `Particle` class defines a particle with properties such as position, type, color, and a unique ID. It includes methods for moving the particle and drawing it on the screen.

### Particle Subclasses

- **A**: A type of particle with a white color.
- **B**: A type of particle with a red color.
- **C**: A type of particle with a green color.

### GameMatrix Class

The `GameMatrix` class manages the grid in which particles exist. It handles adding, removing, and updating particles' positions, as well as computing their attractions based on defined rules.

### Main Game Functions

- `bulk_create_random_particles`: Creates a specified number of particles of a given type at random positions.
- `start_game`: Initializes Pygame, sets up the display, creates particles, and runs the game loop. The game loop handles events, updates game logic, and renders the game.


## Notes

- Modify the `settings.py` file to adjust the window size and attraction rules if needed.
- The unique ID generation for particles uses a simple method; for more robust applications, consider a more sophisticated approach.

## License

This project is licensed under the MIT License. See the LICENSE file for details.