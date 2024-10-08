from collections import deque

class State:
    def __init__(self, missionaries, cannibals, boat):
        self.missionaries = missionaries
        self.cannibals = cannibals
        self.boat = boat
        self.parent = None
    
    def is_valid(self):
        if self.missionaries < 0 or self.cannibals < 0 or self.missionaries > 3 or self.cannibals > 3:
            return False
        if (self.missionaries > 0 and self.missionaries < self.cannibals) or (self.missionaries > 0 and self.missionaries < self.cannibals):
            return False
        return True
    
    def is_goal(self):
        return self.missionaries == 0 and self.cannibals == 0 and self.boat == 0
    
    def get_children(self):
        children = []
        if self.boat == 1:  # Boat on the original side
            new_states = [
                State(self.missionaries - 2, self.cannibals, 0),
                State(self.missionaries, self.cannibals - 2, 0),
                State(self.missionaries - 1, self.cannibals - 1, 0),
                State(self.missionaries - 1, self.cannibals, 0),
                State(self.missionaries, self.cannibals - 1, 0)
            ]
        else:  # Boat on the other side
            new_states = [
                State(self.missionaries + 2, self.cannibals, 1),
                State(self.missionaries, self.cannibals + 2, 1),
                State(self.missionaries + 1, self.cannibals + 1, 1),
                State(self.missionaries + 1, self.cannibals, 1),
                State(self.missionaries, self.cannibals + 1, 1)
            ]
        
        for state in new_states:
            if state.is_valid():
                state.parent = self
                children.append(state)
        
        return children
    
    def __eq__(self, other):
        return self.missionaries == other.missionaries and self.cannibals == other.cannibals and self.boat == other.boat
    
    def __hash__(self):
        return hash((self.missionaries, self.cannibals, self.boat))

def bfs(initial_state):
    queue = deque([initial_state])
    visited = set()
    visited.add(initial_state)
    
    while queue:
        state = queue.popleft()
        if state.is_goal():
            return state
        
        for child in state.get_children():
            if child not in visited:
                visited.add(child)
                queue.append(child)
    
    return None

def print_solution(solution):
    path = []
    state = solution
    while state:
        path.append(state)
        state = state.parent
    
    path.reverse()
    for step in path:
        print(f"({step.missionaries}, {step.cannibals}, {step.boat})")

def main():
    initial_state = State(3, 3, 1)
    solution = bfs(initial_state)
    
    if solution:
        print("Solution found!")
        print_solution(solution)
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()