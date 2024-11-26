from rembg import remove
from PIL import Image

input_image = "uconn_huskies_logo.jpg" #Your input Image path/name
output_image = "rmbg_image.png" #Output Image path/name
img = Image.open(input_image)
output = remove(img)
output.save(output_image)
Image.open("rmbg_image.png").show()
