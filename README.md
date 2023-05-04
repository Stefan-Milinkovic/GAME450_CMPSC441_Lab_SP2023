# Repository for Labs
## CMPSC 441 and GAME 450

This repository will contain code for all the lab sessions for the course. New folders will be added to 'src' folder with the name of the lab. 

Abstract (250 words)
This repository contains all of the labs that we have done throughout the semseter, and includes the final project as well. The code is a game using Pygame where the player navigates between cities that are equally spread apart, and the player comes accross many enemy agents along the way. The game consists of multiple classes that define the behavior and attributes of various game entities. The PyGameHumanPlayer and PyGameHumanCombatPlayer classes allow the game to be played through a Pygame interface, where users to use keyboard input to make selections for their player. The selectAction and weapon_selecting_strategy methods are called during each round of the game to allow the player to choose their destination and their weapon of choice.

CMPSC 441 Final Project Report

In this final project, I incorporated many different AI concepts that we learned throughout the semester. These concepts include intelligent agents, reinforcement learning, and text to image generation. To improve the quality of my project I included concepts that fixed specific parts of my project. One of the improvements I made was to incorporate a GA system to make the cities more realistically spread out. I did this by making sure that no city was on top of eachother, using a fitness function (Appendix D). Another improvement I made was I implemented a system that would carry the cost of travel depending on the elevation of the route. I modified the ‘get_route_cost’ function so that if the path elevation was anything above 1.5 (Appendix B). Also, I implemented a feature into the game that restricted movement between cities without a route. I created a fitness function that checked if the elevation was too high, or if the route was underwater (Appendix E). Finally, I incorporated a feature that would end the game if the player ran out of money. I did this by importing the ‘get_route_cost’ function into the ‘pygame_human_player’ file, and checking to see if the player’s balance was equal to 0. If the player has no money, then the program will terminate (Appendix F).

The additional AI technique that I incorporated into my project was a text to image generator. I implemented this in the rl_episodes file. I created a class that generates a crown image at the end of a round between the AI player and the Human player, which identifies which side was victorious.

Appendix A: Cities and Routes
Lab 2:
We started the semester off by creating a map that has different cities and routes, which we did in lab 2. 

Function: get_randomly_spread_cities
Inputs: 
size: a tuple of two integers representing the maximum x and y values for the map
n_cities: an integer representing the number of cities to be generated
Outputs: A list of n_cities cities, where each city is represented as a tuple of two integers (x, y) that represent its coordinates on the map.
Description: This function takes in two parameters: size and n_cities. The function returns a list of n_cities cities, where each city is represented as a tuple of two integers (x, y) that represent its coordinates on the map. The coordinates are randomly generated within the range of (0,0) to (size[0], size[1]).

Function: get_routes
Inputs: city_names: a list of city names
Outputs: A list of all possible routes between the cities in city_names. The routes are represented as a list of tuples, where each tuple represents a link between two cities.
Description:
This function takes in a single parameter, city_names, which is a list of city names. The function returns a list of all possible routes between the cities in city_names. The routes are represented as a list of tuples, where each tuple represents a link between two cities.


Appendix B: Calculating Route Cost
Lab3:

Lab 3 was where we calculated the route cost.

Function: get_route_cost
Inputs: 
- route_coordinate: a tuple of coordinates of cities to connect
- game_map: a numpy array of floats representing the cost of each cell
Outputs:
- a floating point number representing the cost of the route
Description:
This function takes a tuple of coordinates of cities to connect, and a numpy array of floats representing the cost of each cell. For each route, it finds the cells that lie on the line between the two cities at the endpoints of a route, and then sums the cost of those cells. The cost between cities is the sum of the costs of the cells on the line. 

Function: route_to_coordinates
Inputs: 
- city_locations: a numpy array of integers representing the locations of cities
- city_names: a list of city names
- routes: a list of tuples representing the routes
Outputs:
- a list of tuples of coordinates of cities to connect
Description:
This function takes in the numpy array of integers representing the locations of cities, a list of city names, and a list of tuples representing the routes. It returns a list of tuples of coordinates of cities to connect. For each route, it finds the coordinates of the start and end cities and appends them to the route coordinates list.

Function: generate_terrain
Inputs: 
- map_size: a tuple representing the size of the terrain map to be generated
Outputs:
- a numpy array of floats representing the generated terrain map
Description:
This function generates a numpy array of floats representing a terrain map of size map_size using a random number generator.

Appendix C: Generating Map With Elevation
Lab 5:

Lab 5 is where we generated the map using numpy and noise. 
Function: generate_surface
Inputs: size (tuple)
Outputs: pygame_surface 
Description: This function takes in a tuple representing the size of the landscape, generates a landscape using perlin noise from the get_landscape function in landscape.py, creates a pygame surface from the generated landscape using surfarray.make_surface from pygame.surfarray, and returns the resulting pygame surface.

Function: draw_routes
Inputs: None
Outputs: None
Description: This function draws the first 10 routes between cities on the screen using pygame.draw.line function. It uses the global variables "routes" and "city_locations_dict" to get the starting and ending locations for each route.

Function: draw_cities
Inputs: None
Outputs: None
Description: This function draws the cities on the screen using pygame.draw.circle function. It uses the global variable "city_locations" to get the locations of the cities, and the global variables "color" and "radius" to set the color and radius of the circles.

