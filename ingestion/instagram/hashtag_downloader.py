from instagrapi import Client
import pandas as pd
import time
import warnings
from pandas import json_normalize
warnings.filterwarnings('ignore')
import argparse
import hashlib
import json

parser = argparse.ArgumentParser()

parser.add_argument('--u', type=str, required=True)
parser.add_argument('--p', type=str, required=True)
parser.add_argument('--posts', type=int, required=True)
parser.add_argument('--keyword', type=str, required=True)
parser.add_argument('--type', type=str, required=True, help='recent or top', default='top')
parser.add_argument('--cursor', type=str, default=None)

args = parser.parse_args()

cl = Client()
cl.login(args.u, args.p)

key_map = json.loads(open("insta_duplicate_map.txt", "r").read())
print(len(key_map))

insta_hash_keys = ['pk',
 'id',
 'code',
 'taken_at',
 'location',
 'user',
 'caption_text',
 'accessibility_caption',
 'view_count',
 'title']

def save_posts(insta_posts):
    try:
        insta_posts_hashtag = pd.concat([insta_posts, json_normalize(insta_posts['location'])], axis=1).drop(['location'], axis=1)
        insta_posts_hashtag.to_csv("insta_hashtags_"+str(int(time.time()))+".csv", index=False)
    except:
        pass

def fetch_from_cursor(cursor, request_limit, hash_keyword, post_type, maxPosts):
    
    total_posts_done = 0
    df_geo_hashtags = pd.DataFrame()
    
    while maxPosts > 0:
        
        hash_medias, cursor = cl.hashtag_medias_v1_chunk(hash_keyword, max_amount=request_limit, tab_key=post_type, max_id = cursor)      
        for i in range(len(hash_medias)):

            row = hash_medias[i].dict()
            caption_hash = hashlib.md5(row['caption_text'].encode()).hexdigest()
            
            if caption_hash not in key_map:
                key_map[caption_hash] = 1
                
                try:
                    if row['location']['lat'] != None and row['location']['lng'] != None:
                        df_row = pd.DataFrame.from_dict(
                            {k: row[k] for k in insta_hash_keys}, orient='index'
                            ).transpose()
                        df_geo_hashtags = df_geo_hashtags.append(df_row)

                except:
                    pass

        if total_posts_done == df_geo_hashtags.shape[0]:
            print("No unique posts available")
            
            with open("insta_duplicate_map.txt", "w") as text_file:
                text_file.write(json.dumps(key_map))
            
            break
        else:
            total_posts_done = df_geo_hashtags.shape[0]
        
        maxPosts = maxPosts - request_limit
        print("Posts Downloaded: ", total_posts_done)
        
        with open("insta_hash_cursor.txt", "w") as text_file:
            text_file.write(cursor)
        
        save_posts(df_geo_hashtags.reset_index().drop(['index'], axis=1))
        
        with open("insta_duplicate_map.txt", "w") as text_file:
            text_file.write(json.dumps(key_map))

        time.sleep(10)
    
    print("Saved Cursor: ",cursor)

maxPosts = args.posts
cursor = args.cursor
hash_keyword = args.keyword
request_limit = 30 #minimum 30
post_type = args.type

print("Starting Download...")
fetch_from_cursor(cursor, request_limit, hash_keyword, post_type, maxPosts)
