# from pygoogletranslation import Translator
# translator = Translator()
# translator.translate('Good Morning', dest='ta')

#
# import translators as ts
#
# res = ts.deepl("Welcome to our tutorial!", to_language='fr')
# print(res)

import os
import json

import translator as translator

# !pip install deep-translator
from deep_translator import GoogleTranslator

translator = GoogleTranslator(source='auto', target='fr')
print(translator.translate("Welcome to our tutorial!"))