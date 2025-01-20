function to_boolean(input)
    if input == "true" then
        return true
    elseif input == "false" then
        return false
    else
        return nil
    end
end

-- split_sprite_sheet_with_args.lua
local sprite = app.activeSprite

-- 检查是否有打开的精灵
if not sprite then
  app.alert("没有打开的 Sprite 文件！")
  return
end

-- 从 CLI 获取参数
local rows = tonumber(app.params["rows"])
local columns = tonumber(app.params["columns"])
local is_outline = to_boolean(app.params["is_outline"]) or true
-- local rows = 1
-- local columns = 4

if not rows or not columns then
  print("please provide 'rows' and 'columns' arguments")
  return
end

-- 检查图片尺寸是否能被均匀切分
local spriteWidth = sprite.width
local spriteHeight = sprite.height

local frameWidth = spriteWidth // columns
local frameHeight = spriteHeight // rows

if spriteWidth % columns ~= 0 or spriteHeight % rows ~= 0 then
  print("the sprite cannot be evenly split into the specified rows and columns")
  return
end
 -- import sprite sheet and generate animations
app.command.ImportSpriteSheet{
  ui=false,
  type=SpriteSheetType.ROWS,
  frameBounds=Rectangle(0, 0, frameWidth, frameHeight)
}
-- add outline
for i, frame in ipairs(app.sprite.frames) do
  app.frame = frame
  app.command.Outline {
    ui=false,
    color= Color{r = 0, g = 0, b = 0, a = 255},
  }
end
-- export frame to png
local outputPath = app.fs.filePathAndTitle(app.sprite.filename) .. ".png"
print(outputPath)
app.sprite:saveAs(outputPath)

print("Successfully split the sprite sheet into frames")
