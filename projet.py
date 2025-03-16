import heapq

class PancakeProblem:
    def __init__(self, state):
        self.state = state
        self.goal = tuple(sorted(state))

    def is_goal(self, state):
        return state == self.goal
    
    def actions(self):
        return range(2, len(self.state) + 1)
    
    def flip(self, state, k):
        return tuple(reversed(state[:k])) + state[k:]
    
    @staticmethod
    def heuristic(state):
        return sum(abs(state[i] - state[i+1]) > 1 for i in range(len(state)-1))
    
    def astar(self):
        frontier = []
        heapq.heappush(frontier, (self.heuristic(self.state), 0, self.state, []))
        explored = set()
        
        while frontier:
            _, cost, current, path = heapq.heappop(frontier)
            
            if self.is_goal(current):
                return path
            
            if current in explored:
                continue
            explored.add(current)
            
            for action in self.actions():
                new_state = self.flip(current, action)
                new_path = path + [action]
                heapq.heappush(frontier, (cost + self.heuristic(new_state), cost + 1, new_state, new_path))
        
        return None
    
    def uniform_cost_search(self):
        frontier = [(0, self.state, [])]
        explored = set()
        
        while frontier:
            cost, current, path = heapq.heappop(frontier)
            
            if self.is_goal(current):
                return path
            
            if current in explored:
                continue
            explored.add(current)
            
            for action in self.actions():
                new_state = self.flip(current, action)
                new_path = path + [action]
                heapq.heappush(frontier, (cost + 1, new_state, new_path))
        
        return None
    
    def greedy_best_first(self):
        frontier = [(self.heuristic(self.state), self.state, [])]
        explored = set()
        
        while frontier:
            _, current, path = heapq.heappop(frontier)
            
            if self.is_goal(current):
                return path
            
            if current in explored:
                continue
            explored.add(current)
            
            for action in self.actions():
                new_state = self.flip(current, action)
                new_path = path + [action]
                heapq.heappush(frontier, (self.heuristic(new_state), new_state, new_path))
        
        return None

# Test   instances  
instances = [
    (4, 6, 2, 5, 1, 3),
    (1, 3, 7, 5, 2, 6, 4),
    (1, 7, 2, 6, 3, 5, 4),
    (1, 3, 5, 7, 9, 2, 4, 6, 8)
]

for i, instance in enumerate(instances, start=1):
    problem = PancakeProblem(instance)
    print(f"Solution A* pour c{i}: {problem.astar()}")
    print(f"Solution UCS pour c{i}: {problem.uniform_cost_search()}")
    print(f"Solution Greedy pour c{i}: {problem.greedy_best_first()}")
