# Team Members: Nicolas Uribe, Jamie Pham
# Date: 7/8/2023
# CAP 4630
# Assignment: Project 3

import numpy as np

class AntColonyOptimization:
    '''Initialize algorithm with necessary variables'''
    def __init__(self, n_attractions, n_ants, n_iterations, decay_factor, alpha, beta, exploitation):
        self.n_attractions = n_attractions
        self.n_ants = n_ants
        self.n_iterations = n_iterations
        self.decay_factor = decay_factor
        self.alpha = alpha
        self.beta = beta
        self.exploitation = exploitation              # value determines probability of exploitation
        self.distances = self.matrix_generator()
        self.pheromone = np.ones((self.n_attractions, self.n_attractions))

    def main(self):
        '''Main method that executes the core functions of the
        Ant algorithm i.e pheromone update and best path tracking'''
        best_path = None
        best_length = float('inf')

        for _ in range(self.n_iterations):
            paths = self.construct_solutions()
            self.update_pheromone_trails(paths)

            current_best_path = min(paths, key=lambda x: self.get_distance_traveled(x))
            current_best_length = self.get_distance_traveled(current_best_path)

            if current_best_length < best_length:       # changes best path as it iterates through
                best_path = current_best_path
                best_length = current_best_length

            self.pheromone *= self.decay_factor

        return best_path, best_length

    def matrix_generator(self):
        '''Generates a random attraction matrix'''
        distances = np.random.randint(1, 100, size=(self.n_attractions, self.n_attractions))
        np.fill_diagonal(distances, 0)  # marks the starting point
        return distances

    def construct_solutions(self):
        '''Generates solution paths by iteratively choosing the next attraction for each ant
        based on the ant's current city, pheromone levels, and heuristic information'''
        paths = []

        for _ in range(self.n_ants):        # keeps track of visited attractions
            path = []
            visited = np.zeros(self.n_attractions, dtype=bool)
            current_attraction = np.random.randint(self.n_attractions)
            path.append(current_attraction)
            visited[current_attraction] = True

            for _ in range(self.n_attractions - 1):     # chooses next attraction
                next_attraction = self.visit_attraction(current_attraction, visited)
                path.append(next_attraction)
                visited[next_attraction] = True
                current_attraction = next_attraction

            paths.append(path)

        return paths

    def visit_attraction(self, current_attraction, visited):
        '''Selecting next attraction for ant to visit'''
        unvisited_attractions = np.where(~visited)[0]

        if np.random.rand() < self.exploitation:
            pheromone_values = self.pheromone[current_attraction, unvisited_attractions]
            max_index = np.argmax(pheromone_values)
            return unvisited_attractions[max_index]

        heuristic_values = 1.0 / self.distances[current_attraction, unvisited_attractions]
        probabilities = self.pheromone[current_attraction, unvisited_attractions] ** self.alpha * heuristic_values ** self.beta
        probabilities /= np.sum(probabilities)

        return np.random.choice(unvisited_attractions, p=probabilities)

    def update_pheromone_trails(self, paths):
        '''Trails are updated by ants that find better solutions'''
        for path in paths:
            path_length = self.get_distance_traveled(path)
            delta_pheromone = 1.0 / path_length
            for i in range(len(path) - 1):
                attractionOne, attractionTwo = path[i], path[i + 1]
                self.pheromone[attractionOne, attractionTwo] += delta_pheromone
                self.pheromone[attractionTwo, attractionOne] += delta_pheromone

    def get_distance_traveled(self, path):
        '''Getting distance an ant has traveled'''
        length = 0
        for i in range(len(path) - 1):
            attractionOne, attractionTwo = path[i], path[i + 1]
            length += self.distances[attractionOne, attractionTwo]
        return length


if __name__ == '__main__':
    n_attractions = int(input('Enter number of attractions to visit (5-100): '))
    n_ants = int(input('Enter number of ants in colony(10-500): '))
    n_iterations = 100
    decay_factor = 0.5
    alpha = 1.0
    beta = 2.0
    exploitation = 0.7

    aco = AntColonyOptimization(n_attractions, n_ants, n_iterations, decay_factor, alpha, beta, exploitation)
    best_path, best_length = aco.main()

    print("Best path:", best_path)
    print("Best length:", best_length)
