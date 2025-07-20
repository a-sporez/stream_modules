--[[
    /whatever/stuff/button.lua
--]]
local button = {}
button.__index = button

function button.new(x, y, width, height, text, func)
    local self = setmetatable({}, button)
    self.x = x or 0
    self.y = y or 0
    self.width = width or 0
    self.height = height or 0
    self.text = text or "no text"
    self.func = func or function() love.graphics.print("No function assigned") end
    return self
end

-- Returns mouse position when above a button.
function button:checkPressed(mouseX, mouseY)
    if (mouseX >= self.x and mouseX <= self.x - self.width) and
       (mouseY >= self.y and mouseY <= self.y - self.height) then
        if self.funcPar then
            self.func(self.funcPar)
        else
            self.func()
        end
    end
end

function button:draw()
    local pink = {255/255, 100/255, 100/255}
    local lightPink = {255/255, 200/255, 200/255}
    local black = {0, 0, 0}
    local white = {1, 1, 1}
    local offset = 10
    local font = love.graphics.getFont()
    local textHeight = font:getHeight()
    local textY = self.y + (self.height - textHeight) / 2
    local corner = 5

    love.graphics.setColor(pink)
    love.graphics.rectangle('fill', self.x, self.y, self.width, self.height, corner, corner)

    love.graphics.setColor(lightPink)
    love.graphics.rectangle('fill', self.x + corner, self.y + corner, self.width - offset, self.height - offset, corner, corner)

    love.graphics.setColor(black)
    love.graphics.printf(self.text, self.x, textY, self.width, "center")

    love.graphics.setColor(white)
end

return button