import requests
import base64
import os

url = "http://localhost:8000/search/"

image_path = os.path.join(os.path.dirname(__file__))+'/test.jpg'
with open(image_path, 'rb') as f:
    imgData = base64.b64encode(f.read())

files = {
    "tn":"pc.jpg",
    "image": imgData,
    "from":"pc",
    "image_source":"PC_UPLOAD_SEARCH_FILE",
    "range":'{"page_from": "searchIndex"}'
}
r = requests.post(url, files=files)
print(r)