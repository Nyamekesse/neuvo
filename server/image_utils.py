import base64
import numpy as np
from io import BytesIO
from PIL import Image as PILImage


def generate_default_image(filename=None):
    # Define image dimensions
    width, height = 200, 200

    # Create a gradient image with random colors
    x = np.linspace(0, 1, width)
    y = np.linspace(0, 1, height)
    X, Y = np.meshgrid(x, y)
    R = np.random.uniform(0, 1, size=(height, width))
    G = np.random.uniform(0, 1, size=(height, width))
    B = np.random.uniform(0, 1, size=(height, width))
    img_data = np.dstack((R * X, G * Y, B))

    # Create a PIL Image object from the image data
    img = PILImage.fromarray(np.uint8(img_data * 255))

    # Convert the image to a byte stream
    with BytesIO() as buffer:
        img.save(buffer, format="JPEG")
        img_bytes = buffer.getvalue()

    # Convert the image byte stream to base64
    b64_string = base64.b64encode(img_bytes).decode("utf-8")

    # Save the image to a file if filename is specified
    if filename:
        with open(filename, "wb") as f:
            f.write(img_bytes)
    # print(b64_string)
    # Return the base64 string
    return b64_string
