from random import randint
import os
from PIL import Image, ImageDraw


def circles_generator(num_of_circles=100):
    if not os.path.exists('circles'):
        os.mkdir('circles')
    for i in range(num_of_circles):
        im = Image.new('RGB', (600, 600), (128, 128, 128))
        draw = ImageDraw.Draw(im)
        draw.ellipse((0, 0, 600, 600), fill=(randint(0, 128), randint(0, 128), randint(0, 128)))
        im.save(f'circles/{i + 1}.jpg')
    print("Process ended successfully!")


def main():
    circles_generator()


if __name__ == "__main__":
    main()
