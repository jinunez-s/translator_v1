#Python
#pip3 install googletrans

#importing libraries
from googletrans import Translator, constants
from pprint import pprint

#interface from googletrans
#init the Google API translator
translator = Translator()

#install newer version of googletrans
# pip3 uninstall googletrans
# pip3 install googletrans==3.1.0a0

#translate a spanish text to arabic for instance
translation = translator.translate("Hola mundo", dest="en")
print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")

#translate more than phrase
sentences = [
    "Hello everyone",
    "How are you ?",
    "Do you speak english ?",
    "Good bye!"
]

translations = translator.translate(sentences, dest="en")
for translation in translations:
    print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")