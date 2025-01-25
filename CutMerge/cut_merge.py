"""
Use this script to split a sprite sheet into individual frames.
Then use TexturePacker to pack the frames into a sprite sheet.
"""
import os
import glob
from PIL import Image


def guess_columns_rows(png_path: str) -> tuple:
    pass


def split_sprite_sheet(input_path: str, columns: int, rows: int, is_outline = True):
    aseprite_path = f"D:/Game/Steam/steamapps/common/Aseprite/Aseprite.exe"
    script = "Import And Outline.lua"
    command = f"{aseprite_path} -b {input_path} --script-param columns={columns} --script-param rows={rows} --script-param is_outline={is_outline} -script \"{script}\""
    print(command)
    os.system(command)


def pack_to_sprite_sheet():
    pass


def traverse_and_split(name_starts, width, height, is_outline = True):
    filenames = glob.glob(name_starts)
    for filename in filenames:
        image = Image.open(filename)
        image_width, image_height = image.size
        rows = image_height // height
        columns = image_width // width

        print(f"{filename} {columns}x{rows} {image.size}")
        split_sprite_sheet(f'"{filename}"', columns, rows, is_outline)


if __name__ == "__main__":
    # width = 64
    # height = 80
    # image = Image.open(filename)
    # image_width, image_height = image.size
    # rows = image_height // height
    # columns = image_width // width
    # columns = 4
    # rows = 2
    # print(f"{filename} {columns}x{rows}")
    # split_sprite_sheet(f'"{filename}"', columns, rows, True)
    # filename = "D:/Coding/Code/GodotProject/Raw Resources/Arena Survivor/Split Project/Large2/Large_Slime_Death.png"
    png_path = "D:/Coding/Code/GodotProject/Raw Resources/Arena Survivor/Split Project/Large Slime/*.png"
    traverse_and_split(png_path, 64, 80, False)