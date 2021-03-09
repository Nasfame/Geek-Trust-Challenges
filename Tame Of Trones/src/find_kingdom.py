from .caesar_cipher import caesar_cipher


def find_kingdom(kingdom, secret_msg):
    emblem = {'SPACE': 'GORILLA', 'LAND': 'PANDA', 'WATER': 'OCTOPUS', 'AIR': 'OWL', 'ICE': 'MAMMOTH', 'FIRE': 'DRAGON'}
    decoded_msg = caesar_cipher(secret_msg, len(emblem[kingdom]))
    message_characters = {}
    for character in decoded_msg:
        if character not in message_characters:
            message_characters[character] = 1
        else:
            message_characters[character] += 1
    for character in emblem[kingdom]:
        if character in message_characters and message_characters[character] > 0:
            message_characters[character] -= 1
        else:
            return None
    return kingdom
