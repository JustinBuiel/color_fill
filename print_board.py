from PIL import Image, ImageDraw

color_codes = {
    'white': (255, 255, 255),
    'red': (255, 0, 0),
    'blue': (0, 0, 255),
    'orange': (255, 165, 0),
    'yellow': (255, 255, 0),
    'black': (0, 0, 0),
}


def create_image(board):
    im = Image.new('RGB', (500, 500), (128, 128, 128))
    draw = ImageDraw.Draw(im)

    coords = [0, 0, 50, 50]

    for row in board:
        for i in range(len(row)):
            draw.rectangle(coords, fill=color_codes[row[i]])
            coords[0] += 50
            coords[2] += 50
        coords[0] = 0
        coords[1] += 50
        coords[2] = 50
        coords[3] += 50

    im.save('board.png')
