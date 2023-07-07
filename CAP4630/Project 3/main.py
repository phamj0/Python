
class AntColonyOpt:
    def __init__(self, attractions, ant_count = 100 ):
        self.ant_count = ant_count                      # number of ants that will be used in algorithm, default is at 100 if no value is entered
        self.attractions = attractions                  # the array of attractions
        self.attraction_count = len(attractions)        # number of attractions 

    def ant(self):
        visited_attraction = []
        for place in range (0, (self.attraction_count-1)):
            visited_attraction.append(place)





















