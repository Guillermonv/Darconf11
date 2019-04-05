from os import path
from wordcloud import WordCloud
import matplotlib.pyplot as plt

dirname = path.dirname(__file__)

text = open(path.join(dirname, 'docs/words.txt')).read()

wordcloud = WordCloud(max_font_size=50, max_words=100, background_color="white").generate(text)

plt.imshow(wordcloud)

plt.axis("off")

plt.show()
