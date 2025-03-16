import tkinter as tk
import heapq
import time

class PancakeGUI:
    def __init__(self, root, problem):
        self.root = root
        self.problem = problem
        self.canvas = tk.Canvas(root, width=300, height=400, bg="white")
        self.canvas.pack()
        self.steps = []
        self.index = 0
        self.running = False

    # Draw pancakes as rectangles on the canvas
    def draw_pancakes(self, state):
        self.canvas.delete("all")  # Clear the previous drawing
        width = 300
        height = 400
        bar_height = height // len(state)

        for i, size in enumerate(state):
            x1 = (width - (size * 20)) // 2
            x2 = x1 + size * 20
            y1 = i * bar_height
            y2 = y1 + bar_height - 2
            self.canvas.create_rectangle(x1, y1, x2, y2, fill="brown")

    # Update the canvas display to show each step of sorting
    def update_display(self):
        if self.index < len(self.steps):
            self.draw_pancakes(self.steps[self.index])
            self.index += 1
            self.root.after(1000, self.update_display)  # Update every second
        else:
            self.running = False

    # Start the sorting process with the chosen algorithm
    def start_sorting(self, algorithm):
        if not self.running and len(self.steps) < 1000:
            self.steps = algorithm()
            if self.steps:
                self.index = 0
                self.running = True
                self.update_display()
            else:
                print("No solution found or an issue occurred while executing the algorithm.")
        else:
            self.running = False  # Stops the infinite loop
        
         