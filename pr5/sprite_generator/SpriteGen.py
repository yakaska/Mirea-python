import colorsys
import copy
import math
import random

import matplotlib.pyplot as plt
from PIL import Image


def make(
        mask,
        color_variations=0.2,
        colored=True,
        brightness_noise=0.3,
        edge_brightness=1.0,
        saturation=0.2,
        mirror=False
):
    new_mask = copy.deepcopy(mask)
    height = len(new_mask)
    width = len(new_mask[0])

    is_vertical_gradient = random.random() > 0.5
    saturation = max(min(random.random() * saturation, 1), 0)
    hue = random.random()

    new_mask = make_body(new_mask, width, height)

    if mirror:
        new_mask, width, height = mirror_body(new_mask)
    else:
        new_mask, width, height = mirror_body_small(new_mask)

    new_mask = make_edges(new_mask, width, height)
    new_mask = apply_colors(
        new_mask,
        color_variations,
        colored,
        brightness_noise,
        saturation,
        edge_brightness,
        hue,
        height,
        width
    )

    return to_image(new_mask)


def make_map(
        mask,
        color_variations=0.2,
        colored=True,
        brightness_noise=0.3,
        edge_brightness=0.3,
        saturation=0.2,
        mirror=False,
        n=200,
        nr_columns=20
):
    images = [make(mask, color_variations, colored, brightness_noise, edge_brightness, saturation, mirror)
              for _ in range(n)]

    space = 6

    background_width = ((len(mask[0]) if not mirror else len(mask[0]) * 2) * nr_columns) + (nr_columns * space)
    background_height = int(len(mask) * n / nr_columns) + int(n / nr_columns * space)
    background = Image.new('RGB', (background_width, background_height), (255, 255, 255, 255))
    offset = [0, 0]

    for index, image in enumerate(images):
        img_w, img_h = image.size

        if index % nr_columns == 0:
            offset[1] += img_h + space
            offset[0] = 0

        background.paste(image, tuple(offset))
        offset[0] += img_w + space

    return background


def make_body(mask, width, height):
    for x in range(width):
        for y in range(height):
            if mask[y][x] == 1:
                mask[y][x] = round(random.random() > 0.5)
            elif mask[y][x] == 2:
                if random.random() > 0.5:
                    mask[y][x] = 1
                else:
                    mask[y][x] = -1

    return mask


# отзеркаливание спрайта
def mirror_body(mask):
    for i in range(len(mask)):
        mask[i].extend(mask[i][1::-1])
    height = len(mask)
    width = len(mask[0])
    return mask, width, height


def mirror_body_small(mask):
    for i in range(len(mask)):
        mask[i].extend(mask[i][1::-1])
    height = len(mask)
    width = len(mask[0])
    return mask, 5, 5


# установка четырех границ
def make_edges(mask, width, height):
    for x in range(width):
        for y in range(height):
            if mask[y][x] == 1:
                if x - 1 >= 0 and mask[y][x - 1] == 0:
                    mask[y][x - 1] = -1
                if x + 1 < width and mask[y][x + 1] == 0:
                    mask[y][x + 1] = -1
                if y - 1 >= 0 and mask[y - 1][x] == 0:
                    mask[y - 1][x] = -1
                if y + 1 < height and mask[y + 1][x] == 0:
                    mask[y + 1][x] = -1

    return mask


def apply_colors(
        mask,
        color_variations,
        colored,
        brightness_noise,
        saturation,
        edge_brightness,
        hue,
        height,
        width
):
    ulen = height
    vlen = width

    for u in range(ulen):
        is_new_color = abs((random.random() * 2 - 1)
                           + (random.random() * 2 - 1)
                           + (random.random() * 2 - 1)) / 3

        if is_new_color > (1 - color_variations):
            hue = random.random()  # оттенок

        for v in range(vlen):

            val = mask[u][v]

            rgb = {"r": 1, "g": 1, "b": 1}

            if val != 0:
                if colored:
                    brightness = (math.sin((u / ulen) * math.pi) *
                                  (1 - brightness_noise) + random.random() * brightness_noise)
                    rgb_vals = colorsys.hls_to_rgb(hue, brightness, saturation)
                    rgb['r'] = rgb_vals[0]
                    rgb['g'] = rgb_vals[1]
                    rgb['b'] = rgb_vals[2]

                    if val == -1:
                        rgb['r'] *= edge_brightness
                        rgb['g'] *= edge_brightness
                        rgb['b'] *= edge_brightness

                else:
                    if val == -1:
                        rgb = {"r": 0, "g": 0, "b": 0}

            mask[u][v] = (round(rgb['r'] * 255),
                          round(rgb['g'] * 255),
                          round(rgb['b'] * 255))

    return mask


def to_image(mask):
    width, height = len(mask[0]), len(mask)
    data = sum(mask, [])

    im = Image.new('RGB', (width, height), 1)
    im.putdata(data)
    return im


# http://web.archive.org/web/20080228054410/http://www.davebollinger.com/works/pixelspaceships/
# http://web.archive.org/web/20080228054405/http://www.davebollinger.com/works/pixelrobots/
if __name__ == '__main__':
    robot = [
        [0, 0, 0, 0],
        [0, 1, 1, 1],
        [0, 1, 2, 2],
        [0, 0, 1, 2],
        [0, 0, 0, 2],
        [1, 1, 1, 2],
        [0, 1, 1, 2],
        [0, 0, 0, 2],
        [0, 0, 0, 2],
        [0, 1, 2, 2],
        [1, 1, 0, 0]
    ]

    sprite = make_map(robot,
                      color_variations=0.95,
                      brightness_noise=0.0,
                      edge_brightness=0.1,
                      saturation=0.5,
                      colored=True,
                      mirror=True,
                      n=80,
                      nr_columns=20)
    sprite.resize((sprite.size[0] * 2, sprite.size[1] * 2))
    plt.imshow(sprite)
    plt.show()
