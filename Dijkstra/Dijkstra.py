import heapq
from collections import defaultdict

class Graph:
    def __init__(self):
        # adjacency list:
        # graph[u] = [(v, distance), (v2, distance2), ...]
        self.graph = defaultdict(list)

    def add_edge(self, u, v, w, bidirectional=True):
        """
        Add an edge between city u and city v with road distance w.
        If bidirectional=True, roads work both ways.
        """
        self.graph[u].append((v, w))
        if bidirectional:
            self.graph[v].append((u, w))

    def dijkstra(self, start):
        """
        Dijkstra's algorithm:
        Returns:
            distances: shortest distance from start to every city
            previous: predecessor map to reconstruct path
        """
        # Set all distances to infinity initially
        distances = {node: float('inf') for node in self.graph}
        distances[start] = 0

        # predecessor dictionary to reconstruct shortest path
        previous = {node: None for node in self.graph}

        # priority queue: (distance_from_start, city)
        pq = [(0, start)]

        while pq:
            current_distance, current_city = heapq.heappop(pq)

            # If this is an outdated entry, skip it
            if current_distance > distances[current_city]:
                continue

            # Visit all neighbors
            for neighbor, weight in self.graph[current_city]:
                distance_through_current = current_distance + weight

                # Relaxation step
                if distance_through_current < distances[neighbor]:
                    distances[neighbor] = distance_through_current
                    previous[neighbor] = current_city
                    heapq.heappush(pq, (distance_through_current, neighbor))

        return distances, previous

    def shortest_path(self, start, end):
        """
        Find shortest path from start to end using Dijkstra.
        Returns the path and total distance.
        """
        distances, previous = self.dijkstra(start)

        if distances[end] == float('inf'):
            return None, float('inf')

        # Reconstruct path by walking backwards from end
        path = []
        current = end
        while current is not None:
            path.append(current)
            current = previous[current]

        path.reverse()
        return path, distances[end]


# -----------------------------
# Sample road network of Indian cities
# Distances are example road distances in km
# -----------------------------
g = Graph()

g.add_edge("Delhi", "Jaipur", 280)
g.add_edge("Delhi", "Agra", 233)
g.add_edge("Delhi", "Chandigarh", 243)
g.add_edge("Jaipur", "Ahmedabad", 675)
g.add_edge("Jaipur", "Indore", 600)
g.add_edge("Agra", "Kanpur", 293)
g.add_edge("Agra", "Lucknow", 335)
g.add_edge("Chandigarh", "Amritsar", 230)
g.add_edge("Kanpur", "Lucknow", 79)
g.add_edge("Lucknow", "Varanasi", 320)
g.add_edge("Varanasi", "Patna", 250)
g.add_edge("Indore", "Mumbai", 582)
g.add_edge("Ahmedabad", "Mumbai", 525)
g.add_edge("Mumbai", "Pune", 150)
g.add_edge("Pune", "Hyderabad", 560)
g.add_edge("Hyderabad", "Bangalore", 575)
g.add_edge("Bangalore", "Chennai", 345)
g.add_edge("Chennai", "Kolkata", 1660)
g.add_edge("Patna", "Kolkata", 580)

# -----------------------------
# Example usage
# -----------------------------
start_city = "Delhi"
end_city = "Bangalore"

path, distance = g.shortest_path(start_city, end_city)

if path is None:
    print(f"No route found from {start_city} to {end_city}")
else:
    print("Shortest path:")
    print(" -> ".join(path))
    print(f"Total road distance: {distance} km")