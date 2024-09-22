from emoji import emojize
import sys

def main():
    #read emotion code
    emoti = read_emotion()

    #get emotion from emojize
    emoti = get_emotion(emoti)

    #print emoji
    print_emotion(emoti)

def print_emotion(emoti: str):
    print(f'Output: {emoti}')

def read_emotion():
    try: 
        return input("Input: ")
    except EOFError:
        sys.exit("Should enter a text")

def get_emotion(emoti: str):
    return emojize(emoti)

if __name__ == '__main__':
    main()
