from graphics import Canvas
import time
import random
####################### All the constants ############    
CANVAS_WIDTH = 500
CANVAS_HEIGHT = 500
DISTANCE_X = (CANVAS_WIDTH/10)+10
DISTANCE_Y = (CANVAS_HEIGHT/10)+10
PRINT_X =CANVAS_HEIGHT-50
PRINT_Y =CANVAS_HEIGHT-30
SIZE = 20
MAX_VALUE=CANVAS_WIDTH-SIZE
SNAKE_LENGTH = 20

LEVEL_UP_SCORE=50  # seting the value after which the level should increase
MAX_LEVEL=5     #when you are at max level play until the game gets over

START_X = 0
START_Y = 0
#                                  Remaining Bugs
#There are a lot of corner case. I solved as much as I can and the rests are beyond my capabilities
#right now. One of them is when you collide in a wall and you have life you randomly appear in the canvas.
#I made sure the snake doesn't appear just near the wall and game gets over by colliding to wall, but I
# am unable to figure out how to make sure the snake doesn't appear in front of an obstacle. I guess it
#will depend on players luck for now. ANd for level up the difficulty will be the life will appear less
#and less later with each level. I did not increased the speed with level because it hurt my eyes. But anyone
#wants to do it, knock your self out. Finally, there is only 5 levels because I think the game gets boring
#with too many levels.
 
# if you make this larger, the game will go slower
DELAY = 0.1 
                 
def create_goal_and_obstacle(canvas,score,level): # the function creates the goal, life and obstacle
    const=level*3
    goal=None  #None so that when goal is not created it returns None
    if score==0 or score%const!=0:
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
    if score>0 and score%const==0:
        life_x=random.randint(0, MAX_VALUE)
        life_y=random.randint(0, MAX_VALUE)
        life=canvas.create_oval(life_x,life_y,life_x+SIZE,life_y+SIZE,'lime')
        check=canvas.find_overlapping(life_x,life_y, 
                          life_x+SIZE,life_y+SIZE)
        while len(check)>1: #preventing goal from overlapping obstacle
            canvas.delete(life)
            life_x=random.randint(0, MAX_VALUE)
            life_y=random.randint(0, MAX_VALUE)
            life=canvas.create_oval(life_x,life_y,life_x+SIZE,life_y+SIZE,'lime')
            check=canvas.find_overlapping(life_x,life_y, 
                          life_x+SIZE,life_y+SIZE)
    return goal,obstacle,life




def game_over(canvas,score,level):  #Deletes all the object in the canvas and print score in a black background
    
    #creating the curtain to show at the end of the game
    des_x=-CANVAS_WIDTH
    des_y=-CANVAS_HEIGHT
    des_width=CANVAS_HEIGHT
    des=canvas.create_rectangle(des_x,des_y,des_x+des_width,des_y+des_width+500,'black')
    canvas.create_text(50, 170,
        "***Game Over***", 
        color="white", 
        font="Courier", 
        font_size=35)
    if level==MAX_LEVEL:
        canvas.create_text(60,100 , 
        "You reached MAX level, Hurrah! ",
        color="white", 
        font="Courier", 
        font_size=20)
    else:
        canvas.create_text(60,100 , 
        "You reached level ",
        color="white", 
        font="Courier", 
        font_size=30)
        canvas.create_text(380, 100, 
        str(level),
        color="white", 
        font="Courier", 
        font_size=30)
    #shows game over animation
    while des_x<0:
        des_x+=5
        overlapped_obj=canvas.find_overlapping(des_x,des_y, 
                          des_x+des_width,des_y+des_width+500)
        
        for i in overlapped_obj: #deleting all the objects including snake, goal and obstacles
            if i!=des:
                canvas.delete(i)
        canvas.moveto(des, des_x, des_y)
        time.sleep(0.001) 
        pass
        
    #create the background
    background = canvas.create_rectangle(0, 0,CANVAS_WIDTH,CANVAS_HEIGHT,
                              'black')
    #then print the score
    if level==MAX_LEVEL:
        canvas.create_text(60,100 , 
        "You reached MAX level, Hurrah! ",
        color="white", 
        font="Courier", 
        font_size=20)
    else:
        canvas.create_text(60,100 , 
        "You reached level ",
        color="white", 
        font="Courier", 
        font_size=30)
        canvas.create_text(380, 100, 
        str(level),
        color="white", 
        font="Courier", 
        font_size=30)
    canvas.create_text(50, 170,
        "***Game Over***", 
        color="white", 
        font="Courier", 
        font_size=35)
    canvas.create_text(60,200 , 
        "***Score is =       ***",
        color="white", 
        font="Courier", 
        font_size=30)
    canvas.create_text(300, 200, 
        str(score),
        color="white", 
        font="Courier", 
        font_size=30)
    pass
    
    
