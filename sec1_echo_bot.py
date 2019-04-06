def greeting():
    print("----------------------------------------")
    print("         WELCOME")
    print("I'm Echo Bot")
    print("I just Echo back whatever you say.")
    print("----------------------------------------")
def ask_user():
    user_input = input("What would you like to say? [Q]uit ")

    message =  user_input

def echo_respond(msg):
    bot_output = 'ECHO BOT: I hear you. You said "{}"'.format(msg)

    return bot_output


def main():
    greeting()

    user_input = "dummy string"

    while user_input.upper() != "Q":
        user_input = ask_user()

        if user_input.upper() != "Q":
            output = echo_respond(user_input)
            print(output)


if __name__ == '__main__':
    main()