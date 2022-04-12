import googletrans
from googletrans import Translator
import time

def translate():
    translator = Translator()

    x = True
    keys = list(googletrans.LANGUAGES.keys())
    value = list(googletrans.LANGUAGES.values())

    while x == True:
        time.sleep(1)
        targetlang = input("What language do you want to translate to?")
        targetlang = keys[value.index(targetlang.lower())]
        time.sleep(1)
        sentence = input("What would you like to translate?")
        startlang = translator.detect(sentence).lang
        time.sleep(1)
        print("The starting language is: " + googletrans.LANGUAGES[startlang])
        time.sleep(1)
        print("The starting phrase is: " + sentence)
        time.sleep(1)
        print("The target language is: " + googletrans.LANGUAGES[targetlang])
        time.sleep(1)
        translation = translator.translate(sentence, src = startlang, dest = targetlang)
        print("The translation is: " + translation.text)
        time.sleep(1)
        check = input("Do you want to translate another phrase? (yes/no)")

        if(check == "no"):
            x = False






if __name__ == '__main__':
    translate()
