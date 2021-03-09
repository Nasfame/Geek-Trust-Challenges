from src.orbits import Orbit


def test_orbit():
    orbit_1 = Orbit("Orbit1", 18, 20, 15, 'sunny')
    weather_influence = {'sunny': -0.1, 'rainy': 0.2, 'windy': 0}

    assert orbit_1.name == "Orbit1"
    assert orbit_1.weather_influence == weather_influence
