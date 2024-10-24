import qrcode
from PIL import Image

class QrOperations:
    """
    This class was created to center all operations related to QR Code
    
    Operations:
    - Creation of personalized QR Code given an input
    - [Debug purpose] Reading of a QR Code checking if it works properly
    """

    def generating_qr(temp = "null"):
        # Create a QR code object with a larger size and higher error correction
        qr = qrcode.QRCode(version=3, box_size=20, border=10, error_correction=qrcode.constants.ERROR_CORRECT_H)

        # Define the data to be encoded in the QR code
        data = "https://medium.com/@rahulmallah785671/create-qr-code-by-using-python-2370d7bd9b8d"

        # Add the data to the QR code object
        qr.add_data(data)

        # Make the QR code
        qr.make(fit=True)

        # Create an image from the QR code with a black fill color and white background
        img = qr.make_image(fill_color="black", back_color="white")

        # Save the QR code image
        img.save("outputs/qr_code.png")

if __name__ == '__main__':
    
    qr = QrOperations()
    qr.generating_qr()

    pil_img = Image.open('outputs/qr_code.png', 'r')
    pil_img.show()