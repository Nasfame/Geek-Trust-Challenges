class Orbit():
    weather_influence = {'sunny': -0.1, 'rainy': 0.2, 'windy': 0}

    def __init__(self, name, distance, craters, traffic, weather):
        self.name = name
        self.distance = distance
        self.craters = craters + self.weather_influence[weather] * craters
        self.traffic = traffic
        self.weather = weather
