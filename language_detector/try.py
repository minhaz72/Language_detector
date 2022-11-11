import langdetect
from langdetect import detect
print('-----hi, this a language detector----')
text=str(input('enter a text'))
print(detect(text))
