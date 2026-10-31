import pgzrun
import time
WIDTH = 1000
HEIGHT = 700
TITLE = "Quiz"

#Rect(x,y, width, height)
Welcome_box = Rect(0, 0, 1300, 100)
question_1 = Rect(0,120,700, 180)
answer_1 = Rect(20,320, 400, 145)
answer_2 = Rect(20, 520, 400, 145)
answer_3 = Rect(430, 320, 400, 145)
answer_4 = Rect(430,520, 400, 145)
timer = Rect(750,120,200,180)
next = Rect(850,320, 100,145)

questions = []
questionfilename = "/Users/ajaysahu/Desktop/python/Game dev/question.txt"
question_index = 0
question = []
time_left = 10

def draw():
    screen.clear()
    screen.draw.filled_rect(Welcome_box, color = "blue")
    welcome_text = "Welcome to the quiz master"
    screen.draw.textbox(welcome_text, Welcome_box, color = "White")
    screen.draw.filled_rect(question_1, color = "pink")
    screen.draw.filled_rect(answer_1, color = "green")
    screen.draw.filled_rect(answer_2, color = "yellow")
    screen.draw.filled_rect(answer_3, color = "purple")
    screen.draw.filled_rect(answer_4, color = "grey")
    screen.draw.filled_rect(timer, color = "blue")
    screen.draw.filled_rect(next, color = "white")
    

    screen.draw.textbox(question[0].strip(), question_1, color = "black")
    screen.draw.textbox(question[1].strip(), answer_1, color = "white")
    screen.draw.textbox(question[2].strip(), answer_2, color = "white")
    screen.draw.textbox(question[3].strip(), answer_3, color = "white")
    screen.draw.textbox(question[4].strip(), answer_4, color = "white")

    screen.draw.textbox("next", next, color = "black")
    screen.draw.textbox(str(time_left), timer, color = "white")


def on_mouse_down(pos):
    pass

def update():
    scroll_text()

def scroll_text():
    Welcome_box.x = Welcome_box.x - 5
    if Welcome_box.right < 0:
        Welcome_box.left = 1000

def read_questionfile():
    global questions
    Qfile = open(questionfilename, "r")
    for i in Qfile:
        questions.append(i)

read_questionfile()        

def read_next_question():
    global question_index
    return questions.pop(0).split(",")



read_next_question()

question = read_next_question()
print(question)

def gameover():
 global question
 message = "Game over"
 question = [message, "-", "-", "-", "-"]

def update_time_left():
    global time_left
    if time_left:

        time_left = time_left -1
    else:
        gameover()    
clock.schedule_interval(update_time_left, 1)

pgzrun.go()


