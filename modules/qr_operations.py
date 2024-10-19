class QrOperations:
    """
    This class was created to center all operations related to QR Code
    
    Operations:
    - Creation of personalized QR Code given an input
    - [Debug purpose] Reading of a QR Code checking if it works properly

    Parameters:
    first_name  (str): The first name of the person.
    last_name   (str): The last name of the person.
    personal_id (str): The last 5 characters of the CPF.

    Output:
    - QR Code, used to redirect who scan it to an API that will check if the inputs are present in the database.  

    """

import qrcode

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
img.save("qr_code.png")