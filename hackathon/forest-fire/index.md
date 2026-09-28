
# Forest Fire Simulation

For this assignment you'll work on a simple simulation of forests growing and catching fire. The
forest will be represented as a rectangular grid, where each cell will contain a live tree, a
burning tree or an empty space. Empty spaces might grow new trees, and burning trees might cause
neighbouring trees to catch fire. During the simulation you'll update the forest at each timestep
to see the effect of these rules evolve. For the last part you'll investigate the effectiveness
of different types of fire breaks on the survival of the forest.

## Part 0: Getting started

First, download the starting file [here](forest_fire.py). Next, install the *Pygame* library in
your `(minai)` environment by running the following command in your terminal:

    pip install pygame

We will be using *Pygame* to visualize the forest on screen during the simulation. The *Pygame*
code is already given in the starting file, but it is good to have a basic idea of what this part
of the code approximately does.

### Main variables

For this assignment the `forest` will be represented as a list of lists, where each inner list is
one row of the forest. Each element in the inner lists will have a number representing the state
of that cell:

* **0** - *Empty cell*
* **1** - *Living tree*
* **2** - *Burning tree*
* **3** - *Fire break*

So, a simple *3x3* `forest` with only healthy trees would look like:

    [[1, 1, 1],
     [1, 1, 1]
     [1, 1, 1]]

The other main important variables are  `config` and `screen`. Respectively, these are the dictionary that contains all of the
settings configuring the simulation, and the variable representing the screen
on which the simulation will be shown.

With these variables explained, we can take a look at the two most important *Pygame* functions
already provided in the code:

### `draw(screen, forest, config)`

