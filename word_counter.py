#!/usr/local/bin/python3
# Made by @swisscoding on Instagram

from colored import stylize, fg

# decoration
print(stylize("\n---- | Word counter | ----\n", fg("red")))

# class
class Counter:
    def __init__(self, text):
        self.text = text

    # output magic method
    def __repr__(self):
        amount_of_words = self.count(self.text)
        if amount_of_words == 1:
            amount_of_words = stylize(amount_of_words, fg("red"))
            return f"\nThere is {amount_of_words} word in the given text.\n"
        else:
            amount_of_words = stylize(amount_of_words, fg("red"))
            return f"\nThere are {amount_of_words} words in the given text.\n"

    # methods
    def count(self, text):
        words = text.split(" ")

        return len(words)

# main execution
if __name__ == "__main__":
    # user interaction
    text = input("Text: ")

    print(Counter(text))
