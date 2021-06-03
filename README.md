# AI_Translator

## Clone

```sh
git clone https://github.com/sdsuy/AI_Translator.git machinetranslation
```

## Installation

```sh
pip3 install pylint
pip3 install pandas
pip3 install python-decouple
pip3 install ibm_watson
```

## Package import and use

```sh
python3
>>> import machinetranslation as mt
>>> mt.translator.englishtofrench('Hello World!')
'Bonjour le monde !'
>>> mt.translator.englishtogerman('Hello World!')
'Hallo Welt!'
>>> quit()
```

## Environment

### Create the .env file into machinetranslation folder with the values from your IBM Watson Language Translator service:

```sh
URL_LT={language translator url service}
APIKEY_LT={laguage translator api key}
VERSION_LT={date version YYYY-MM-DD}
```

## Testing

```sh
cd machinetranslation
python3 -m unittest tests.tests
```
