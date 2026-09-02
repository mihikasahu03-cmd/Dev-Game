import pgzrun
WIDTH = 1000
HEIGHT = 500
TITLE = "Quiz"

#Rect(x,y, width, height)
Welcome_box = Rect(0, 0, 1000, 100)



def draw():
    screen.clear()
    screen.draw.filled_rect(Welcome_box, color = "blue")
    welcome_text = "Welcome to the quiz master"
    screen.draw.textbox(welcome_text, Welcome_box, color = "White")

def on_mouse_down(pos):
    pass

def update():
    scroll_text()

def scroll_text():
    Welcome_box.x = Welcome_box.x - 5
    if Welcome_box.right < 0:
        Welcome_box.left = 1000

pgzrun.go()


