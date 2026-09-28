import pygame, random, sys, copy

# ----------------------------
# Forest initialization
# ----------------------------

def create_forest(config):
    """Create a forest grid initially containing no trees."""
    # Define the 4 forest states
    no_tree, tree, burning_tree, fire_break = range(4)

    # TODO: Part 1

    return []

def read_forest(config, filename):
    """Read a forest from a text file and update the grid dimensions."""
    # Define the 4 forest states
    no_tree, tree, burning_tree, fire_break = range(4)

    # TODO: Part 2

    return []

# ----------------------------
# Simulation
# ----------------------------

def simulate(forest, config):
    """
    Update the forest according to the following rules:

    1. An empty cell grows a tree with probability `spawn_prob`
    2. A tree burns if at least one neighbour is burning.
    3. A burning cell becomes empty.
    4. Fire breaks cannot burn or spawn trees
    """
    # Define the 4 forest states
    no_tree, tree, burning_tree, fire_break = range(4)

    # Make a new forest so that all cells are updated simultaneously.
    new_forest = create_forest(config)

    # TODO: Part 1 and 3

    return new_forest


def check_neighbours(row, col, forest, config):
    """
    This function should return True if any of the 8 neighbouring cells
    for a tree at position (row, col) is burning.
    """
    # Define the 4 forest states
    no_tree, tree, burning_tree, fire_break = range(4)

    # TODO: Part 2

    return False

# ----------------------------
# Fire start and end
# ----------------------------

def start_fire(forest, config):
    """
    This function should set some trees on fire, so the forest fire simulation
    can actually start. Which trees are ignited at the start can be configured
    in the `fire_start` list.
    """
    # Define the 4 forest states
    no_tree, tree, burning_tree, fire_break = range(4)

    # TODO: Part 3 and 4

    return forest

def check_forest(forest, config):
    """
    This function counts how many trees are left in the forest, to check if
    the majority of the forest has burned in the fire. The majority percentage
    can be configured using the `burn_ratio`.
    """
    # Define the 4 forest states
    no_tree, tree, burning_tree, fire_break = range(4)

    # TODO: Part 4

    return False

# ----------------------------
# Drawing
# ----------------------------

def start_screen(config):
    """Initialize the Pygame screen."""
    # Calculate the screen size
    window_width = config['grid_width'] * config['cell_size']
    window_height = config['grid_height'] * config['cell_size']

    # Set up the Pygame window
    pygame.init()
    screen = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Forest Fire Simulation")

    return screen


def draw(screen, forest, config):
    """Draw the current forest state to the Pygame window."""
    # Define the 4 forest states
    no_tree, tree, burning_tree, fire_break = range(4)

    # Define the RGB colors for each of the 4 states
    colors = {
        no_tree: (0, 0, 0),
        tree: (0, 255, 0),
        burning_tree: (255, 0, 0),
        fire_break: (0, 0, 255),
    }

    # Start with an empty screen
    screen.fill((255, 255, 255))

    # Draw a rectangle for each cell in the grids
    for row in range(config['grid_height']):
        for col in range(config['grid_width']):

            state = forest[row][col]
            color = colors[state]

            x_start = col * config['cell_size']
            y_start = row * config['cell_size']
            size = config['cell_size']

            pygame.draw.rect(screen, color, (x_start, y_start, size, size))

    pygame.display.flip()

# ----------------------------
# Simulations
# ----------------------------

def run_simulation(screen, forest, config):
    """
    Function containing the main simulation loop. It alternates between
    updating the simulation and drawing the result on screen at a fixed
    FPS rate.
    """
    clock = pygame.time.Clock()

    for iteration in range(config['max_iterations']):

        # Handle window events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("The simulation was stopped early.")
                return False

        # Start fire
        if iteration == config['growth_period']:
            forest = start_fire(forest, config)

        # Update simulation
        forest = simulate(forest, config)

        # Redraw the forest
        draw(screen, forest, config)

        # Control simulation speed
        if iteration < config['growth_period']:
            clock.tick(config['growth_fps'])

        else:
            clock.tick(config['burn_fps'])

            # Check burned forest status
            if check_forest(forest, config):
                print(f"More than {int(100*config['burn_thres'])}% of the forest burned!")
                return True

    print("The forest surived the fire!")
    return False


def test_neighbours(screen, forest, config):
    """
    A separate simulation specifically to test the function check_neighbour().
    It loops over all the point in the `neighbour_test_list` and prints the
    results of check_neighbour() on the screen for each point. The forest being
    tested is shown as a static image on the screen.
    """
    clock = pygame.time.Clock()

    for x, y in config['neighbour_test_list']:
        print(f"The cell at position ({x}, {y}) has", end=" ")

        if check_neighbours(y, x, forest, config):
            print("at least one burning neighbour!")
        else:
            print("no burning neighbours at all!")


    for iteration in range(config['max_iterations']):

        # Handle window events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Draw the forest
        draw(screen, forest, config)

        # Control simulation speed
        clock.tick(config['growth_fps'])


def simulation_no_draw(forest, config):
    """Runs the simulation without rendering the result on screen."""
    for iteration in range(config['max_iterations']):
        # Start fire
        if iteration == config['growth_period']:
            forest = start_fire(forest, config)

        # Update simulation
        forest = simulate(forest, config)

        # Check burn status
        if iteration > config['growth_period'] and check_forest(forest, config):
            return True

    return False


def repeated_simulation(forest, config):
    """Runs repeated simulations and counts how many times fire a forest mostly burned."""
    reps = config['simulate_repeated_runs']
    count = 0
    for rep in range(reps):
        # Make a full copy of the starting forest, so the original does not get modified
        new_forest = copy.deepcopy(forest)

        # Count the cases where the forest mostly burned
        if simulation_no_draw(new_forest, config):
            count += 1

    print(f"Out of {reps} repeated experiments, in {count} cases most of the forest burned,",
          f"which was {int(count / reps * 100)}% of cases")

# ----------------------------
# Main program
# ----------------------------

def main(config):
    """Main function starting different versions of the simulation."""
    print()

    # If a filename was supplied, read that forest from file
    if len(sys.argv) == 2:
        forest = read_forest(config, sys.argv[1])

    # Otherwise, create an empty forest
    else:
        forest = create_forest(config)


    # If testing neighbours for some cells, rescale the cells and start test
    if len(config['neighbour_test_list']) > 0:
        config['cell_size'] = 100

        screen = start_screen(config)
        test_neighbours(screen, forest, config)

    # If computing average over multiple runs, don't start the screen
    elif config['simulate_repeated_runs'] > 0:
        repeated_simulation(forest, config)

    # Otherwise, run the main simulation loop
    else:
        screen = start_screen(config)
        run_simulation(screen, forest, config)


    pygame.quit()


if __name__ == "__main__":
    config = {
        'grid_width': 50,
        'grid_height': 40,
        'cell_size': 15,

        'growth_fps': 10,
        'burn_fps': 10,

        'growth_period': 50,
        'spawn_prob': 0.02,
        'max_iterations': 150,

        'fire_start': [(24,0), (25,0), (26,0)],
        'burn_thres': 0.8,

        'neighbour_test_list': [],
        'simulate_repeated_runs': 0,
    }

    main(config)
