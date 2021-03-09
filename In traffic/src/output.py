from .orbits import Orbit
from .vehicles import Vehicle


def output(weather, orbit1_traffic, orbit2_traffic):
    bike = Vehicle("bike", 10, 2 / 60, ["sunny", "windy"])  # converting mins to hour
    tuk_tuk = Vehicle("tuktuk", 12, 1 / 60, ["sunny", "rainy"])
    car = Vehicle("car", 20, 3 / 60, ["sunny", "windy", "rainy"])

    orbit_1 = Orbit("Orbit1", 18, 20, orbit1_traffic, weather)
    orbit_2 = Orbit("Orbit2", 20, 10, orbit2_traffic, weather)

    vehicles = [bike, tuk_tuk, car]
    orbits = [orbit_1, orbit_2]
    priority = {bike: 1, tuk_tuk: 2, car: 3}

    time_taken_by_vehicles = []

    for vehicle in vehicles:
        time_taken_by_this_vehicle = []
        for orbit in orbits:
            time_taken = vehicle.real_time(orbit)
            time_taken_by_this_vehicle.append((time_taken, orbit.name))
        time_taken_by_this_vehicle.sort()
        min_time, orbit_name = time_taken_by_this_vehicle[0]
        time_taken_by_vehicles.append((min_time, priority[vehicle], vehicle.name, orbit_name))

    time_taken_by_vehicles.sort()
    best_vehicle, best_orbit = time_taken_by_vehicles[0][2:]
    output = f'''{best_vehicle} {best_orbit}'''

    return output.upper()
