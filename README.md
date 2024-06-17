# Particle Automaton README

## Overview

This project is a simulation of particle interactions using Pygame. Particles of different types (A, B, and C) are created and their interactions are determined by attraction rules defined in the settings. The simulation visualizes these particles moving within a defined space.

## Requirements

- Python 3.10 or higher
- Poetry for dependency management

## Installation

1. **Clone the repository:**

    ```sh
    git clone <repository_url>
    cd <repository_directory>
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

### Main Script

The `main.py` script initializes and starts the game by calling the `start_game` function.

## Detailed Explanation of Key Components

### Particle Class

```python
class Particle:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.type = None
        self.color = None
        self._id = None
        self._has_changed_this_loop = False
        self._acc_forces = []

    @property
    def id(self):
        if self._id:
            return self._id
        while self._id is None:
            _id = np.random.randint(0, 100000)
            if _id not in ids:
                ids.append(_id)
                self._id = _id
                return self._id

    def move(self, x: int = None, y: int = None):
        if x is None and y is None:
            raise ValueError("You must provide x or y to move the particle")
        if x:
            self.x = x
        if y:
            self.y = y
        self.rect = pygame.Rect(self.x, self.y, 1, 1)

    def draw(self, screen: pygame.Surface):
        pygame.draw.rect(screen, self.color, (self.x, self.y, 1, 1))

    def move_up(self, movement):
        self.move(y=self.y + movement)
    
    def move_down(self, movement):
        self.move(y=movement - self.y)

    def move_left(self, movement):
        self.move(x=self.x - movement)

    def move_right(self, movement):
        self.move(x=self.x + movement)
```
## Notes

- Ensure Pygame and other dependencies are correctly installed.
- Modify the `settings.py` file to adjust the window size and attraction rules if needed.
- The unique ID generation for particles uses a simple method; for more robust applications, consider a more sophisticated approach.

## License

This project is licensed under the MIT License. See the LICENSE file for details.