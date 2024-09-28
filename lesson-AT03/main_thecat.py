import requests


def get_cat_image():
    url = 'https://api.thecatapi.com/v1/images/search'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        image_url = data[0]['url']
        return requests.get(image_url).content
    else:
        return None


image = get_cat_image()
with open('cat.jpg', 'wb') as f:
    f.write(image)

