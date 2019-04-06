#I adapted the code in sec1_chit_chat_bot.py to create a class
class DefinedResponses:
    def __init__(self):
        questions = ["hello", 'hi', "whats your name",
                     "what do you speak", "what languages do you speak",
                     "how do you say hello in klingon", "what's your favorite color"]
        answers = ["Hi!", "Hi!", "Eliza",
                   "English and some Klingon", "English and some Klingon",
                   'nuqneH', "green"]

        answer_key = dict(zip(questions, answers))

        self.questions = questions
        self.answer_key = answer_key

    def response(self, question):
        if question in self.questions:
            return self.answer_key[question]
        else:
            #Leverage Python's truthiness
            return ''
