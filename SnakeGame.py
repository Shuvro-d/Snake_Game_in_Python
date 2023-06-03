from graphics import Canvas
import time
import random

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
SIZE = 20
MAX_VALUE = 380
SNAKE_LENGTH = 20

START_X = 0
START_Y = 0

# if you make this larger, the game will go slower
DELAY = 0.1


def create_goal_and_obstacle(canvas, score):  # the function creates the goal and obstacle
    goal_x = random.randint(0, MAX_VALUE)
    goal_y = random.randint(0, MAX_VALUE)
    goal = canvas.create_rectangle(goal_x, goal_y, goal_x + SIZE, goal_y + SIZE, 'red')
    check = canvas.find_overlapping(goal_x, goal_y,
                                    goal_x + SIZE, goal_y + SIZE)
    while len(check) > 1:  # preventing goal from overlapping obstacle
        canvas.delete(goal)
        goal_x = random.randint(0, MAX_VALUE)
        goal_y = random.randint(0, MAX_VALUE)
        goal = canvas.create_rectangle(goal_x, goal_y, goal_x + SIZE, goal_y + SIZE, 'red')
        check = canvas.find_overlapping(goal_x, goal_y,
                                        goal_x + SIZE, goal_y + SIZE)

    obstacle = None  # obstacle is none because it only appears if score>5
    if score > 0 and score % 5 == 0:
        obs_x = random.randint(0, MAX_VALUE)
        obs_y = random.randint(0, MAX_VALUE)
        obstacle = canvas.create_rectangle(obs_x, obs_y, obs_x + SIZE, obs_y + SIZE, 'black')
        check = canvas.find_overlapping(obs_x, obs_y, obs_x + SIZE, obs_y + SIZE)
        while len(check) > 1:  # preventing obstacle from overlapping goal and another obstacle
            canvas.delete(obstacle)
            obs_x = random.randint(0, MAX_VALUE)
            obs_y = random.randint(0, MAX_VALUE)
            obstacle = canvas.create_rectangle(obs_x, obs_y, obs_x + SIZE, obs_y + SIZE, 'black')
            check = canvas.find_overlapping(obs_x, obs_y, obs_x + SIZE, obs_y + SIZE)
    return goal, obstacle


def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    # TODO: your code here
    INITIAL_VELOCITY = 12
    x_velocity = INITIAL_VELOCITY
    y_velocity = 0
    snake_x = START_X
    snake_y = START_Y
    score = 0
    snake = canvas.create_rectangle(snake_x, snake_y,
                                    snake_x + SNAKE_LENGTH,
                                    snake_y + SNAKE_LENGTH,
                                    'blue')

    goal, obstacle = create_goal_and_obstacle(canvas, score)

    while True:
        if (snake_x < 0) or (snake_x + SNAKE_LENGTH >= CANVAS_WIDTH):  # snake is colliding with wall
            print(" Game Over ")
            print(" Score is = ", score)
            break
        if (snake_y < 0) or (snake_y + SNAKE_LENGTH >= CANVAS_HEIGHT):  # snake is colliding with wall
            print(" Game Over ")
            print(" Score is = ", score)
            break

        key = canvas.get_last_key_press()
        if key == 'ArrowLeft':
            if x_velocity == 0:
                x_velocity = INITIAL_VELOCITY * (-1)
            elif x_velocity > 0:  # making sure it doesn't change direction if left arrow pressed twice
                x_velocity *= (-1)
            y_velocity = 0
            # print('left arrow pressed!')
        if key == 'ArrowRight':
            if x_velocity == 0:
                x_velocity = INITIAL_VELOCITY
            elif x_velocity < 0:  # making sure it doesn't change direction if right arrow pressed twice
                x_velocity *= (-1)
            y_velocity = 0
            # print('right arrow pressed!')
        if key == 'ArrowUp':
            if y_velocity == 0:
                y_velocity = INITIAL_VELOCITY * (-1)
            elif y_velocity > 0:  # making sure it doesn't change direction if up arrow pressed twice
                y_velocity *= (-1)
            x_velocity = 0
            # print('up arrow pressed!')
        if key == 'ArrowDown':
            if y_velocity == 0:
                y_velocity = INITIAL_VELOCITY
            elif y_velocity < 0:  # making sure it doesn't change direction if down arrow pressed twice
                y_velocity *= (-1)
            x_velocity = 0
            # print('down arrow pressed!')

        overlapped_obj = canvas.find_overlapping(snake_x, snake_y,
                                                 snake_x + SNAKE_LENGTH, snake_y + SNAKE_LENGTH)

        if len(overlapped_obj) > 1:  # reached the goal or an obstacle
            if overlapped_obj[1] == goal:
                # print("Goal")
                score += 1
                canvas.delete(goal)
            else:
                # print("Obstacle")
                print(" Game Over ")
                print(" Score = ", score)
                break
            if score % 5 == 0 and score > 0:
                INITIAL_VELOCITY += 1  # increas score after every 5 points
            goal, obstacle = create_goal_and_obstacle(canvas, score)  # snake eating the goal

        snake_x += x_velocity
        snake_y += y_velocity
        canvas.moveto(snake, snake_x, snake_y)
        time.sleep(DELAY)
        pass


if __name__ == '__main__':
    main()
