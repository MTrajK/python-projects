from graphics import *
import random


def main():
    win = GraphWin('Puzzle 15', 420, 450)
    win.setBackground(color_rgb(224, 224, 224))

    create_menu(win)
    

def create_menu(win):
    button_y_size = 80
    button_x = (125, 295)
    button_color = color_rgb(30, 136, 229)
    button_text_color = 'white'
    button_font = 20

    label_select = Text(Point(210, 50), 'SELECT GAME MODE')
    label_select.setSize(button_font)
    label_select.setTextColor(button_color)
    label_select.draw(win)

    button_easy_y = 105
    button_easy = Rectangle(
        Point(button_x[0], button_easy_y), 
        Point(button_x[1], button_easy_y + button_y_size)
    )
    button_easy.setFill(button_color)
    button_easy.draw(win)
    label_easy = Text(Point(210, 145), 'EASY')
    label_easy.setSize(button_font)
    label_easy.setTextColor(button_text_color)
    label_easy.draw(win)

    button_medium_y = 210
    button_medium = Rectangle(
        Point(button_x[0], button_medium_y), 
        Point(button_x[1], button_medium_y + button_y_size)
    )
    button_medium.setFill(button_color)
    button_medium.draw(win)
    label_medium = Text(Point(210, 250), 'MEDIUM')
    label_medium.setSize(button_font)
    label_medium.setTextColor(button_text_color)
    label_medium.draw(win)

    button_hard_y = 315
    button_hard = Rectangle(
        Point(button_x[0], button_hard_y), 
        Point(button_x[1], button_hard_y + button_y_size)
    )
    button_hard.setFill(button_color)
    button_hard.draw(win)
    label_hard = Text(Point(210, 355), 'HARD')
    label_hard.setSize(button_font)
    label_hard.setTextColor(button_text_color)
    label_hard.draw(win)

    random_moves = 0

    while True:
        pointer = win.getMouse()
        pointer_x = pointer.getX()
        pointer_y = pointer.getY()

        if (pointer_x < button_x[0]) or (pointer_x > button_x[1]):
            continue
        
        if pointer_y < button_easy_y:
            continue
        
        if pointer_y <= button_easy_y + button_y_size:
            random_moves = 20
            break

        if pointer_y < button_medium_y:
            continue
        
        if pointer_y <= button_medium_y + button_y_size:
            random_moves = 50
            break
        
        if pointer_y < button_hard_y:
            continue
        
        if pointer_y <= button_hard_y + button_y_size:
            random_moves = 100
            break

    label_select.undraw()
    button_easy.undraw()
    label_easy.undraw()
    button_medium.undraw()
    label_medium.undraw()
    button_hard.undraw()
    label_hard.undraw()

    create_game(win, random_moves)


def move(table, empty, move):
    changed = None

    if move == 0:
        if empty[0] != 0:
            changed = (-1, 0)
    elif move == 1:
        if empty[1] != 3:
            changed = (0, 1)
    elif move == 2:
        if empty[0] != 3:
            changed = (1, 0)
    elif move == 3:
        if empty[1] != 0:
            changed = (0, -1)

    if changed != None:
        x, y = empty
        changed = (empty[0] + changed[0], empty[1] + changed[1])
        changed_x, changed_y = changed

        temp = table[x][y]
        table[x][y] = table[changed_x][changed_y]
        table[changed_x][changed_y] = temp

    return changed


