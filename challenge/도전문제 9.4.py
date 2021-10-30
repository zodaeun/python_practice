import wikipedia
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

wiki = wikipedia.page('coffee')
text = wiki.content

s_words = STOPWORDS.union({'many'},{'often'},{'one'},{'two'},{'may'},{'first'})

wordCloud = WordCloud(width = 1500, height = 1500, stopwords = s_words).generate(text)

plt.imshow(wordCloud)
plt.show()
