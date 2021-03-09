from .find_kingdom import find_kingdom


def output(input):
    allies = []
    for secret_message in input:
        secret_message = secret_message.split()
        ally = find_kingdom(secret_message[0], ''.join(secret_message[1:]))
        if ally is not None:
            allies.append(ally)
    if len(set(allies)) >= 3:  # Condition to be a ruler
        return f'''SPACE {' '.join(allies)}'''  # outputs ruler or None
