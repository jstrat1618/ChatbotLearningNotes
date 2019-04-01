import re
from sec1_chit_chat_bot import ask_user, clean_user_input
from Text import MyText

def greeting():
    print("---------------------------------------")
    print("              WELCOME!")
    print("My name is Eliza!")
    print("---------------------------------------")


def response_match(text):
    user_says = ['^remember when', '^do you remember', '^remember that time', '^do you recall']

    bot_says = ['how could I forget when', 'how could I forget when',
                'how could I forget when', 'how could I forget when']

    ref_dict = dict(zip(user_says, bot_says))

    out_text = ''

    for match,replace in ref_dict.items():
        regex_match = re.match(match, text)

        if regex_match:
            rest_of_string = text[regex_match.end():].lstrip()

            text_swap = MyText(rest_of_string).swap_pronouns()

            out_text = replace + " " + text_swap.text +"!!!"

    return out_text



def main():
    greeting()

    user_input = ask_user()

    while user_input.upper() != "Q":


        cleaned_input = clean_user_input(user_input)

        match_text = response_match(cleaned_input)

        #Using Python's "truthiness" for an empty string here
        response = match_text if match_text else "Sorry, I'm not familiar with that"

        print(response)

        user_input = ask_user()


if __name__ == '__main__':
    main()