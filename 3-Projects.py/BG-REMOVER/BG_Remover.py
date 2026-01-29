from rembg import remove
from PIL import Image
import io

input_path="/Users/tanishksharma/Desktop/Gemini_Generated_Image_gwhw4bgwhw4bgwhw.png"
output_path="/Users/tanishksharma/Desktop/remove.png"

# read the input file as bytes, remove the background, and save the result
with open(input_path, "rb") as f:
	input_bytes = f.read()

output_bytes = remove(input_bytes)

result = Image.open(io.BytesIO(output_bytes)).convert("RGBA")
result.save(output_path)


