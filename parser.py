
# coding: utf-8

# In[1]:


from lxml import html
import requests


# In[2]:


def parse_tweets( nickname , tweet_size):
    base_url = 'https://twitter.com/'
    url = base_url + nickname
    page = requests.get(url)
    tree = html.fromstring(page.content)
    tweets = tree.xpath('//p[@class="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text"]/text()')
    print(nickname + "Tweets")
    print("=======================")
    for num in range(0,tweet_size):
        print(str(num) + "--" +tweets[num])
    return tweets
    
    


# In[4]:


parse_tweets("google" , 3)


# In[5]:


parse_tweets("twitter",5)

