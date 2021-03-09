import sys

from src import output


def main():
    try:
        input_file = sys.argv[1]
    except IndexError:
        input_file = "src/input_in_traffic.txt"
    finally:
        with open(input_file, 'r') as f1:
            input_ = f1.read()
            weather, orbit1, orbit2 = input_.lower().split()
            print(output(weather, int(orbit1), int(orbit2)))
    return


''''Driver Code'''

if __name__ == "__main__":
    main()
