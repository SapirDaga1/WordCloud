from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt    # to display our word cloud
from PIL import Image     # to load our image
import numpy as np     # to get the color of our image
from encodings import utf_8
from bidi.algorithm import get_display


# Content-related
text = open('textfile_rtl.txt', 'r', encoding="utf-8").read()
stopwords = set(STOPWORDS)

# Appearance-related
custom_mask = np.array(Image.open('cloud .png'))
wc = WordCloud(background_color='white', stopwords=stopwords,
               mask=custom_mask, font_path="SuezOne-Regular.ttf")

wc.generate(get_display(text))

#image_colors = ImageColorGenerator(custom_mask)
#wc.recolor(color_func= image_colors)

# Plotting

#plt.imshow(wc, interpolation='bilinear')
#plt.axis('off')
#plt.show()

wc.to_file('my_wordcloud.png')