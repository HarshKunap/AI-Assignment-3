# UGV Path Planning using Search Algorithms

## Overview

This project focuses on implementing path planning techniques for an Unmanned Ground Vehicle (UGV) in a grid-based environment. The objective is to compute an optimal path from a user-defined start node to a goal node while avoiding obstacles.

The implementation covers:

1. Dijkstra’s Algorithm (Uniform Cost Search) for weighted graphs
2. A* Search for grid-based navigation with static obstacles

The environment assumes that all obstacles are known a priori and remain fixed throughout execution.

---

## Problem Description

* The environment is modeled as a two-dimensional grid (e.g., 70×70)
* Each cell represents a node in the search space
* Obstacles are placed in the grid based on predefined density levels
* The UGV must navigate from a start position to a goal position
* Movement is restricted to four directions: up, down, left, and right

The goal is to compute the shortest valid path that avoids all obstacles.

---

## Algorithms Implemented

### 1. Dijkstra’s Algorithm (Uniform Cost Search)

Dijkstra’s algorithm is used for computing the shortest path in a weighted graph where edge costs may vary.

**Key characteristics:**

* Uses a priority queue (min-heap)
* Expands the node with the smallest cumulative path cost
* Guarantees optimal shortest paths for non-negative edge weights

**Core principle:**
[
\text{distance}[v] = \min(\text{distance}[v], \text{distance}[u] + w(u, v))
]

---

### 2. A* Search Algorithm

A* is used for efficient pathfinding in the grid environment.

**Key characteristics:**

* Combines actual cost and heuristic estimate
* Uses Manhattan distance as the heuristic
* Reduces unnecessary exploration compared to Dijkstra’s algorithm

**Evaluation function:**
[
f(n) = g(n) + h(n)
]

Where:

* ( g(n) ): cost from start to node ( n )
* ( h(n) ): estimated cost from ( n ) to goal

---

## Grid and Obstacle Model

* The grid is generated programmatically
* Obstacles are assigned using random sampling
* Three density levels are supported:

  * Low density
  * Medium density
  * High density

Cells are represented as:

* `0` → free space
* `1` → obstacle

---

## Path Planning Approach

### Static Environment

1. Generate the grid with obstacles
2. Define start and goal positions
3. Apply A* search to compute the shortest path
4. Reconstruct the path using parent tracking

---

## Performance Metrics

The implementation evaluates performance using the following measures:

* **Path Length**: Number of steps from start to goal
* **Visited Nodes**: Total nodes explored during search
* **Execution Time**: Time required to compute the path
* **Feasibility**: Whether a valid path exists under given obstacle density

---

## Project Structure

```
ugv-path-planning-astar/
│
├── main.py          # Core implementation (Dijkstra and A*)
├── data/            # Optional dataset for graph-based input
├── README.md        # Documentation
```

---

## Execution

Run the program using:

```
python main.py
```

The program will:

* Generate grids with varying obstacle densities
* Execute the pathfinding algorithm
* Output performance metrics for each case

---

## Key Observations

* Dijkstra’s algorithm guarantees optimal paths but explores more nodes
* A* improves efficiency by guiding the search using a heuristic
* Higher obstacle density increases search complexity and may lead to no feasible path

---

## Applications

* Autonomous ground vehicle navigation
* Robotics path planning
* Simulation of constrained environments
* Artificial intelligence search problems

---

## Conclusion

This project demonstrates the application of classical search algorithms for path planning in structured environments. It highlights the transition from cost-based search (Dijkstra) to heuristic-guided search (A*), showing how efficiency can be improved while maintaining optimality.

---
