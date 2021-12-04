#                      Listen-News
import requests
import json

def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.Spvoice")
    speak.Speak(str)
if __name__ == '__main__':
    speak("Hello, Everyone, how are you , Let's hear some News headlines")
    url = "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=c34e6fdc7229497aa7739ef14e1abc07"
    news = requests.get(url).text
    # print(news)
    news_dic = json.loads(news)
    print(news_dic["articles"])
    arts = news_dic["articles"]
    for article in arts:
       speak(article['title'])
       speak("Moving on to next News headline......Listen please")
    speak("Thank you for Listening....See you later")



