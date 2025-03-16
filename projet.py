import tkinter as tk
import heapq
import time
from Interface import PancakeGUI

class PancakeProblem:
    def __init__(self, state):
        self.state = state
        self.goal = tuple(sorted(state))

    # Check if the current state is the goal state
    def is_goal(self, state):
        return state == self.goal
    
    # Define possible flip actions (positions where the spatula can be placed)
    def actions(self):
        return range(2, len(self.state) + 1)
    
    # Perform a flip at position k
    def flip(self, state, k):
        return tuple(reversed(state[:k])) + state[k:]
    
    # Heuristic function: counts the number of adjacent pancakes that are not in order
    @staticmethod
    def heuristic(state):
        return sum(abs(state[i] - state[i+1]) > 1 for i in range(len(state)-1))
    
    # A* search algorithm with step tracking
    def astar_with_steps(self):
        frontier = []
        heapq.heappush(frontier, (self.heuristic(self.state), 0, self.state, []))
        explored = set()
        steps = [self.state]  # List of successive states
        
        while frontier:
            _, cost, current, path = heapq.heappop(frontier)

            if self.is_goal(current):
                return steps  # Return the list of steps to reach the goal
            
            if current in explored:
                continue
            explored.add(current)
            
            for action in self.actions():
                new_state = self.flip(current, action)
                new_path = path + [action]
                steps.append(new_state)  # Store the new state
                heapq.heappush(frontier, (cost + self.heuristic(new_state), cost + 1, new_state, new_path))
        
        return steps

    # Uniform Cost Search (UCS) with step tracking
    def uniform_cost_search_with_steps(self):
        frontier = [(0, self.state, [])]
        explored = set()
        steps = [self.state]
        
        while frontier:
            cost, current, path = heapq.heappop(frontier)
            
            if self.is_goal(current):
                return steps
            
            if current in explored:
                continue
            explored.add(current)
            
            for action in self.actions():
                new_state = self.flip(current, action)
                new_path = path + [action]
                steps.append(new_state)
                heapq.heappush(frontier, (cost + 1, new_state, new_path))
        
        return steps
    
    # Greedy Best-First Search with step tracking
    def greedy_best_first_with_steps(self):
        frontier = [(self.heuristic(self.state), self.state, [])]
        explored = set()
        steps = [self.state]
        
        while frontier:
            _, current, path = heapq.heappop(frontier)
            
            if self.is_goal(current):
                return steps
            
            if current in explored:
                continue
            explored.add(current)
            
            for action in self.actions():
                new_state = self.flip(current, action)
                new_path = path + [action]
                steps.append(new_state)
                heapq.heappush(frontier, (self.heuristic(new_state), new_state, new_path))
        
        return steps

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Pancake Sorting 🍽️")

    instance = (4, 6, 2, 5, 1, 3)  # Example initial state
    problem = PancakeProblem(instance)
    
    gui = PancakeGUI(root, problem)

    btn_astar = tk.Button(root, text="Start A*", command=lambda: gui.start_sorting(problem.astar_with_steps))
    btn_astar.pack()

    btn_ucs = tk.Button(root, text="Start UCS", command=lambda: gui.start_sorting(problem.uniform_cost_search_with_steps))
    btn_ucs.pack()

    btn_greedy = tk.Button(root, text="Start Greedy", command=lambda: gui.start_sorting(problem.greedy_best_first_with_steps))
    btn_greedy.pack()

    root.mainloop()

# Test instances
instances = [
    (4, 6, 2, 5, 1, 3),
    (1, 3, 7, 5, 2, 6, 4),
    (1, 7, 2, 6, 3, 5, 4),
    (1, 3, 5, 7, 9, 2, 4, 6, 8)
]

for i, instance in enumerate(instances, start=1):
    problem = PancakeProblem(instance)
    print(f"A* Solution for c{i}: {problem.astar_with_steps()}")
    print(f"UCS Solution for c{i}: {problem.uniform_cost_search_with_steps()}")
    print(f"Greedy Solution for c{i}: {problem.greedy_best_first_with_steps()}")