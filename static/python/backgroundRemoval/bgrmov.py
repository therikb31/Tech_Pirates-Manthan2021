import requests

response = requests.post(
    'https://api.remove.bg/v1.0/removebg',
    files={'image_file': open('./static/python/backgroundRemoval/input/image1.jpeg', 'rb')},
    data={'size': 'auto'},
    headers={'X-Api-Key': 'KTPgYHvZcChaga3nnmqs94vc'},
)
if response.status_code == requests.codes.ok:
    with open('./static/python/backgroundRemoval/output/no-bg.png', 'wb') as out:
        out.write(response.content)
else:
    print("Error:", response.status_code, response.text)