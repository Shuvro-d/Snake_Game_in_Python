from graphics import Canvas
import time
import random
    
CANVAS_WIDTH = 500
CANVAS_HEIGHT = 500
SIZE = 20
MAX_VALUE=CANVAS_WIDTH-SIZE
SNAKE_LENGTH = 20

START_X = 0
START_Y = 0


# if you make this larger, the game will go slower
DELAY = 0.1 
                 
def create_goal_and_obstacle(canvas,score): # the function creates the goal and obstacle
    goal=None
    if score==0 or score%15!=0:
        goal_x=random.randint(0, MAX_VALUE)
        goal_y=random.randint(0, MAX_VALUE)
        goal=canvas.create_rectangle(goal_x,goal_y,goal_x+SIZE,goal_y+SIZE,'red')
        check=canvas.find_overlapping(goal_x,goal_y, 
                           goal_x+SIZE,goal_y+SIZE)
        while len(check)>1: #preventing goal from overlapping obstacle
            canvas.delete(goal)
            goal_x=random.randint(0, MAX_VALUE)
            goal_y=random.randint(0, MAX_VALUE)
            goal=canvas.create_rectangle(goal_x,goal_y,goal_x+SIZE,goal_y+SIZE,'red')
            check=canvas.find_overlapping(goal_x,goal_y, 
                           goal_x+SIZE,goal_y+SIZE)
        
    obstacle=None  #obstacle is none because it only appears if score is divisible by 5
    if score>0 and score%5==0:
        obs_x=random.randint(0, MAX_VALUE)
        obs_y=random.randint(0, MAX_VALUE)
        obstacle=canvas.create_rectangle(obs_x,obs_y,obs_x+SIZE,obs_y+SIZE,'black')
        check=canvas.find_overlapping(obs_x,obs_y,obs_x+SIZE,obs_y+SIZE)
        while len(check)>1: #preventing obstacle from overlapping goal and another obstacle
            canvas.delete(obstacle)
            obs_x=random.randint(0, MAX_VALUE)
            obs_y=random.randint(0, MAX_VALUE)
            obstacle=canvas.create_rectangle(obs_x,obs_y,obs_x+SIZE,obs_y+SIZE,'black')
            check=canvas.find_overlapping(obs_x,obs_y,obs_x+SIZE,obs_y+SIZE)
         
    life=None   # life is none because it only appears if score is divisible by 15
    if score>0 and score%15==0:
        life_x=random.randint(0, MAX_VALUE)
        life_y=random.randint(0, MAX_VALUE)
        life=canvas.create_oval(life_x,life_y,life_x+SIZE,life_y+SIZE,'lime')
        check=canvas.find_overlapping(life_x,life_y, 
                          life_x+SIZE,life_y+SIZE)
        while len(check)>1: #preventing goal from overlapping obstacle
            canvas.delete(life)
            life_x=random.randint(0, MAX_VALUE)
            life_y=random.randint(0, MAX_VALUE)
            goal=canvas.create_oval(life_x,life_y,life_x+SIZE,life_y+SIZE,'lime')
            check=canvas.find_overlapping(life_x,life_y, 
                          life_x+SIZE,life_y+SIZE)
    return goal,obstacle,life




def game_over(canvas,score):
    #first delete all the obstacles, snake and goal from the canvas
    overlapped_obj=canvas.find_overlapping(0,0, 
                           CANVAS_WIDTH,CANVAS_HEIGHT)
    for i in overlapped_obj:
        canvas.delete(i)
        
    #create the background
    background = canvas.create_rectangle(0, 0,CANVAS_WIDTH,CANVAS_HEIGHT,
                              'black')
    #then print the score
    canvas.create_text(50, 170,
        "***Game Over***", 
        color="white", 
        font="Courier", 
        font_size=35)
    canvas.create_text(60,200 , 
        "***Score is =  ***",
        color="white", 
        font="Courier", 
        font_size=30)
    canvas.create_text(300, 200, 
        str(score),
        color="white", 
        font="Courier", 
        font_size=30)
    pass
    
def print_score(canvas,score):
    text=canvas.create_text(145, 450, 
        str(score),
        color="black", 
        font="Courier", 
        font_size=20)
    return text
def print_power(canvas,x):
    power=canvas.create_text(145, 470, 
        str(x),
        color="black", 
        font="Courier", 
        font_size=20)
    return power
    
    


