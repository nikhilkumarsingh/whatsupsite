import os
from os import path
from PIL import Image
import numpy as np
from wordcloud import WordCloud, STOPWORDS



def wcloud(text,query):
     os.chdir('C:\\mysite1\\twapp\\static\\')
     mask = np.array(Image.open(os.getcwd() + '\\masks\\circle.png'))
     stopwords = set(STOPWORDS)
     stopwords.add(query)
     wc = WordCloud(background_color="white",
                    max_words=50,
                    mask=mask,
                    stopwords=stopwords,
                    width=800,
                    height=400,
                    mode="RGB",
                    )
     wc.generate(text)
     index=str(len(os.listdir(os.getcwd()+ "\\clouds\\")))
     file_name=index +'.png'
     wc.to_file(os.getcwd()+'\\clouds\\'+file_name)
     return "clouds\\"+file_name

'''
(self, font_path=None, width=400, height=200, margin=2,
                 ranks_only=None, prefer_horizontal=0.9, mask=None, scale=1,
                 color_func=random_color_func, max_words=200, min_font_size=4,
                 stopwords=None, random_state=None, background_color='black',
                 max_font_size=None, font_step=1, mode="RGB", relative_scaling=0, regexp=None)
'''



















'''
plt.imshow(wc)
plt.axis("off")
plt.figure()
'''










'''
from os import path
from wordcloud import WordCloud

d = path.dirname(__file__)

# Read the whole text.
text = open(path.join(d, 'constitution.txt')).read()

# Generate a word cloud image
wordcloud = WordCloud().generate(text)

# Display the generated image:
# the matplotlib way:
import matplotlib.pyplot as plt
plt.imshow(wordcloud)
plt.axis("off")

# take relative word frequencies into account, lower max_font_size
wordcloud = WordCloud(max_font_size=40, relative_scaling=.5).generate(text)
plt.figure()
plt.imshow(wordcloud)
plt.axis("off")
plt.show()
'''
