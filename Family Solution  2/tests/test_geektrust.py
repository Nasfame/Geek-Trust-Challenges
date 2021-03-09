import pytest
import sys
import os

from os.path import dirname, abspath
sys.path.append(dirname(dirname(abspath(__file__))))

from geektrust import is_valid_input, load_family_tree,\
    execute_command
    
from ..src import InvalidParameters

def test_user_input_validation_correct():
    userinput = "ADD_CHILD Satya Yaya Female"
    valid = is_valid_input(userinput)
    assert valid == True

def test_user_input_validation_wrong():
    userinput = "ADD_CHILD"
    valid = is_valid_input(userinput)
    assert valid == False
    
def test_execute_command_wrong(testFamily):
    userinput = "WRONGINPUT"
    with pytest.raises(InvalidParameters) as e:
        response = execute_command(userinput, testFamily)
    assert "Command does not support" in str(e.value)

def test_execute_command_wrong(testFamily):
    userinput = "ADD_CHILD mother Female child"
    response = execute_command(userinput, testFamily)
    assert response == "CHILD_ADDITION_SUCCEEDED"
