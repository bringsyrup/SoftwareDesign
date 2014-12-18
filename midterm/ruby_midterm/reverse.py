#! /bin/env python 

def reverse_text(input_text):
    """
    Takes in some text and returns the text in reversed order
    (character by character)
    """
    new_name = ""
    for i in range(1, len(input_text)+1):
        new_name += input_text[-i]
    return new_name
    
def main():
    my_name = "whadya think?"
    print reverse_text(my_name)

if __name__ == "__main__":
    main()

