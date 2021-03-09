from src.output import output

def test_output():
    with open("test_input.txt", "r") as f1:
        secret_messages = f1.readlines()
        secret_messages = [message.rstrip('\n') for message in secret_messages]
    result = output(secret_messages)
    expected_result = "SPACE LAND ICE FIRE"
    assert result == expected_result
