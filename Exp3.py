from facebook_scraper import get_posts
import pandas as pd
import warnings
warnings.filterwarnings("ignore")

fbPosts = []
for post in get_posts('nike', pages=10):
    fbPosts.append(post)
print(fbPosts)
df = pd.DataFrame(fbPosts)
df.info()
df = df[['post_id', 'text', 'post_url', 'page_id', 'comments', 'likes', 'time']]
print(df.isna())
print(f"Latest posts:\n {df}")
