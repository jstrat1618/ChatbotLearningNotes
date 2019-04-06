import re
from sec1_chit_chat_bot import ask_user
from Text import MyText
from DefinedResponses import DefinedResponses

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

            break

    return out_text



def main():
    greeting()

    user_input = ask_user()

    loaded_responses = DefinedResponses()

    while user_input.upper() != "Q":


        cleaned_input = MyText(user_input).clean_text()

        predefined_response = loaded_responses.response(cleaned_input.text)

        match_text = response_match(cleaned_input.text)

        if predefined_response:
            print(predefined_response)

        elif match_text:
            print(match_text)

        else:
            print("Sorry, I'm not familiar with that")

        user_input = ask_user()


if __name__ == '__main__':
    main()