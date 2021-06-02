import os
from decouple import config
from ibm_watson import LanguageTranslatorV3
import json
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
# from pandas import json_normalize

URL_LT = config('URL_LT')
APIKEY_LT = config('APIKEY_LT')
VERSION_LT = config('VERSION_LT')
authenticator = IAMAuthenticator(APIKEY_LT)
language_translator = LanguageTranslatorV3(version=VERSION_LT, authenticator=authenticator)
language_translator.set_service_url(URL_LT)

# Get language codes
# language_codes = json_normalize(language_translator.list_identifiable_languages().get_result(), "languages")
# print(language_codes.values)


def englishtofrench(text):
    '''
    Translate english text to french
    '''
    # French Translation
    try:
        translation_response = language_translator.translate(text=text , model_id='en-fr')
    except ValueError as error:
        return error.__str__()
    
    translation = translation_response.get_result()
    french_translation = translation['translations'][0]['translation']

    return french_translation

def englishtogerman(text):
    '''
    Translate english text to french
    '''
    # German Translation
    try:
        translation_response = language_translator.translate(text=text , model_id='en-de')
    except ValueError as error:
        return error.__str__()
    
    translation = translation_response.get_result()
    german_translation = translation['translations'][0]['translation']

    return german_translation
