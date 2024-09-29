import tkinter as tk
import nltk #for natural languuage processing
from textblob import TextBlob #only for implementing the sentiment analysis part
from newspaper import Article

def summarize():

    url = utext.get("1.0", "end").strip()
# nltk.download('punkt_tab') #model needed for sentiment analysis


# #starting with the summarization and sentiment analysis part because it is the easy and quick part
# url = 'https://www.hindustantimes.com/cricket/jasprit-bumrahs-clever-i-respect-everyone-but-response-on-being-asked-to-name-a-tough-batter-leaves-crowd-elated-101725015507562.html'
# #as the important work is done by these libraries we dont need to do actually natural language processing
    article = Article(url) #by doing this it will create an Article object of the newspaper library and it is focussed on url.
    article.download()
    article.parse() #parsing means it will disect the article in the neccesary parts
    article.nlp()

    title.config(state='normal')
    author.config(state='normal')
    Publication.config(state='normal')
    summary.config(state='normal')
    sentiment.config(state='normal')

    title.delete('1.0','end')
    title.insert('1.0', article.title)

    author.delete('1.0','end')
    author.insert('1.0', article.authors)

    Publication.delete('1.0','end')
    Publication.insert('1.0', article.publish_date)

    summary.delete('1.0','end')
    summary.insert('1.0', article.summary)

    analysis = TextBlob(article.text)
    sentiment.delete('1.0', 'end')
    sentiment.insert('1.0', f"Polarity :{analysis.polarity}, sentiment : {'positive' if analysis.polarity > 0 else 'negative' if analysis.polarity < 0 else 'neutral'}")

    title.config(state='disabled')
    author.config(state='disabled')
    Publication.config(state='disabled')
    summary.config(state='disabled')
    sentiment.config(state='disabled')
    # print(f"title : {article.title}")
    # print(f"Authors : {article.authors}")
    # print(f"Publication date : {article.publish_date}")
    # print(f"Summary : {article.summary}")

    # here the news extraction part and all is done

    # now start with sentiment analysis part

    #we'll need to turn the nes article in a textblob version
    

root = tk.Tk()
root.title('News Summarizer')
root.geometry('1200x600')

tlabel = tk.Label(root, text='Title')
tlabel.pack()

title = tk.Text(root, height = 1, width =140)
title.config(state='disabled', bg='#dddddd')
title.pack()

alabel = tk.Label(root, text='Author')
alabel.pack()

author = tk.Text(root, height = 1, width =140)
author.config(state='disabled', bg='#dddddd')
author.pack()

plabel = tk.Label(root, text='Publication Date')
plabel.pack()

Publication = tk.Text(root, height = 1, width =140)
Publication.config(state='disabled', bg='#dddddd')
Publication.pack()

slabel = tk.Label(root, text='Summary')
slabel.pack()

summary = tk.Text(root, height = 20, width =140)
summary.config(state='disabled', bg='#dddddd')
summary.pack()

selabel = tk.Label(root, text='Sentiment Analysis')
selabel.pack()

sentiment = tk.Text(root, height = 1, width =140)
sentiment.config(state='disabled', bg='#dddddd')
sentiment.pack()

ulabel = tk.Label(root, text='URL')
ulabel.pack()

utext = tk.Text(root, height = 1, width =140)
# utext.config(state='enabled', bg='#dddddd')
utext.pack()

btn = tk.Button(root, text="Summarizer", command=summarize)
btn.pack()
root.mainloop()
