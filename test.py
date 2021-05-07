import requests
url = "http://localhost:8000/search/"
files = {
    "tn":"pc",
    "image":("test.jpg",open('test.jpg','rb'),"image/jpeg"),
    "from":"pc",
    "image_source":"PC_UPLOAD_SEARCH_FILE",
    "range":'{"page_from": "searchIndex"}'
}
r = requests.post(url, files=files)
print(r)