Overall Description: This code is a combined procedural content generation and project lab for creating the static components of a game. It imports the necessary modules and functions, and defines helper functions for generating a pygame surface from a generated landscape, drawing routes between cities, and drawing cities on the screen. It initializes pygame and the screen, generates a landscape and sets up the cities and routes, and continuously draws the cities and routes on the screen until the user closes the window. The purpose of this lab is to get the user familiar with the pygame.draw functions, use perlin noise to generate a landscape, and build a mindset of writing modular code.

Function: get_elevation
Inputs: size:  tuple, represents the size of the landscape to be generated in pixels (width, height)
Outputs: elevation:  2D numpy array of shape (width, height), representing the elevation of each point in the landscape generated using perlin noise.
Description: This function generates a landscape using perlin noise algorithm and returns the elevation values as a numpy array.

Function: elevation_to_rgba
Inputs: elevation: 2D numpy array of shape (width, height), representing the elevation of each point in the landscape generated using perlin noise.
Outputs: landscape: 3D numpy array of shape (width, height, 3), representing the RGB values of each pixel in the landscape.
Description: This function takes in the elevation values of a landscape generated using perlin noise and returns a numpy array representing the landscape as an RGB image.

Function: get_landscape
Inputs: size: tuple, represents the size of the landscape to be generated in pixels (width, height)
Outputs: 3D numpy array of shape 
Description: This function is a lambda function that generates a landscape using perlin noise algorithm, calls the elevation_to_rgba function on the generated elevation values and returns the resulting RGB landscape.

Appendix D: Creating Realistic Cities
Lab 7:
Lab 7 is where we used GA to create realistic cities.

Function: game_fitness
Inputs:
- cities: List of coordinates for cities, where each city is a tuple (x, y)
- idx: int giving index of the current solution being evaluated
- elevation: 2D numpy array of the elevation data for the map
- size: Tuple representing the size of the map; width and height
Outputs: fitness` (float): The fitness value for the current solution
Description:
The ”game_fitness” function is a fitness function used to evaluate the fitness of a given set of cities. The function takes in a list of cities, their index in the population being evaluated, the elevation data of the map, and the size of the map, and returns a fitness value. The function checks the following criteria to assign fitness values:

The cities should not be under water. For each city, if its elevation is less than 0.05, a fitness penalty of -10 is assigned. The cities should have a realistic distribution across the landscape. For each city, the function calculates its distance from the center of the map, and assigns a fitness bonus based on how close the city is to the center. The closer the city to the center, the higher the fitness bonus. The cities may not be on top of mountains or on top of each other: For each pair of cities, the function calculates the distance between them, and assigns a fitness penalty of -10 if the distance is less than 5. Additionally, if either city is on top of a mountain (elevation greater than 0.95), a fitness penalty of -10 is assigned. Finally, the fitness value is returned at the end of the function.

Appendix E: Atomizing the Game
Lab 11:
Lab 11 is where we made the game run automatically between the AI and the player.
Function: PyGameAICombatPlayer.selectAction()
Inputs: self, state
Outputs: An integer value representing the selected action.
Description: This method selects an action based on the input state passed as an argument. It first checks the events in the Pygame event queue and returns the value of the key pressed if it is a number between 0 to 9. If no number key is pressed, it returns the ASCII value of the current city name, which may not be a safe operation for more than 10 cities. 

Function: PyGameAICombatPlayer.__init__()
Inputs: self: class object, name: string
Outputs: None
Description: This is the constructor of the `PyGameAICombatPlayer` class. It initializes the object of the class and takes `self` and `name` as arguments, where `self` refers to the instance of the object being created, and `name` refers to the name of the player. 

Function: weapon_selecting_strategy()
Inputs: self: class object
Outputs: int: representing the selected weapon.
Description: This method selects a weapon for the combat player. If the event is of type `pygame.QUIT`, it terminates the program. If the event is of type `pygame.KEYDOWN` and the pressed key is "s", "a", or "f", it assigns the corresponding integer value to the `weapon` attribute of the class instance and returns it. The `weapon` attribute represents the index of the selected weapon.

Function: PyGameHumanPlayer.selectAction()
Inputs: state: an object representing the current state of the game.
Outputs: An integer representing the selected action.
Description: 
This method is part of the PyGameHumanPlayer class, which represents a human player in a game using the Pygame library. The selectAction() method allows the player to select an action based on the current state of the game. The method waits for the player to press a key on the keyboard and returns the integer value of the key pressed, which represents the selected action. If the player’s balance is less than the travel cost, or if their balance is 0, the game terminates. 
Function: PyGameHumanCombatPlayer.weapon_selecting_strategy()
Inputs: 
- None.
Outputs:
- An integer representing the selected weapon.
Description: 
This method is part of the PyGameHumanCombatPlayer class, which represents a human player in combat. The weapon_selecting_strategy() method allows the player to select a weapon for combat. The method waits for the player to press a key on the keyboard and returns the integer value of the selected weapon. The letters "s", "a", and "f" represent the weapons in the game, with "s" representing the sword, "a" the arrow, and "f" for fire. The method uses a dictionary to convert the key pressed into the corresponding weapon number and returns that value minus one, since the weapon numbers start at zero in the game. If the player presses the "QUIT" button, the game is terminated.


Appendix: 
Appendix A: Cities and Routes
Appendix B: Calculating Route Cost
Appendix C: Generating Map with Elevation
Appendix D: Creating Realistic Cities
Appendix E: Atomizing the Game 
