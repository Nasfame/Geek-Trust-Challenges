from src.caesar_cipher import caesar_cipher


def test_caesar_cipher():
    kingdom = "AIR"
    secret_message = "ROZO"
    expected_result = "OLWL"
    result = caesar_cipher(secret_message, len(kingdom))
    assert result == expected_result
