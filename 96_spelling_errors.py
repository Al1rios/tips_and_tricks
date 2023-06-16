
from textblob import TextBlob

def correct_text(n: str):
    textblob = TextBlob(n)
    corrected_text = textblob.correct()
    return corrected_text

print(correct_text("do you studied in franse"))


from textblob import Word

word = Word('buy potatoe').pluralize()

print(word)
