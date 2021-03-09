import math


class Vehicle():
    def __init__(self, name, speed, crater_time, weather):
        self.name = name
        self.speed = speed
        self.crater_time = crater_time
        self.weather = weather

    def _real_speed(self, traffic, weather):
        if weather not in self.weather:
            return -1
        max_speed_possible = min(traffic, self.speed)
        return max_speed_possible

    def real_time(self, orbit):
        real_speed = self._real_speed(orbit.traffic, orbit.weather)
        if real_speed == -1:
            return math.inf
        duration = orbit.distance / real_speed  # Time = Distance/Speed
        crater_duration = self.crater_time * orbit.craters
        real_time = duration + crater_duration
        return real_time
