from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.root = Tk()
        self.root.title = "Maze Solver"
        self.canvas = Canvas(self.root, bg="white", height=height, width=width)
        self.canvas.pack()
        self.running = False
    
    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def draw_line(self, line, fill_color="black"):
        line.draw(self.canvas, fill_color)
    
    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()
    
    def close(self):
        self.running = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def draw(self, canvas, fill_color):
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2)
        canvas.pack()

class Cell:
    def __init__(self, x1, x2, y1, y2):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._win = False
    
    def draw(self, canvas, x1, y1, x2, y2):
        if self.has_left_wall:
            canvas.create_line(x1, y1, x1, y2, fill="green", width=2)
        if self.has_right_wall:
            canvas.create_line(x2, y1, x2, y2, fill="purple", width=2)
        if self.has_top_wall:
            canvas.create_line(x1, y1, x2, y1, fill="blue", width=2)
        if self.has_bottom_wall:
            canvas.create_line(x1, y2, x2, y2, fill="red", width=2)

def main():
    win = Window(800,600)
    p1 = Point(100,100)
    p2 = Point(300,300)
    line = Line(p1,p2)
    win.draw_line(line, "black")
    cell = Cell(20, 40, 20, 40)
    cell.draw(win.canvas, 60, 80, 100, 120)
    win.wait_for_close()
    win.close()

main()
