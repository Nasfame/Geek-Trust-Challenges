import os
import sys

from geektrust import main


def test_geektrust():
    expected_result = "CAR ORBIT2"
    sys.stdout = open("temp_out.txt", 'w')
    sys.argv[1] = "test_input.txt"
    main()
    sys.stdout.close()
    with open("temp_out.txt", 'r') as f1:
        result = f1.readline()
        result = result.rstrip('\n')  # Remove line breaks
    os.remove("temp_out.txt")
    assert result == expected_result
