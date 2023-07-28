import replicate
from PIL import Image

image = Image.open("imgs/man_1.jpg.jpg", "rb")

output = replicate.run(
    "hazxone/img2img-vg:3edc1fecc293d8c88657d5442ece7857f907bc50b451e0603c7981c240f6a94d",
    input={"prompt": "portrait of a man in the style of vangh", "image": image}
)

print(output)
