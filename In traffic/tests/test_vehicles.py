from src.orbits import Orbit
from src.vehicles import Vehicle


def test_vehicles():
    bike = Vehicle("bike", 10, 2 / 60, ["sunny", "windy"])

    assert bike.name == "bike"
    assert bike.weather == ["sunny", "windy"]
    assert bike.speed == 10
    assert bike.crater_time == 2 / 60


def test_real_time():
    tuk_tuk = Vehicle("tuktuk", 12, 1 / 60, ["sunny", "rainy"])
    orbit_1 = Orbit("Orbit1", 18, 20, 15, "sunny")
    real_time = tuk_tuk.real_time(orbit_1)
    expected_real_time = 1.8
    assert real_time == expected_real_time


def test_real_speed():
    tuk_tuk = Vehicle("tuktuk", 12, 1 / 60, ["sunny", "rainy"])
    orbit_1 = Orbit("Orbit1", 18, 20, 15, "sunny")
    real_speed = tuk_tuk._real_speed(orbit_1.traffic, orbit_1.weather)
    expected_real_speed = 12
    assert real_speed == expected_real_speed
