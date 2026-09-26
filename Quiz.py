import pgzrun
WIDTH = 1000
HEIGHT = 700
TITLE = "Quiz"

#Rect(x,y, width, height)
Welcome_box = Rect(0, 0, 1300, 100)
question_1 = Rect(0,120,600, 180)
answer_1 = Rect(20,320, 400, 145)
answer_2 = Rect(20, 520, 400, 145)
answer_3 = Rect(430, 320, 400, 145)
answer_4 = Rect(430,520, 400, 145)


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




def on_mouse_down(pos):
    pass

def update():
    scroll_text()

def scroll_text():
    Welcome_box.x = Welcome_box.x - 5
    if Welcome_box.right < 0:
        Welcome_box.left = 1000

pgzrun.go()


