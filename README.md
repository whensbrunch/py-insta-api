# Insta API

An exploration of the Instagram API through python!
I'll probably try to pull basic stats on my pics and
check out if it's feasible to figure out which likes / follows
came from which hashtags.

The official Instagram API is v boring. You can only play with users in the sandbox. We need a backdoor.

## Installing

```
pip3 install -r requirements.txt
```

Get your access token by following the guide [here](http://dmolsen.com/2013/04/05/generating-access-tokens-for-instagram/).

## Like this tool?
Please consider donating!

## Useful tips
http://httpbin.org/ will return the layout of the HTTP request sent to it.
I used it to determine how to convert the curl -F command recommended by Instagram to
the *requests* package.

Look! Here's an example:

```python
url = 'http://httpbin.org/post'
r = requests.post(url)
print(r.text)
```

Easy, right? Here's what we get:
```
{
  "args": {},
  "data": "",
  "files": {},
  "form": {},
  "headers": {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Connection": "close",
    "Content-Length": "0",
    "Host": "httpbin.org",
    "User-Agent": "python-requests/2.18.4"
  },
  "json": null,
  "origin": "190.18.163.200",
  "url": "http://httpbin.org/post"
}
```

Super helpful for seeing what form your request is actually taking.

## Authors

* **David Stevens** - *all work*

# To-Do
Figure out how to get access_token through python
Say thanks project

# Resources

[Unofficial Insta API](https://github.com/LevPasha/Instagram-API-python)

- No access_tokens, just username and password!