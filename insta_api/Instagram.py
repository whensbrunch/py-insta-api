# use InstagramAPI
# import InstagramAPI
#
# ia = InstagramAPI()

# directly query the API
import requests
from requests_toolbelt import MultipartEncoder
import yaml


# Authentication + Authorization

# Scope options
# :basic - to read a user’s profile info and media
# :public_content - to read any public profile info and media on a user’s behalf
# :follower_list - to read the list of followers and followed-by users
# :comments - to post and delete comments on a user’s behalf
# :relationships - to follow and unfollow accounts on a user’s behalf likes

# Nowww they tell me I need to re-authorize with scope=public_content :tina_fey_eyeroll:
# Generating an access token for Instagram: http://dmolsen.com/2013/04/05/generating-access-tokens-for-instagram/
# Step 1: Direct user to our authorization URL / paste this url in your browser
with open("credentials.yaml", 'r') as stream:
    credentials = yaml.load(stream)
# url = 'https://api.instagram.com/oauth/authorize/?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code&scope={scope}'.format(
#     client_id = credentials.get('client_id'),
#     redirect_uri = credentials.get('redirect_uri'),
#     scope = credentials.get('scope')
# )
# print(url)
# r = requests.get(url)
# print(r.status_code)
# print(r.text) # looks like I need to log in first

# [USE THIS ] Use this multipart encoder to get access_token using code
# url = 'https://api.instagram.com/oauth/access_token'
# m = MultipartEncoder(
#     fields = {
#         'client_id': credentials.get('client_id'),
#         'client_secret': credentials.get('client_secret'),
#         'grant_type': 'authorization_code',
#         'redirect_uri': credentials.get('redirect_uri'),
#         'code': credentials.get('code')
#     }
# )
# r = requests.post(url, data=m, headers={'Content-Type': m.content_type})
# print(r.status_code)
# print(r.text)

# Step 2: Receive the redirect from Instagram


url = 'https://api.instagram.com/v1/users/self/?access_token={ACCESS_TOKEN}'.format(ACCESS_TOKEN = credentials.get('access_token'))
print(url)
r = requests.get(url)
print(r.status_code)
print(r.text)

# example of how to pull info on tags
# url = 'https://api.instagram.com/v1/tags/{tag_name}?access_token={ACCESS_TOKEN}'.format(
#     ACCESS_TOKEN = credentials.get('access_token'),
#     tag_name = 'calisthenics'
# )
# r = requests.get(url)
# print(r.status_code)
# print(r.text)

def tag_info(tag_name):
    url = 'https://api.instagram.com/v1/tags/{tag_name}?access_token={access_token}'.format(
        access_token = credentials.get('access_token'),
        tag_name = tag_name
    )
    r = requests.get(url)
    print(r.status_code)
    print(r.text)

def recent_media(tag_name):
    '''Get a list of recently tagged media.'''
    url = 'https://api.instagram.com/v1/tags/{tag_name}/media/recent?access_token={access_token}'.format(
        access_token = credentials.get('access_token'),
        tag_name = tag_name
    )
    r = requests.get(url)
    print(r.status_code)
    print(r.text)

def tag_search(tag_name):
    url = 'https://api.instagram.com/v1/tags/search?q={tag_name}&access_token={access_token}'.format(
        access_token=credentials.get('access_token'),
        tag_name=tag_name
    )
    r = requests.get(url)
    print(r.status_code)
    print(r.text)


def follows():
    '''Get the list of users this user follows.'''
    url = 'https://api.instagram.com/v1/users/self/follows?access_token={access_token}'.format(
        access_token = credentials.get('access_token')
    )
    r = requests.get(url)
    print(r.status_code)
    print(r.text)

url = 'https://api.instagram.com/v1/users/self/followed-by?access_token={access_token}'.format(
        access_token = credentials.get('access_token')
    )
r = requests.get(url)
print(r.text)

if __name__ == '__main__':
    print('Getting a list of the users you follow...')
    follows()
    tag_info('calisthenics')
    tag_search('calisthenics')
    recent_media('calisthenics')

