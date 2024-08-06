import requests
import json
import cv2 as cv
from PIL import Image
filename='C:/Users/Admin/Desktop/list.jpg'
api_key='K85584476188957'
image = Image.open(filename)
image.save(filename,quality=15,optimize=True)

payload = {'isOverlayRequired': True,
               'apikey': api_key,
               'language': 'eng',
               'OCRENGINE': 5,
               }
with open(filename, 'rb') as f:
    r = requests.post('https://api.ocr.space/parse/image',
                      files={filename: f},
                      data=payload,
                          )
p=r.content.decode()
data=json.loads(p)

total=['total amount','total','bill','due','total amount:','total amount :']
staticZero = 0
itemCost_item = [0]
initText = data['ParsedResults'][staticZero]['ParsedText']
flag=False
for index, line in enumerate(data['ParsedResults'][staticZero]['TextOverlay']['Lines']):
    stri = data['ParsedResults'][staticZero]['TextOverlay']['Lines'][index]['Words'][staticZero]['WordText']
    chars = set('0123456789$,.')
    if 'LineText' in line:
        t=line['LineText'].split('/n')
        if flag==True:
            if all((c in chars) for c in t[0]):
                if ',' in t[0]:
                    t[0]=t[0].replace(',','')
                itemCost_item.append(float(t[0]))
                flag=False
            else:
                flag=True
        if t[0].lower() in total:
            flag=True
print(max(itemCost_item))

