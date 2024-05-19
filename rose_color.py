import tkinter as tk
import math
import random

class RoseCurveApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Rose Curve Generator")

        self.canvas = tk.Canvas(self.root, width=600, height=600, bg='white')
        self.canvas.pack()

        self.k = 1
        self.colors = ["red", "green", "blue", "orange", "purple", "pink", "yellow", "cyan", "magenta"]
        self.animate_rose_curve()

    def animate_rose_curve(self):
        self.canvas.delete("all")
        self.draw_rose_curve(self.k)
        self.k += 1
        if self.k <= 200:
            self.root.after(500, self.animate_rose_curve)  # Adjust the delay for slower animation

    def draw_rose_curve(self, k):
        width = 600
        height = 600
        center_x = width // 2
        center_y = height // 2
        radius = min(center_x, center_y) - 10

        num_points = 1000
        angle_step = 2 * math.pi / num_points

        points = []
        current_color = random.choice(self.colors)
        segment_length = num_points // len(self.colors)

        for i in range(num_points + 1):
            angle = i * angle_step
            r = radius * math.cos(k * angle)
            x = center_x + r * math.cos(angle)
            y = center_y - r * math.sin(angle)
            points.append((x, y))

            if i % segment_length == 0 and i != 0:
                if len(points) > 1:
                    self.canvas.create_line(points, fill=current_color, smooth=True, width=2)
                points = [(x, y)]
                current_color = random.choice(self.colors)

        if len(points) > 1:
            self.canvas.create_line(points, fill=current_color, smooth=True, width=2)

if __name__ == "__main__":
    root = tk.Tk()
    app = RoseCurveApp(root)
    root.mainloop()