def start_game(canvas):
    INITIAL_VELOCITY = 12
    x_velocity = INITIAL_VELOCITY
    y_velocity = 0
    snake_x = START_X
    snake_y = START_Y
    score=0
    power=0
    

    #creating snake
    snake = canvas.create_rectangle(snake_x, snake_y,
                              snake_x + SNAKE_LENGTH,
                              snake_y + SNAKE_LENGTH,
                              'blue')
    #calling the goal function
    goal,obstacle,life=create_goal_and_obstacle(canvas,score)
    
    canvas.create_text(10,450 , 
        "Score is =  ",
        color="black", 
        font="Courier", 
        font_size=20)
    canvas.create_text(10,470 , 
        "Power is =  ",
        color="black", 
        font="Courier", 
        font_size=20)
    
    text=print_score(canvas,score)
    px=print_power(canvas,power)
    while True:
        canvas.delete(text)
        canvas.delete(px)
        text=print_score(canvas,score)
        px=print_power(canvas,power)
        if (snake_x < 0) or (snake_x + SNAKE_LENGTH >= CANVAS_WIDTH): # snake is colliding with wall
            game_over(canvas,score)
            break
            pass
        if (snake_y < 0) or (snake_y + SNAKE_LENGTH >= CANVAS_HEIGHT): # snake is colliding with wall
            game_over(canvas,score)
            break
            pass
        
        key = canvas.get_last_key_press()
        if key == 'ArrowLeft':
            if x_velocity==0:
                x_velocity=INITIAL_VELOCITY*(-1)
            elif x_velocity>0:    # making sure it doesn't change direction if left arrow pressed twice
                x_velocity*=(-1)
            y_velocity=0
            print('left arrow pressed!')
        if key == 'ArrowRight':
            if x_velocity==0:
                x_velocity=INITIAL_VELOCITY
            elif x_velocity<0:    # making sure it doesn't change direction if right arrow pressed twice
                x_velocity*=(-1)
            y_velocity=0
            #print('right arrow pressed!')
        if key == 'ArrowUp':
            if y_velocity==0:
                y_velocity=INITIAL_VELOCITY*(-1)
            elif y_velocity>0:   # making sure it doesn't change direction if up arrow pressed twice
                y_velocity*=(-1)
            x_velocity=0
            #print('up arrow pressed!')
        if key == 'ArrowDown':
            if y_velocity==0:
                y_velocity=INITIAL_VELOCITY
            elif y_velocity<0:    # making sure it doesn't change direction if down arrow pressed twice
                y_velocity*=(-1)
            x_velocity=0
            #print('down arrow pressed!')
     
      
        overlapped_obj=canvas.find_overlapping(snake_x,snake_y, 
                           snake_x+SNAKE_LENGTH,snake_y+SNAKE_LENGTH)
        
        flag=True # to check it is eatin life or destroying obstacle with power
        if len(overlapped_obj)>1: #reached the goal or an obstacle
            if overlapped_obj[1]==goal:   #snake eats the goal
                print("Goal")
                score+=1
                canvas.delete(goal) 
            elif overlapped_obj[1]==life: #snake get power
                print("life")
                power+=1
                score+=1
                canvas.delete(life)
            else:
                print("obstacle")
                if power>0:        # snake destroyes obstacle with power
                    power-=1
                    flag=False
                    canvas.delete(overlapped_obj[1])
                else:               #snake dies 
                    game_over(canvas,score)
                    break
            if score%15==0 and score>0:
                INITIAL_VELOCITY+=1   #increas score after every 15 points
            if flag==True:
                goal,obstacle,life=create_goal_and_obstacle(canvas,score)  #create new goal after snake eats one
            
      
        snake_x += x_velocity
        snake_y += y_velocity
        canvas.moveto(snake, snake_x, snake_y)
        time.sleep(DELAY)
        pass

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    # TODO: your code here
    background=canvas.create_rectangle(0, 0,
                              CANVAS_WIDTH,
                              CANVAS_HEIGHT,
                              'yellow')
    start=canvas.create_text(50, 100,
        "***Press Enter to start the game***", 
        color="red", 
        font="Courier", 
        font_size=20)
    text=canvas.create_text(50, 150,
        "***Instructions***", 
        color="red", 
        font="Courier", 
        font_size=25)
    text2=canvas.create_text(50, 190,
        "# Blue box is snake", 
        color="red", 
        font="Courier", 
        font_size=15)
    text3=canvas.create_text(50, 210,
        "# Red box is Goal, eat it", 
        color="red", 
        font="Courier", 
        font_size=15)
    text4=canvas.create_text(50, 230,
        "# Black box is obstacle, touch and game over", 
        color="red", 
        font="Courier", 
        font_size=15)
    text5=canvas.create_text(50, 250,
        "# Green ball is power, eat it and gain extra life", 
        color="red", 
        font="Courier", 
        font_size=15)
    text6=canvas.create_text(50, 270,
        "# Power saves you from obstacle not wall", 
        color="red", 
        font="Courier", 
        font_size=15)
    while True:
        key=canvas.get_last_key_press()
        if key=='Enter':
            overlapped_obj=canvas.find_overlapping(0,0, 
                           CANVAS_WIDTH,CANVAS_HEIGHT)
            canvas.delete(text)
            canvas.delete(text2)
            canvas.delete(text3)
            canvas.delete(text4)
            canvas.delete(text5)
            canvas.delete(text6)
            canvas.delete(start)
            canvas.delete(background)
            
            start_game(canvas)
            break
    pass
        
    
    
    
if __name__ == '__main__':
    main()