# this functions prints score and power in the left lower corner, when player is playing the game    
def print_score(canvas,score):
    text=canvas.create_text(110, PRINT_X, 
        str(score),
        color="black", 
        font="Courier", 
        font_size=20)
    return text
def print_power(canvas,x):
    power=canvas.create_text(110, PRINT_Y, 
        str(x),
        color="black", 
        font="Courier", 
        font_size=20)
    return power
    
    

# this is the most important function where all the codes for playing the game
def start_game(canvas,score,level):
    #starting animation
    des_x=-CANVAS_WIDTH
    des_y=-CANVAS_HEIGHT
    des_width=CANVAS_HEIGHT
    des=canvas.create_rectangle(des_x,des_y,des_x+des_width,des_y+des_width+500,'purple')
    if level==1:
        text=canvas.create_text(50, 170,
        "Game starting!!!", 
        color="white", 
        font="Courier", 
        font_size=35)
        textx=canvas.create_text(70, 210,
        "At level     !!!", 
        color="white", 
        font="Courier", 
        font_size=32)
        textl=canvas.create_text(240, 210,
        str(level), 
        color="white", 
        font="Courier", 
        font_size=32)
    else:
        text=canvas.create_text(150, 170,
        "Hurrah !!!", 
        color="white", 
        font="Courier", 
        font_size=35)
        textx=canvas.create_text(70, 210,
        "Moving to level   !!!", 
        color="white", 
        font="Courier", 
        font_size=32)
        textl=canvas.create_text(370, 210,
        str(level), 
        color="white", 
        font="Courier", 
        font_size=32)
    #shows game loading animation
    while des_x<0:
        des_x+=5
        canvas.moveto(des, des_x, des_y)
        time.sleep(0.001) 
    canvas.delete(des)
    canvas.delete(text)
    INITIAL_VELOCITY = 12
    x_velocity = INITIAL_VELOCITY
    y_velocity = 0
    snake_x = START_X
    snake_y = START_Y
    #score and power is initially zero
    power=0
    

    #creating snake
    snake = canvas.create_rectangle(snake_x, snake_y,
                              snake_x + SNAKE_LENGTH,
                              snake_y + SNAKE_LENGTH,
                              'blue')
                              
    #calling the goal function to create the first goal
    goal,obstacle,life=create_goal_and_obstacle(canvas,score,level)
    
    #create the score and power initializer at the lower left corner
    a=canvas.create_text(10,PRINT_X , 
        "Score =  ",
        color="black", 
        font="Courier", 
        font_size=20)
    b=canvas.create_text(10,PRINT_Y , 
        "Power =  ",
        color="black", 
        font="Courier", 
        font_size=20)
    
    text=print_score(canvas,score)
    px=print_power(canvas,power)
    while True:
        canvas.delete(text)#deleting the score and power everytime so that they updates instead of overlapping
        canvas.delete(px)
        text=print_score(canvas,score)
        px=print_power(canvas,power)
        
        #Checking the snake is colliding into the wall or not
        flag2=True
        if (snake_x < 0) or (snake_x + SNAKE_LENGTH >= CANVAS_WIDTH): # snake is colliding with wall
            if power>0:
                #print("power is more")
                power-=1
                canvas.delete(snake)
                if goal:      # make sure which to delete, goal or life
                    canvas.delete(goal)
                elif life:
                    canvas.delete(life)
                    score+=1
                flag2=False
                snake_x=random.randint(DISTANCE_X, MAX_VALUE-DISTANCE_X)# this makes sure the random function does't put snake right in front of wall and you collide immediately
                snake_y=random.randint(0, MAX_VALUE)
                snake = canvas.create_rectangle(snake_x, snake_y,
                              snake_x + SNAKE_LENGTH,
                              snake_y + SNAKE_LENGTH,
                              'blue')
                check=canvas.find_overlapping(snake_x, snake_y,
                              snake_x + SNAKE_LENGTH,
                              snake_y + SNAKE_LENGTH)
                while len(check)>1: #preventing snake from overlapping obstacle
                    canvas.delete(snake)
                    snake_x=random.randint(0, MAX_VALUE)
                    snake_y=random.randint(0, MAX_VALUE)
                    snake = canvas.create_rectangle(snake_x, snake_y,
                              snake_x + SNAKE_LENGTH,
                              snake_y + SNAKE_LENGTH,
                              'blue')
                    check=canvas.find_overlapping(snake_x, snake_y,
                              snake_x + SNAKE_LENGTH,
                              snake_y + SNAKE_LENGTH)
            else:   #snake dies
                game_over(canvas,score,level)
                break
            pass
        elif (snake_y < 0) or (snake_y + SNAKE_LENGTH >= CANVAS_HEIGHT): # snake is colliding with wall
            if power>0:
                #print("power is more")
                power-=1
                canvas.delete(snake)
                if goal:       #makes sure which to delete, goal or life
                    canvas.delete(goal)
                elif life:
                    canvas.delete(life)
                flag2=False
                snake_x=random.randint(0, MAX_VALUE)
                snake_y=random.randint(DISTANCE_Y, MAX_VALUE-DISTANCE_Y)#this makes sure the random function does't put snake right in front of wall and you collide immediately
                snake = canvas.create_rectangle(snake_x, snake_y,
                              snake_x + SNAKE_LENGTH,
                              snake_y + SNAKE_LENGTH,
                              'blue')
                check=canvas.find_overlapping(snake_x, snake_y,
                              snake_x + SNAKE_LENGTH,
                              snake_y + SNAKE_LENGTH)
                while len(check)>1: #preventing snake from overlapping obstacle
                    canvas.delete(snake)
                    snake_x=random.randint(0, MAX_VALUE)
                    snake_y=random.randint(0, MAX_VALUE)
                    snake = canvas.create_rectangle(snake_x, snake_y,
                              snake_x + SNAKE_LENGTH,
                              snake_y + SNAKE_LENGTH,
                              'blue')
                    check=canvas.find_overlapping(snake_x, snake_y,
                              snake_x + SNAKE_LENGTH,
                              snake_y + SNAKE_LENGTH)
            else:  #snake dies
                game_over(canvas,score,level)
                break
            pass
        if flag2==False:   # this make sure after reviving the snake doesn't take goal as obstacle. I put this because I am 
            goal,obstacle,life=create_goal_and_obstacle(canvas,score,level)# unable to figure out how to solve this issue
        
        
        
        #checking player is pressing which key
        key = canvas.get_last_key_press()
        if key == 'ArrowLeft':
            if x_velocity==0:
                x_velocity=INITIAL_VELOCITY*(-1)
            elif x_velocity>0:    # making sure it doesn't change direction if left arrow pressed twice
                x_velocity*=(-1)
            y_velocity=0
            #print('left arrow pressed!')
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
     
        #Checks snake is touching anything or not
        overlapped_obj=canvas.find_overlapping(snake_x,snake_y, 
                           snake_x+SNAKE_LENGTH,snake_y+SNAKE_LENGTH)
        
        
        #checking snake is toucing a goal or life or obstacle
        flag=True # to check it is eating life or destroying obstacle with power
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
                    print("power is ",power)
                    power-=1
                    flag=False
                    for i in overlapped_obj: # deleting the obstacle
                        if i!=snake:
                            canvas.delete(i)
                else:   #snake dies 
                    game_over(canvas,score,level)
                    break
            if score%15==0 and score>0:
                INITIAL_VELOCITY+=1   #increas speed after every 15 points
            if flag==True:
                goal,obstacle,life=create_goal_and_obstacle(canvas,score,level)  #create new goal after snake eats one
            
        
        
        if score==LEVEL_UP_SCORE and level!=MAX_LEVEL:
            canvas.delete(a)
            canvas.delete(b)
            canvas.delete(text)
            canvas.delete(px)
            o=canvas.find_overlapping(0,0,CANVAS_WIDTH,CANVAS_HEIGHT)
            for i in o:
                canvas.delete(i)
            #print("Breaking the loop")
            break
        
        snake_x += x_velocity
        snake_y += y_velocity
        canvas.moveto(snake, snake_x, snake_y)
        time.sleep(DELAY)
        pass
    #print("Returning the score")
    return score

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    # TODO: your code here
    score=0
    level=1
    #creates a background
    background=canvas.create_rectangle(0, 0,
                              CANVAS_WIDTH,
                              CANVAS_HEIGHT,
                              'yellow')
    #printing the required instruction
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
        "# Start and eat some goals", 
        color="red", 
        font="Courier", 
        font_size=15)
    text7=canvas.create_text(50, 290,
        "# Score 50 to level up", 
        color="red", 
        font="Courier", 
        font_size=15)
        
    #deletes instructions and start the game when pressed enter
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
            canvas.delete(text7)
            canvas.delete(start)
            canvas.delete(background)
            #starting the game
            score = start_game(canvas,score,level)
            while score==LEVEL_UP_SCORE:#increasing the level
                level+=1
                if level<=MAX_LEVEL:
                    score=start_game(canvas,0,level)
            break
    pass
        
    
    
    
if __name__ == '__main__':
    main()
