from facebook_scraper import get_posts
import pandas as pd
import warnings
warnings.filterwarnings("ignore")

fbPosts = []
for post in get_posts('nike', pages=10):
    fbPosts.append({x: post[x] for x in ['post_id', 'text', 'likes']})
print(f"Latest Facebook Posts:\n {pd.DataFrame(fbPosts)}")
