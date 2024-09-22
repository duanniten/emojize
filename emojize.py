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
    splited = emoti.split(sep= ' ')
    transformed_text = ''
    for text_part in splited:
        if text_part[0] == ':' and text_part[-1] == ':':
            transformed_text += emojize(
                text_part, delimiters= [':', ':'], language='en', 
                ) + ' '
        else:
            transformed_text += text_part + ' '
    return transformed_text[:-1]

if __name__ == '__main__':
    main()
