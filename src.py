import tkinter as tk
import nltk
from textblob import TextBlob
from newspaper import Article

# nltk.download('punkt_tab')

# url = "https://finshots.in/archive/why-jio-wants-to-file-your-taxes/"

# article = Article(url)
# article.download()
# article.parse()

# article.nlp()

# print("Title:", article.title)
# print("Authors:", article.authors)
# print("Publish Date:", article.publish_date)
# print("Summary:", article.summary)
# # print("Text:", article.text)

# analysis = TextBlob(article.text)
# print("Sentiment:", analysis.sentiment)
# print(f"Positive" if analysis.sentiment.polarity > 0 else "Negative" if analysis.sentiment.polarity < 0 else "Neutral")

def summarize():
    url = utext.get('1.0', 'end').strip()
    article = Article(url)
    article.download()
    article.parse()

    article.nlp()

    # enabling to edit on ui
    title.config(state="normal")
    author.config(state="normal")
    pdate.config(state="normal")
    summary.config(state="normal")
    sentiment.config(state="normal")

    title.delete('1.0', 'end')
    title.insert('1.0', article.title)

    author.delete('1.0', 'end')
    author.insert('1.0', article.authors)

    pdate.delete('1.0', 'end')
    pdate.insert('1.0', article.publish_date)

    summary.delete('1.0', 'end')
    summary.insert('1.0', article.summary)

    analysis = TextBlob(article.text)
    sentiment.delete('1.0', 'end')
    sentiment.insert(
        '1.0',
        f"Polarity: {analysis.polarity}, Sentiment: {'Positive' if analysis.sentiment.polarity > 0 else 'Negative' if analysis.sentiment.polarity < 0 else 'Neutral'}"
    )
    #disbling back
    title.config(state="normal")
    alabel.config(state="normal")
    plabel.config(state="normal")
    slabel.config(state="normal")
    sentiment.config(state="normal")

root = tk.Tk()
root.title("News Article Sentiment Analysis")
root.geometry("1200x600")


tlabel = tk.Label(root, text="title")
tlabel.pack()

title = tk.Text(root, height=1, width=140)
title.config(state='disabled', bg="lightgrey")
title.pack()

alabel = tk.Label(root, text="Author")
alabel.pack()

author = tk.Text(root, height=1, width=140)
author.config(state='disabled', bg="lightgrey")
author.pack()

plabel = tk.Label(root, text="Publication Date")
plabel.pack()

pdate = tk.Text(root, height=1, width=140)
pdate.config(state='disabled', bg="lightgrey")
pdate.pack()

slabel = tk.Label(root, text="Summary")
slabel.pack()

summary = tk.Text(root, height=20, width=140)
summary.config(state='disabled', bg="lightgrey")
summary.pack()

sentimentlabel = tk.Label(root, text="Sentiment Analysis")
sentimentlabel.pack()

sentiment = tk.Text(root, height=1, width=140)
sentiment.config(state='disabled', bg="lightgrey")
sentiment.pack()

ulabel = tk.Label(root, text="URL")
ulabel.pack()

utext = tk.Text(root, height=1, width=140)
utext.pack()

btn = tk.Button(root, text="Summarize", command=summarize)
btn.pack()



root.mainloop()