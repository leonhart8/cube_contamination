# cube_contamination
Repository containing the solution to a cube contamination problem. The premise is the following : given a cube of given size which represents a 3D grid made up of smaller individual cubes of size 1, simulate the behavior of a virus contamining cubes.

How does the infection work ?

A virus selects a random cube and infects it. Afterwards the infection spreads to neighboring cubes.

Let us illustrate the process in 2D, with 0 representing an uninfected tile and 1 an infected tile.

At the start no tile is infected :

+--------+<br/>
|0 |0 |0 |<br/>
+--------+<br/>
|0 |0 |0 |<br/>
+--------+<br/>
|0 |0 |0 |<br/>
+--------+<br/>

The virus then randomly chooses a tile to infect :

+--------+<br/>
|1 |0 |0 |<br/>
+--------+<br/>
|0 |0 |0 |<br/>
+--------+<br/>
|0 |0 |0 |<br/>
+--------+<br/>


The infection spreads to neighboring tiles until complete infection !

+--------+<br/>
|1 |1 |0 |<br/>
+--------+<br/>
|1 |0 |0 |<br/>
+--------+<br/>
|0 |0 |0 |<br/>
+--------+<br/>

# Required libraries

The project is written in python3, so it requires a python3 installation at the very least.

It also requires for numpy to be installed, in order to do so one can run in command line :

<code>user$ pip3 install numpy</code>

No other install is required.

# Usage

## Running tests

In order to run tests in command line, place yourself at the root of the project and run

<code>user$ python3 -m tests.{test_module_name} </code>

## Running the infection

The main script to execute is <code>infection_main.py</code>. In order to execute it
one needs in command line to run the following command :

<code>user$ python3 infection_main -s [size]</code>

Where <code>[size]</code> is the size of the cube to be infected. Its total number of elements
will be equal to size * size * size.

In order to get more info on the usage of the script run

<code>python3 infection_main -h </code>

# Possible improvements

Find a way to harness vectorization to compute the infection even faster

Implement a GUI which displays the infection