This takes the current forest and draws it on the screen. Each cell in the forest grid is drawn
as a rectangle, where trees become green, empty squares become black, and burning trees become
red. The color is encoded as an 8-bit RGB value, meaning the first value is the amount of *Red*,
the second is the amount of *Green*, and the third is the amount of *Blue*. For more explanation
and examples, see the link [here](https://www.rapidtables.com/web/color/RGB_Color.html).

By drawing each cell as a separate rectangle with its own color and position, eventually the
entire forest will be drawn on the screen.

### `run_simulation(screen, forest, config)`

This loops a total of `max_iterations` number of times to do the following:

1. Check if the *Pygame* window was closed, if so, exit the simulation
2. Update the forest to the next step using the `simulate()` function
3. Draw the new forest to the screen using `draw()` as described above
4. Use the clock to wait a specified time to create a fixed frame rate

The last step is necessary so the simulation runs at a fixed rate and it is possible to observe
each of the different steps. If this wasn't added the different states would flash by as fast as
they could be computed.

Take a look at both these functions and see if you can find the steps described above in the code
for `draw()` and `run_simulation()`. Make sure each of you understands the overall structure of
both functions, before moving on to part 1.

## Part 1: Growing the forest

For this first part we'll only focus on growing the forest and drawing this on the screen. This
should be enough to be able to start the simulation and observe the first results

### `create_forest(config)`

This function should initialize an empty forest (i.e. a forest containing only empty cells). The
argument `config` is the main configuration dictionary, which contains all the settings for the
simulation. For this function, the only relevant settings are `grid_height` and `grid_width`,
which define the size of the forest grid to be created. You can change these settings in the
`config` dictionary definition at the very end of the file, before the call to the main function.

This function should return a list of lists, where the inner lists are each `grid_width` long,
and the outer list contains `grid_height` lists. All cells in that grid should have the value
for the empty cell, which is stored in the variable `no_tree` at the start of the function
(all 4 state variables are defined at the start of each function).

### `simulate(forest, config)`

Next you'll write part of the simulate function to start growing the trees. For this you'll need
the same `grid_height` and `grid_width` from the `config` dictionary, along with `spawn_prob`.
This is the probability that any empty cell will randomly grow a new tree. Your code should loop
over all the cells in the grid, and change the empty cells to become trees with probability
`spawn_prob`, otherwise they remain empty. Cells that already contain trees should remain the
same.

***Note:*** At the start of the function a variable `new_forest` is made, that will always start
completely empty. You should use this variable to store the updated forest, and **not** the
original `forest`. The reason for this will be become clearer after part 3, where you'll
expand on this simulate function further. For now, just make sure to add any existing or newly
spawned trees into this `new_forest`, which is returned at the end of the function.

### Run simulation and experiment

Run the simulation and observe the results. Does everything work as expected and without errors?
Try changing the `grid_height`, `grid_width`, and `spawn_prob` in the config dictionary. Do you
observe the expected changes?

## Part 2: Checking neighbours

One of the most important parts of the simulation will be based on checking the surrounding cells
for a tree. If any of the 8 surrounding cells is a `burning_tree`, then that tree should also start
burning. As this is one of the main functions of the simulation, we'll write and test it
separately in this part, before adding it to the main simulation.

### `check_neighbours(row, col, forest, config)`

This function should check all 8 possible neighbours for a specific position `(row, col)` in the
`forest` grid. If any of the 8 neighbours are a `burning_tree`, the function should return *True*,
but if none of the neighbours are burning, the function should return *False*.

*Hints:* Try to use 2 loops to compute all 9 possible locations in a *3x3* box, where the position
`(row, col)` in the middle if that box. Not every position on the grid will have 8 possible
neighbours, so also make sure to check that neighbour position is actually a valid grid position
using the `config` dictionary.

### `read_forest(config, filename)`

Next, write a function to read a forest from a simple text file. Here each row of the forest will be on a new line, and each cell will be separated by a space. So a text file that looks
like

    0 1 0
    2 1 1
    2 0 1

should be read into a forest list as

    [[0, 1, 0],
     [2, 1, 1],
     [2, 0, 1]]

The function should return this new forest list that was read from the file `filename`. It should
also update the `grid_height` and `grid_width` in the `config` dictionary to match the dimensions
of the forest that was just read from the file.

### Testing your neighbour function

To test the `check_neighbours()` function, we'll be using a simple test forest like
[test\_neighbour.txt](test_neighbour.txt). You can load this forest using the `read_forest()`
function, which will give you a simple example you can test with and modify.

In the `config` dictionary defined at the end of the program, modify the setting for
`neighbour_test_list`. If you change this from an empty list to a list of points like

    [(1, 0), (0, 1), (1, 1), (2, 0), (0, 2)]

This will be the list of coordinates on which to test your `check_neighbours()` function. Then,
to load a forest from a file, you can use an additional command line argument when starting your
program, like

    python forest_fire.py test_neighbour.txt

If you use this modified command and also change the `neighbour_test_list`, you should get the
results from testing your `check_neighbours()` function. Modify the forest inside the text file
and the list of points in test list until all of you are sure the function works correctly.

## Part 3: Simulating a fire

For the next part we'll be adding this `check_neighbours()` function to the simulation, and using
it to make sure that if a neighbour tree is burning, that tree will also catch fire.

### `simulate(forest, config)`

Currently this function only adds new trees to empty cells with probability `spawn_prob`, and
cells that contained trees remained trees at the next step. Complete this function by adding the
following rules:

* If any neighbour of a tree is burning, that tree becomes a burning tree at the next step
* If any tree is currently burning, then it becomes empty at the next step (it is burned out)
* Fire breaks will always remain fire breaks at the next step (i.e. cannot catch fire)

*Note:* This first rule is exactly why it is important to use the `new_forest` and for next step
and not update the existing `forest`. When you update you'd also change what neighbours would be
on fire for the next cell to check, causing bugs in your simulation.

### `start_fire(forest, config)`

Next we'll add some fire to our forest fire simulation, as we'll need a fire to start somewhere
in the forest before it can spread. The `fire_start` setting in the `config` dictionary contains
a list of points where the fire should start. Currently it contains

    [(24, 0), (25, 0), (26, 0)]

which means that there are 3 coordinates at the center top of the screen where the fire should
start. Complete the function by looping over all of the pairs of points in `fire_start` and changing
all these points in the grid to be `burning_tree`s instead.

### Some people just want to watch the forest burn

Now we can run our first real forest fire experiments. Start by making sure the
`neighbour_test_list` is set to an empty list `[]` again, so the regular simulation is run instead
of the neighbour test from the previous part. If you now start the simulation, you should observe
two separate phases:

1. First the trees are growing to fill in the empty spaces, which will be the same as in part 1.
2. Then a fire should start on the top edge of the screen, which will spread to neighbouring trees

There are several settings from the `config` dictionary you should tweak for this simulation

* `spawn_prob`: The probability of a new tree growing in an empty space
* `growth_period`: The number of iterations the trees grow before the fire starts
* `max_iterations`: The total number of iterations to simulate, including growth and fire phases

You should try and modify these parameters until you get a combination that looks like most of
the forest burns about 70% of the simulations you run. There is one additional setting you might
want to change, which is `growth_fps`. If you increase this number, the growth phase will simulate
faster. This means you can have much longer growth period, without having to wait each time before
the fire starts. Once you have a combination of settings all of you are happy with and which feels like
a somewhat realistic simulation, you can move on to the next step.

### Part 4: Scaling the simulation

For this final step, you'll add a check to see if most of the forest burned during the simulation
and then run repeated simulations to test the effect of different types of fire breaks on the
survival of the forest.

### `check_forest(forest, config)`

This function should loop over the entire grid, and count how many healthy trees there currently
are. This can then be used to compute what part of the forest is currently burned. The ratio of
burned trees can be computed as

    1 - (tree_count / total_grid_size)

If this ratio is above the `burn_thres` set in the `config` dictionary, the function should return
*True*, and otherwise it should return *False*.

### `start_fire(forest, config)`

Modify the function `start_fire` to start at a random point on the grid, if the list `fire_start`
in the `config` dictionary is empty. The function should select a random point on the grid, and
set any trees in a *2x2* square starting at that point on fire. If the list `fire_start` is not
an empty list, the function should work as before and start the fire at those points.

### Fire break design

You can now test your code by running the simulation. When more than 80% of the trees have burned
the simulation will now automatically stop and print a message informing you of the result. You
can modify `burn_ratio` in the `config` dictionary to change this percentage. If you change the
`fire_start` to an empty list `[]`, the start of the fire should now change randomly each
simulation.

For the last part of this project, you can experiment with adding different fire breaks. Fire
breaks are parts of the forest that are intentionally cleared to prevent forest fires spreading
beyond that point. In the simulation they will show up as blue squares that cannot grow any trees
and cannot catch fire at all. To add fire breaks you'll need to load a starting forest that
already has the fire breaks added. You can download an example [here](fire_breaks.txt) and you
can test this example by running

    python forest_fire.py fire_breaks.txt

Finally, to make your experimentation a little easier, we've also provided a function that will
run repeated simulations without actually showing them on the screen. This function will just
count in how many of the cases most of the forest burned down and print the final result in the
terminal. This way you can easily do 10 or 100 simulations, without having to watch them all
progress and count when enough of the forest survived.

To use this feature, modify the `simulate_repeated_runs` setting in the `config` dictionary to
the number of runs you want to do. First, start by verifying that in the regular simulation (so
without adding any fire breaks) the forest does indeed burn most of the way in about 70% of runs.
If not, try to tweak the settings you found in part 3 to get closer to this number.

Now, you can experiment with adding fire breaks of different designs, and seeing the impact on the
survival percentage. You can create your own starting forest with fire breaks in different patterns;
the number 2 is the state you can use to add fire breaks in a file. Try to find the best fire break
design!
