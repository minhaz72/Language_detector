import langdetect 
from langdetect  import * 
def Language_detector(txt :  set ) : 
    print(' ===  hi , this is a language detector : ')
    print('===input text to  detect your language : ')
    print(f' your language is {detect(txt)}')
if __name__ =='__main__ ': 
    txt= input('enter your txt : ')
    print(Language_detector(txt))
    