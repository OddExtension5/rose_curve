import tkinter as tk
import math

class RoseCurveApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Rose Curve Generator")

        self.canvas = tk.Canvas(self.root, width=600, height=600, bg='white')
        self.canvas.pack()

        self.controls_frame = tk.Frame(self.root)
        self.controls_frame.pack()

        self.label_k = tk.Label(self.controls_frame, text="Enter k value:")
        self.label_k.pack(side=tk.LEFT)

        self.entry_k = tk.Entry(self.controls_frame)
        self.entry_k.pack(side=tk.LEFT)

        self.draw_button = tk.Button(self.controls_frame, text="Draw", command=self.draw_rose_curve)
        self.draw_button.pack(side=tk.LEFT)

    def draw_rose_curve(self):
        k = float(self.entry_k.get())
        self.canvas.delete("all")

        width = 600
        height = 600
        center_x = width // 2
        center_y = height // 2
        radius = min(center_x, center_y) - 10

        num_points = 1000
        angle_step = 2 * math.pi / num_points

        points = []
        for i in range(num_points + 1):
            angle = i * angle_step
            r = radius * math.cos(k * angle)
            x = center_x + r * math.cos(angle)
            y = center_y - r * math.sin(angle)
            points.append((x, y))

        self.canvas.create_line(points, fill='black', smooth=True)

if __name__ == "__main__":
    root = tk.Tk()
    app = RoseCurveApp(root)
    root.mainloop()
