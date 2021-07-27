import requests
import base64
import os



# image_path = os.path.join(os.path.dirname(__file__))+'test.jpg'
# image_path = "C:\\Users\\46222\\Documents\\Django_learning-main\\Django_learning-main\\test.jpg"
# with open(image_path, 'rb') as f:
#     imgData = base64.b64encode(f.read())


url = "https://bitxiaoyk.cn:8000/"
#关键字key在前，需要传输的变量在后
files = {
    "name": "pc.name",
    "id": "pc.id",
    "class": "pc.class",
    "account": "pc.account",
    "image": "pc.jpg",
}
#    "image_source":"PC_UPLOAD_SEARCH_FILE",
#    "range":'{"page_from": "searchIndex"}'
r = requests.post(url, files=files, verify = False)
print(r)