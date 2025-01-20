"""
Use this script to split a sprite sheet into individual frames.
Then use TexturePacker to pack the frames into a sprite sheet.
"""
import os


def guess_columns_rows(png_path: str) -> tuple:
    pass


def split_sprite_sheet(png_path: str, columns: int, rows: int):
    pass


def pack_to_sprite_sheet():
    pass


if __name__ == "__main__":
    png_path = "\"D:/Coding/Code/GodotProject/Raw Resources/Arena Survivor/enemies/BOSS/Large_Slime_Idle.png\""
    aseprite_path = f"D:/Game/Steam/steamapps/common/Aseprite/Aseprite.exe"
    script = "Import And Outline.lua"
    columns = 4
    rows = 1
    command = f"{aseprite_path} -b {png_path} --script-param columns={columns} --script-param rows={rows} -script \"{script}\""
    print(command)
    os.system(command)