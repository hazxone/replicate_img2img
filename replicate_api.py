import replicate
from PIL import Image

image = Image.open("balloon.jpg", "rb")

output = replicate.run(
    "hazxone/img2img-vg:76b7599585142940646d43cdaa259aa530d95fc270dbc1374d987ecab71469fb",
    input={"prompt": "lvngvncnt, a kid holding a balloon", "image": image}
)

print(output)
