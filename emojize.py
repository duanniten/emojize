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
    return input("Input: ").strip()

def get_emotion(emoti):
    try:
        return emojize(emoti, delimiters= [':', ':'])
    except:
        sys.exit("Emoji not found")

if __name__ == '__main__':
    main()
