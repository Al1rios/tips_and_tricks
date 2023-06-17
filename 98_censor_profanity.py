
from better_profanity import profanity

text = ' I hate this shit '

censored_text = profanity.censor(text)

print(censored_text)

text2 = 'i hate this shit so much'

censored_text2 = profanity.censor(text2, censor_char="&")

print(censored_text2)

text3 = 'i hate this shit so much'

print(profanity.contains_profanity(text3))

bad_words = ['hate', 'war', 'evil']

profanity.load_censor_words(bad_words)

text4 = 'people that love war are evil'

censored_text4 = profanity.censor(text4)

print(censored_text4)