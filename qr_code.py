import qrcode

def convert(text):

    qr=qrcode.QRCode(
        version=1,
        error_correction=qrcode.ERROR_CORRECT_L,
        box_size=15,
        border=5,
    )

    qr.add_data(text)
    qr.make(fit=True)

    img=qr.make_image(fill_color='black',back_color='white')
    img.save('image.png')

convert('www.youtube.com')