import pyglet
from pyglet.gl import *

class Letter:
    def __init__(self):
        self.x_rotation=10
        self.x=100

    def draw(self):
        glRotatef(self.x_rotation, 0,1,0)
        glBegin(GL_QUADS)

        glColor3ub(255,0,0)
        glVertex3i(-60,-60,0)
        glVertex3i(-40,-60,0)
        glVertex3i(0,40,0)
        glVertex3i(0,80,0)

        glColor3ub(255,0,0)
        glVertex3i(0,80,0)
        glVertex3i(0,40,0)
        glVertex3i(40,-60,0)
        glVertex3i(60,-60,0)

        glColor3ub(255,0,0)
        glVertex3i(-30,-5,0)
        glVertex3i(-35,-15,0)
        glVertex3i(35,-15,0)
        glVertex3i(30,-5,0)


        glColor3ub(255,0,0)
        glVertex3i(-60,-60,-10)
        glVertex3i(-40,-60,-10)
        glVertex3i(0,40,-10)
        glVertex3i(0,80,-10)

        glColor3ub(255,0,0)
        glVertex3i(0,80,-10)
        glVertex3i(0,40,-10)
        glVertex3i(40,-60,-10)
        glVertex3i(60,-60,-10)

        glColor3ub(255,0,0)
        glVertex3i(-30,-5,-10)
        glVertex3i(-35,-15,-10)
        glVertex3i(35,-15,-10)
        glVertex3i(30,-5,-10)

        glColor3ub(255,0,0)
        glVertex3i(-60,-60,-10)
        glVertex3i(-60,-60,0)
        glVertex3i(0,80,-10)
        glVertex3i(0,80,0)


        glColor3ub(255,0,0)
        glVertex3i(60,-60,-10)
        glVertex3i(60,-60,0)
        glVertex3i(0,80,-10)
        glVertex3i(0,80,0)

        glColor3ub(255,0,0)
        glVertex3i(40,-60,-10)
        glVertex3i(40,-60,0)
        glVertex3i(0,40,-10)
        glVertex3i(0,40,0)

        glColor3ub(255,0,0)
        glVertex3i(-40,-60,0)
        glVertex3i(-40,-60,-10)
        glVertex3i(0,40,0)
        glVertex3i(0,40,-10)
        glEnd()
    def update(self):
        self.x_rotation += 1

class Window(pyglet.window.Window):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.letter=Letter()
    def on_draw(self):
        self.clear()
        glPushMatrix()
        self.letter.draw()
        glPopMatrix()
    def on_resize(self,width,height):
        glViewport(0,0,width,height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(35,1,1,1000)
        gluLookAt(0,0,100,0,0,0,0,1,0)
        glMatrixMode(GL_MODELVIEW)
        glTranslatef(0,0,-400)
    def update(self,dt):
        self.letter.update()

if __name__=="__main__":
    win=Window(width=800, height=600, resizable=False)
    pyglet.clock.schedule_interval(win.update , 1/100)
    pyglet.app.run()
        
    
