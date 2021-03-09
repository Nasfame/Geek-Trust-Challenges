from src.output import output

def test_output():
    with open("test_input.txt", "r") as f1:
        input_ = f1.read()
    weather, orbit1, orbit2 = input_.lower().split()
    result = output(weather,int(orbit1),int(orbit2))
    expected_result = "CAR ORBIT2"
    assert result == expected_result