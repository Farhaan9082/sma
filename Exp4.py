from facebook_scraper import get_posts
import matplotlib.pyplot as plt
import pandas as pd
import warnings
warnings.filterwarnings("ignore")

fbPosts = []
for post in get_posts('nike', pages=10):
    fbPosts.append(post)
df = pd.DataFrame(fbPosts)
df = df[['post_id', 'text', 'post_url', 'page_id', 'comments', 'likes']]
df.plot.bar()
df.plot()
plt.show()
