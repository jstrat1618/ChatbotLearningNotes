import string
class MyText:
    def __init__(self, text, has_been_replaced=None):
        self.text = text

        self.words = text.split(" ")

        if not has_been_replaced:
            words = text.split(" ")

            has_been_replaced = [False for _ in words]

        self.has_been_replaced = has_been_replaced


    def __repr__(self):
        return self.text


    def swap_pronouns(self):

        #Create dictionary of replacements
        originals = ["you", "your", "yours", "me", "my", "mine", "i"]
        replacements = ["I", "my", "mine", "you", "your", "yours", "you"]
        rep_key = dict(zip(originals, replacements))

        new_text = ""

        for i in range(len(self.words)):
            if self.words[i] in rep_key.keys() and not self.has_been_replaced[i]:
                self.words[i] = rep_key[self.words[i]]
                self.has_been_replaced[i] = False

            new_text += self.words[i] + " "


        return MyText(new_text.rstrip(), has_been_replaced=self.has_been_replaced)


    def clean_text(self, has_been_replaced=None):
        text = self.text

        text = text.strip()

        text = text.lower()

        #Remove punctuation
        text = text.translate(str.maketrans('', '', string.punctuation))

        return MyText(text, has_been_replaced)





