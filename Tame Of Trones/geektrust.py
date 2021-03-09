import sys

from src import output


def main():
    try:
        input_file = sys.argv[1]
    except IndexError:
        input_file = "src/input_tame_of_thrones.txt"
    finally:
        with open(input_file, 'r') as f1:
            messages = f1.readlines()
            messages = [message.rstrip('\n') for message in messages]  # To remove line breaks
            print(output(messages))
    return


''''Driver Code'''

if __name__ == "__main__":
    main()
