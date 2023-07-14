# Nicolas Uribe and Jamie Pham
# CAP 4630
# Dr. Marques
# 6/25/23


import random
import math
import matplotlib.pyplot as plt

# How many cities in a route
CHROMOSOME_LENGTH = int(input('Enter a number (25 to 50) for cities per route: '))
# How many routes in a generation
POPULATION_SIZE = int(input('Enter a number (50 to 100) for routes per generation: '))
GENERATIONS = int(input('Enter a number (250 to 400) for number of generation: '))
MUTATION_RATE = 0.02


def calculate_distance(city_a, city_b):  # Calculate the distance between each coordinate
    x_diff = city_b[0] - city_a[0]
    y_diff = city_b[1] - city_a[1]
    distance = math.sqrt(x_diff ** 2 + y_diff ** 2)  # Pythagorean theorem
    return distance


def calculate_fitness(chromosome):
    distance = 0
    for i in range(len(chromosome)):
        city_a = chromosome[i]
        city_b = chromosome[(i + 1) % len(chromosome)]  # wraps around to the start when at the end
        distance += calculate_distance(city_a, city_b)
    fitness_score = 1 / distance  # finding the inverse to get the best route
    return fitness_score


def tournament_selection(population, t_size):  # selection of the two parents through tournament selection
    tournament_winners = []
    while len(tournament_winners) < 2:
        tournament_participants = random.sample(population, t_size)
        fittest_parent = max(tournament_participants, key=calculate_fitness)
        tournament_winners.append(fittest_parent)
    return tournament_winners


def order_crossover(parents):
    parent1 = parents[0]
    parent2 = parents[1]
    offspring = [-1] * CHROMOSOME_LENGTH

    # Choose random slice indices
    slice_start = random.randint(0, CHROMOSOME_LENGTH - 1)
    slice_end = random.randint(slice_start, CHROMOSOME_LENGTH - 1)

    # Copy slice from parent1 to offspring
    offspring[slice_start:slice_end + 1] = parent1[slice_start:slice_end + 1]

    # Fill in remaining positions with genes from parent2
    parent2_index = 0
    for i in range(CHROMOSOME_LENGTH):
        if offspring[i] == -1:
            while parent2[parent2_index] in offspring:
                parent2_index = (parent2_index + 1) % CHROMOSOME_LENGTH
            offspring[i] = parent2[parent2_index]
            parent2_index = (parent2_index + 1) % CHROMOSOME_LENGTH

    return offspring


def mutate(chromosome, mutation_rate):  # mutation of offspring to create diversity
    for i in range(len(chromosome)):
        if random.random() < mutation_rate:
            index_swap = random.randint(0, len(chromosome) - 1)
            chromosome[i], chromosome[index_swap] = chromosome[index_swap], chromosome[i]
    return chromosome


def generate_cities(num_cities):  # 25 coordinates of the city is generated
    city_list = []
    for _ in range(num_cities):
        city_list.append((random.randrange(-200, 200), random.randrange(-200, 200)))
    return city_list


def initial_generation(initial_city_list):  # first random generation from initial city
    generation = []
    for _ in range(POPULATION_SIZE):
        generation.append(random.sample(initial_city_list, len(initial_city_list)))
    return generation


def plot_graph(route):  # plot traveling salesman route
    x_coords, y_coords = zip(*route)
    plt.plot(x_coords, y_coords, marker='o')
    plt.plot([x_coords[-1], x_coords[0]], [y_coords[-1], y_coords[0]], linestyle='-', color='blue')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Best Route')
    plt.show()


if __name__ == "__main__":
    city_list = generate_cities(CHROMOSOME_LENGTH)
    population = initial_generation(city_list)
    print('Cities in route: ', CHROMOSOME_LENGTH)
    print('Population Size: ', POPULATION_SIZE)
    print('Generation Size: ', GENERATIONS)
    print('Mutation Rate: ', MUTATION_RATE)

    best_distances = []  # List to store the distance of the best route in each generation

    for generation in range(GENERATIONS):
        # Evaluate fitness
        fitness_scores = [calculate_fitness(chromosome) for chromosome in population]

        # Select parents
        parents = [tournament_selection(population, t_size=5) for _ in range(POPULATION_SIZE // 2)]

        # Create offspring through crossover
        offspring = [order_crossover(parent_pair) for parent_pair in parents]

        # Apply mutation
        offspring = [mutate(chromosome, MUTATION_RATE) for chromosome in offspring]

        # Replace population with offspring
        population = offspring

        # Find the best route in the current generation
        best_route = max(population, key=calculate_fitness)

        # Calculate and store the distance of the best route
        best_distance = sum(calculate_distance(best_route[i], best_route[(i + 1) % len(best_route)]) for i in range(len(best_route)))
        best_distances.append(best_distance)

        # Print the best fitness score and distance in each generation
        best_fitness = calculate_fitness(best_route)
        print(f"Generation {generation + 1}: Best Fitness = {best_fitness}, Distance = {best_distance}")

    # Plot the best route found
    plot_graph(best_route)
