from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator

dryer_coloring = np.array(Image.open("file_path"))

# 通过mask参数来设置词云形状
wc = WordCloud(background_color="white", max_words=2000, mask=dryer_coloring,max_font_size=40, random_state=42)
# generate word cloud
wc.generate(str(filtered_words))

# create coloring from image
image_colors = ImageColorGenerator(dryer_coloring)

# show
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.figure()