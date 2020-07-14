# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor
class LatLon: # set the class
    def __init__(self, lat, lon): # init method with attributes.
        self.lat = lat # create variables for attributes.
        self.lon = lon
        
# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.
class Waypoint(LatLon):# class with inherited latlon class.
    def __init__(self, lat, lon, name): # init method with attributes.
        super().__init__(lat, lon) # gather lat, lon variables from latlon class.
        self.name = name # create new variable.

    def __str__(self): # str method used to use print an output.
        output = (
            f'name {self.name} is located',
            f'at {self.lat},{self.lon}!' # f string to show name and coordinates.
        )
        return '\n'.join(output)# return the output seperated by lines.

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?
class Geocache(LatLon):
    def __init__(self, lat, lon, name, diff, size):
        super().__init__(lat, lon)
        self.name = name
        self.diff = diff
        self.size = size

    def __str__(self): # str method used to use print an output.
        output = (
            f'name {self.name} is located',
            f'at {self.lat},{self.lon}. Its difficulty is {self.diff} and',
            f'its size is {self.size}!' # f string to show name and coordinates.
        )
        return '\n'.join(output) # return the output seperated by lines.

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

waypoint = Waypoint(name='Catacombs', lat=41.70505, lon=-121.51521) # create the new waypoint.

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556
geocache = Geocache(
                name="Newberry Views",
                diff=1.5,
                size=2,
                lat=44.052137,
                lon=-121.41556
                ) # set the Newberry Views geocache waypoint.

# Print it--also make this print more nicely
print(geocache) 