def create_game(win, random_moves):
    table = [[(i + j) for j in range(1, 5)] for i in range(0, 16, 4)]

    empty = (3, 3)
    table[empty[0]][empty[1]] = None

    # randomize tiles
    i = 0
    while i < random_moves:
        rand = random.randint(0,3)

        changed = move(table, empty, rand)

        if changed != None:
            empty = changed
            i += 1

    texts = []
    tiles = []
    tile_color = color_rgb(30, 136, 229)
    text_color = 'white'
    font = 25

    label_moves = Text(Point(225, 35), 'TOTAL MOVES: 0')
    label_moves.setSize(20)
    label_moves.setTextColor(tile_color)
    label_moves.draw(win)

    # draw tiles
    for i in range(4):
        texts.append([])
        tiles.append([])

        for j in range(4):
            x_start = 40 + j * 90
            y_start = 70 + i * 90

            temp_text = Text(Point(x_start + 40, y_start + 40), '')
            temp_text.setSize(font)
            temp_text.setTextColor(text_color)

            temp_tile = Rectangle(
                Point(x_start, y_start), 
                Point(x_start + 80, y_start + 80)
            )
            temp_tile.setFill(tile_color)

            if table[i][j] != None:
                temp_text.setText(str(table[i][j]))
                temp_tile.draw(win)
                temp_text.draw(win)

            texts[i].append(temp_text)
            tiles[i].append(temp_tile)
    
    map_moves = {
        'Up': 0,
        'Right': 1,
        'Down': 2,
        'Left': 3
    }

    total_moves = 0

    # user move tile
    while True:
        key = win.getKey()

        if key in map_moves:
            changed = move(table, empty, map_moves[key])

            if changed != None:
                total_moves += 1
                label_moves.setText('TOTAL MOVES: {0}'.format(total_moves))

                new_empty = changed
                
                texts[new_empty[0]][new_empty[1]].undraw()
                tiles[new_empty[0]][new_empty[1]].undraw()

                texts[empty[0]][empty[1]].setText(str(table[empty[0]][empty[1]]))
                tiles[empty[0]][empty[1]].draw(win)
                texts[empty[0]][empty[1]].draw(win)
                
                empty = new_empty

                completed = True

                # check if completed
                for i in range(15):
                    if table[i // 4][i % 4] != (i + 1):
                        completed = False
                        break
                
                if completed:
                    label_moves.undraw()

                    for ts in texts:
                        for t in ts:
                            t.undraw()
                    
                    for ts in tiles:
                        for t in ts:
                            t.undraw()

                    break
    
    create_end(win, total_moves)


def create_end(win, total_moves):
    button_y_size = 80
    button_x = (125, 295)
    button_color = color_rgb(30, 136, 229)
    button_text_color = 'white'
    button_font = 20

    label_congratulations = Text(Point(210, 80), 'CONGRATULATIONS!!!')
    label_congratulations.setSize(button_font)
    label_congratulations.setTextColor(button_color)
    label_congratulations.draw(win)

    label_total = Text(Point(210, 120), 'TOTAL MOVES: {0}'.format(total_moves))
    label_total.setSize(button_font)
    label_total.setTextColor(button_color)
    label_total.draw(win)

    button_new_y = 180
    button_new = Rectangle(
        Point(button_x[0], button_new_y), 
        Point(button_x[1], button_new_y + button_y_size)
    )
    button_new.setFill(button_color)
    button_new.draw(win)
    label_new = Text(Point(210, 220), 'NEW GAME')
    label_new.setSize(button_font)
    label_new.setTextColor(button_text_color)
    label_new.draw(win)

    button_end_y = 285
    button_end = Rectangle(
        Point(button_x[0], button_end_y), 
        Point(button_x[1], button_end_y + button_y_size)
    )
    button_end.setFill(button_color)
    button_end.draw(win)
    label_end = Text(Point(210, 325), 'EXIT')
    label_end.setSize(button_font)
    label_end.setTextColor(button_text_color)
    label_end.draw(win)

    new_game = True

    while True:
        pointer = win.getMouse()
        pointer_x = pointer.getX()
        pointer_y = pointer.getY()

        if (pointer_x < button_x[0]) or (pointer_x > button_x[1]):
            continue
        
        if pointer_y < button_new_y:
            continue
        
        if pointer_y <= button_new_y + button_y_size:
            break

        if pointer_y < button_end_y:
            continue
        
        if pointer_y <= button_end_y + button_y_size:
            new_game = False
            break

    label_congratulations.undraw()
    label_total.undraw()
    button_new.undraw()
    label_new.undraw()
    button_end.undraw()
    label_end.undraw()

    if new_game:
        create_menu(win)
    else:
        win.close()


if __name__ == '__main__':
    main()