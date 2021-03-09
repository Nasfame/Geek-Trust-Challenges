from src.find_kingdom import find_kingdom


def test_find_kingdom():
    kingdom = "AIR"
    secret_message = "ROZO"
    result = find_kingdom(kingdom, secret_message)
    assert result == kingdom
