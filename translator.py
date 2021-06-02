import os
from decouple import config
from ibm_watson import LanguageTranslatorV3
import json
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from pandas import json_normalize

URL_LT = config('URL_LT')
APIKEY_LT = config('APIKEY_LT')
VERSION_LT = config('VERSION_LT')

def englishtofrench(text):
    '''
    Translate english text to french
    '''
    authenticator = IAMAuthenticator(APIKEY_LT)
    language_translator = LanguageTranslatorV3(version=VERSION_LT, authenticator=authenticator)
    language_translator.set_service_url(URL_LT)

    json_normalize(language_translator.list_identifiable_languages().get_result(), "languages")

    # French Translation
    translation_response = language_translator.translate(text=text , model_id='en-fr')
    translation = translation_response.get_result()
    french_translation = translation['translations'][0]['translation']

    return french_translation
