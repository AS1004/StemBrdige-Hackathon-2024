
TILE_SIZE = 121
WIDTH = TILE_SIZE * 11
HEIGHT = TILE_SIZE * 11

tiles = ["empty", "wall", "goal", "treasure chest", "key", "enemy", "fire", "water"]
unlock = 0
points = 0
lives = 3

maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 2, 0, 1, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1],
    [1, 7, 1, 0, 6, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 1, 0, 6, 1],
    [1, 0, 1, 4, 0, 0, 0, 1, 0, 0, 1],
    [1, 5, 1, 5, 7, 0, 3, 1, 0, 0, 1],
    [1, 0, 0, 0, 5, 0, 0, 0, 5, 0, 1],
    [1, 5, 0, 0, 7, 0, 5, 0, 0, 0, 1],
    [1, 0, 0, 5, 0, 0, 0, 5, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],

]

Hero = input("What is your name? ")

print("Welcome " + Hero + "! While exploring the universe, you have mysteriously been teleported to a new world. To escape these new surroundings, you must escape through this maze. You may use the arrow keys to move. Watch out, there are enemies and other obstacles hidden in the maze. Good luck " + Hero + ", and may the odds ever be in your favor.")

player = Actor("player", anchor=(0, 0), pos=(1 * TILE_SIZE, 1 * TILE_SIZE))
enemy = Actor("enemy", anchor=(0, 0), pos=(3 * TILE_SIZE, 6 * TILE_SIZE))
enemy.yv = -1

def draw():
    screen.clear()
    for row in range(len(maze)):
        for column in range(len(maze[row])):
            x = column*TILE_SIZE
            y = row*TILE_SIZE
            tile = tiles[maze[row][column]]
            screen.blit(tile, (x, y))

    player.draw()
    enemy.draw()

def on_key_down(key):
    row = int(player.y/TILE_SIZE)
    column = int(player.x/TILE_SIZE)
    # points = 0
    # lives = 3
    if key == keys.UP:
        row = row-1
    if key == keys.DOWN:
        row = row+1
    if key == keys.LEFT:
        column = column-1
    if key == keys.RIGHT:
        column = column+1
    tile = tiles[maze[row][column]]
    if tile == "empty":
        x = column * TILE_SIZE
        y = row * TILE_SIZE
        animate(player, duration=0.1, pos=(x, y))
    global lives
    global points
    if tile == "enemy":
        print("Uh Oh, You Lost A Life!")
        lives -= 1
        maze[row][column] = 0
    global unlock
    if tile == 'key':
        unlock = unlock + 1
        maze[row][column] = 0
    elif tile == 'treasure chest' and unlock > 0:
        unlock = unlock - 1
        points += 5
        maze[row][column] = 0
    elif tile == 'water':
        print("The Water Healed You! You Gained A Life!")
        lives += 1
        maze[row][column] = 0
    elif tile == 'fire':
        lives -= 1
        print("You Got Burned By The Fire! You Lose A Life!")
        maze[row][column] = 0
    elif lives == 0:
        print("Uh Oh! You have no lives left! Game Over!")
        exit()
    if tile == "goal":
        points += 10
        print("Excellent Job Hero! You Win! You had " + str(lives) + " life/lives remaining and you gained " + str(points) + " points!")
        exit()


