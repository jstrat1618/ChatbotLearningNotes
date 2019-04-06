def greeting():
    print("--------------------------------------")
    print("         WELCOME")
    print("--------------------------------------")

    print("My name is Chit-Chat!")
    print("I can make small talk, but not much else")


def get_responses():
    questions = ["hello", 'hi', "what's your name?",
                 "what do you speak?", "what languages do you speak?",
                 "how do you say hello in klingon?", "what's your favorite color?"]
    answers = ["Hi!", "Hi!", "Chit Chat!",
               "English and some Klingon", "English and some Klingon",
               'nuqneH', "green"]

    return dict(zip(questions, answers))


def ask_user():
    user_input = input("What would you like to say? [Q]uit ")
    return user_input

def clean_user_input(user_input):

    text = user_input.strip()

    text = text.lower()

    return text


def respond(user_input, data, default="Sorry, I'm not familiar with that"):

    if user_input in data.keys():
        response = data[user_input]

    else:
        response = default

    return response

def main():
    greeting()

    user_input = "dummy string"

    responses = get_responses()

    while user_input.upper() != "Q":
        user_input = ask_user()

        user_input = clean_user_input(user_input)

        if user_input.upper() != "Q":
            output = respond(user_input, data=responses)
            print(output)

    print("Goodbye!")

if __name__ == '__main__':
    main()