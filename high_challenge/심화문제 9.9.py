import wikipedia
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

wiki1 = wikipedia.page("South Korea")
wiki2 = wikipedia.page("Japan")
text = wiki1.content + wiki2.content

s_words = STOPWORDS.union({"south","north","korean","wolrd","country"})
wordcloud = WordCloud(width = 2000, height = 1500, stopwords = s_words).generate(text)

plt.imshow(wordcloud)
plt.show()
