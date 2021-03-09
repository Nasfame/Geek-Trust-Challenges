''' 
This is a simple Coding excercise to test the coding style rather
than coding skill
'''

import os
import sys

from src import Family
from src.family_tree_structure import family_tree
from src import INPUT_FUNC_MAPPER,\
    InvalidParameters


def is_valid_input(command):
    ''' Simple user input Validation
    We cant trust any user input :(
    '''
    commands = command.split(" ")
    if not commands and commands[0] not in INPUT_FUNC_MAPPER:
        return False

    if commands[0] == "ADD_CHILD" and len(commands) != 4:
        return False

    if commands[0] == "GET_RELATIONSHIP" and len(commands) != 3:
        return False

    return True

def load_family_tree(family_tree):
    '''Initialize the family
    '''
    family_name = family_tree['name']
    members = family_tree['members']

    family = Family(family_name)
    for name, sex, mother, spouse in members:
        family.add_member(name, sex, mother, spouse)
    return family
            
def execute_command(command, family):
    result = None
    if not is_valid_input(command):
        raise InvalidParameters("Command does not support")
    command = command.split(" ")
    if command[0] == "ADD_CHILD":
        mother, name, sex = command[1:]
        result = family.add_member(name, sex, mother)

    elif command[0] == "GET_RELATIONSHIP":
        name, relation = command[1:]
        result = family.get_relationship(name, relation)

    return result

def main():
    family = load_family_tree(family_tree)
    try:
        input_file = sys.argv[1]
    except IndexError:
        input_file = "input_family.txt"
    finally:
        with open(input_file, 'r') as f1:
            content = f1.readlines()
            commands = [i.strip() for i in content]  # to remove\n in readlines()
        for command in commands:
            print(execute_command(command,family))



if __name__ == "__main__":
    main()
