from PIL import Image
import os

def crop_center(img):
    width, height = img.size
    length = min(width, height)
    left = (width - length) / 2
    top = (height - length) / 2
    right = (width + length) / 2
    bottom = (height + length) / 2
    return img.crop((left, top, right, bottom))

def process_images(folder_path):
    index = 1
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(folder_path, filename)
            with Image.open(image_path) as img:
                grayscale = img.convert('L')
                cropped = crop_center(grayscale)
                resized = cropped.resize((32, 32), Image.ANTIALIAS)
                output_path = os.path.join(folder_path, f"{index}.jpg")
                resized.save(output_path)
            index += 1

folder_path = './selfish'  # 替换为你的文件夹路径
process_images(folder_path)
