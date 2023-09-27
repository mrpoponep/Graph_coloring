# Graph Coloring Algorithms

This project implements graph coloring algorithms, including Greedy, Independent Set, DSATUR, and Welsh-Powell, using the NumPy library for efficient data manipulation and the Timeit library for measuring execution times.

## Table of Contents

- [Introduction](#introduction)
- [Usage](#usage)
- [Algorithms](#algorithms)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Graph coloring is an essential problem in graph theory, where the goal is to assign colors to the vertices of a graph such that no adjacent vertices share the same color. This project provides implementations of various graph coloring algorithms to find optimal or near-optimal coloring solutions.

## Usage

To use this project, follow these steps:

1. Clone the repository to your local machine

2. Navigate to the project directory

3. Install the required dependencies using pip

4. Run the desired graph coloring algorithm by executing the corresponding Python script. 

5. The program will display the coloring results and execution time.

## Input and output
The input consists of a .txt file containing the number of vertices on the first line, followed by the list of edges on subsequent lines.

The output is a list of colors assigned to each vertex, starting from the first vertex and ending with the last.

See example of input and output in Dataset file

## Algorithms

### Greedy Algorithm

The Greedy algorithm assigns colors to vertices one by one in the order they appear, selecting the smallest available color for each vertex.

### Independent Set Algorithm

The Independent Set algorithm identifies independent sets of vertices (i.e., vertices that have no edges connecting them) and colors these sets independently.

### DSATUR Algorithm

DSATUR is a more sophisticated algorithm that selects vertices with the highest degree of saturation, ensuring that it colors as many adjacent vertices as possible.

### Welsh-Powell Algorithm

The Welsh-Powell algorithm orders the vertices in descending order of degrees and colors them one by one, ensuring that no adjacent vertices share the same color.

## Dependencies

- NumPy: Used for efficient data manipulation and storage.
- Timeit: Used for measuring execution times.

## Contributing

Contributions to this project are welcome. If you have any suggestions, bug fixes, or want to add more features or algorithms, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
