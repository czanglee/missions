from pyzbar.pyzbar import decode
from PIL import Image
import requests

url="http://gynvael.coldwind.pl/qrmaze/"
fileName = "e:\python\\"
fn = "start"
ext = '.png'

while fn != '':
    req = requests.get(''.join([url, fn, ext]))
    file = open(''.join([fileName, fn, ext]), 'wb')
    for chunk in req.iter_content(100000):
        file.write(chunk)
    file.close()

    qrData = decode(Image.open(''.join([fileName, fn, ext])))
    item = qrData[0][0].decode("utf-8")
    fn = ''
    if "Calc value, add .png, repeat: " in item:
        x = item[30:].split(',')
        print(x)
        value = x[0].__str__()
        for a in x[1:]:
            tmp = ''.join([value, a])
            value = eval(tmp).__str__()
        print(value)
        fn = ''.join(value)
    else:
        print(item)



#http://gynvael.coldwind.pl/qrmaze/69129246053.png