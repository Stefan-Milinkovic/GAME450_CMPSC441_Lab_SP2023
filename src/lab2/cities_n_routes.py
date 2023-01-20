import itertools
import random

''' 
Lab 2: Cities and Routes

In the final project, you will need a bunch of cities spread across a map. Here you 
will generate a bunch of cities and all possible routes between them.
'''

def get_randomly_spread_cities(size, n_cities):
    """
    > This function takes in the size of the map and the number of cities to be generated 
    and returns a list of cities with their x and y coordinates. The cities are randomly spread
    across the map.
    
    :param size: the size of the map as a tuple of 2 integers
    :param n_cities: The number of cities to generate
    :return: A list of cities with random x and y coordinates, as a tuple of two values.
    [ (23, 34), (3,56), ... ]
    """

    coordinates = []
    for i in range(n_cities):
        x = random.randrange(size[0])
        y = random.randrange(size[1])
        coordinates.append((x, y))

    return coordinates

    # Consider the condition where maximum x size and y size are different

    pass 

def get_routes(city_names):
    """
    It takes a list of cities and returns a list of all possible routes between those cities
    
    :param city_names: a list of city names
    :return: A list of tuples representing all possible links between cities, 
            each item in the list (a link) represents a route between two cities.
    A, B, C
    [ ('A', 'B'), ('A', 'C'), ('B', 'C') ]
    """
    combinations = itertools.combinations(city_names, 2)
    return combinations

    pass


# TODO: Fix variable names
if __name__ == '__main__':
    city_names = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    '''print the cities and routes'''
    cities = get_randomly_spread_cities((100, 100), 10)
    routes = get_routes(city_names)
    print('Cities:')
    for i, city in enumerate(cities):
        print(f'{city_names[i]}: {city}')
    print('Routes:')
    for i, route in enumerate(routes):
        print(f'{i}: {route[0]} to {route[1]}')
