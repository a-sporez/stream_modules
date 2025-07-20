local Button = require 'stuff.button'

function love.load()
    ExitButton = Button.new(
    100,
    100,
    96,
    32,
    "Exit",
    love.graphics.print("CLICK"))
end

-- loop
function love.update(dt)
end

function love.draw()
    local black = {0, 0, 0}
    local white = {1, 1, 1}

    local midX = love.graphics.getWidth() / 2
    local midY = love.graphics.getHeight() / 2

    love.graphics.setColor(white)
    ExitButton:draw()
end

function love.mousepressed(x, y, button, isTouch)
    if button == 1 then
        if ExitButton then
            ExitButton:checkPressed(x, y)
            print("[debug-main] mouse pressed")
        end
    end
end