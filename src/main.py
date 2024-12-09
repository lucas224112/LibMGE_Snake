import MGE
from random import randrange

MGE.init()

window = MGE.Window("LibMGE Snake", resolution=(500, 500), flags=0)
window.set_TitleBarColor(MGE.Color((30, 34, 38)))
window.set_BorderColor(None)

sizeOfSquare = 10
gameWidth, gameHeight = window.resolution[0]//sizeOfSquare, window.resolution[1]//sizeOfSquare

snake = [[gameHeight//2, gameWidth//2]]
direction = 0
apple = [randrange(gameHeight), randrange(gameWidth)]

timeGameLogic = MGE.Time(MGE.fps_to_time(10))

while True:
    MGE.update()
    window.update()
    window.title = f"LibMGE Snake | FPS: {int(window.frameRate)}"

    if MGE.QuitEvent() or MGE.keyboard(MGE.KeyboardButton.F1):
        exit()

    if MGE.keyboard(MGE.KeyboardButton.KeyW) or MGE.keyboard(MGE.KeyboardButton.Up):
        if not direction == 2:
            direction = 0
    if MGE.keyboard(MGE.KeyboardButton.KeyA) or MGE.keyboard(MGE.KeyboardButton.Left):
        if not direction == 1:
            direction = 3
    if MGE.keyboard(MGE.KeyboardButton.KeyS) or MGE.keyboard(MGE.KeyboardButton.Down):
        if not direction == 0:
            direction = 2
    if MGE.keyboard(MGE.KeyboardButton.KeyD) or MGE.keyboard(MGE.KeyboardButton.Right):
        if not direction == 3:
            direction = 1

    if timeGameLogic.tick(True):
        print(snake)
        if direction == 0:
            snake.insert(0, [snake[0][0] - 1, snake[0][1]])
        elif direction == 1:
            snake.insert(0, [snake[0][0], snake[0][1] + 1])
        elif direction == 2:
            snake.insert(0, [snake[0][0] + 1, snake[0][1]])
        elif direction == 3:
            snake.insert(0, [snake[0][0], snake[0][1] - 1])

        if snake[0][0] < 0 or snake[0][0] >= gameHeight or snake[0][1] < 0 or snake[0][1] >= gameWidth or snake.count([snake[0][0], snake[0][1]]) > 1:
            exit()

        if snake[0][0] == apple[0] and snake[0][1] == apple[1]:
            apple = [randrange(gameHeight), randrange(gameWidth)]
        else:
            snake.pop()

    window.clear(color=(20, 20, 26, 255))

    if "snake" not in window.drawnObjects:
        window.drawnObjects.append("snake")
        for snakePart in snake:
            window.drawSquare((snakePart[1] * sizeOfSquare, snakePart[0] * sizeOfSquare), (sizeOfSquare, sizeOfSquare), 0, 0, MGE.Colors.Green)

    if "apple" not in window.drawnObjects:
        window.drawnObjects.append("apple")
        window.drawSquare((apple[1] * sizeOfSquare, apple[0] * sizeOfSquare), (sizeOfSquare, sizeOfSquare), 0, 0, MGE.Colors.Red)
