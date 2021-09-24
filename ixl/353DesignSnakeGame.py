class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        """
        self.width = width
        self.height = height
        self.food = food
        self.snake = [[0, 0]]
        self.score = 0
        

    def move(self, direction: str) -> int:
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        """
        nextx, nexty = self.snake[0]
        if direction == 'U':
            nextx -= 1
        elif direction == 'L':
            nexty -= 1
        elif direction == 'D':
            nextx += 1
        elif direction == 'R':
            nexty += 1
        
        # found food, extend head, tail does not move
        if self.food and [nextx, nexty] == self.food[0]:
            self.snake.insert(0, [nextx, nexty])
            self.food = self.food[1:]
            self.score += 1
        else:
            # tail moves forward, remove the previous tail position
            self.snake = self.snake[:-1]
            # head moves to a new position
            self.snake.insert(0, [nextx, nexty])
            
            # check if the new pos goes beyond boudaries
            if nextx < 0 or nextx > self.height - 1 or nexty < 0 or nexty > self.width - 1:
                return -1
            
            # check if head is running into itself
            tmp = []
            for point in self.snake:
                if point not in tmp:
                    tmp.append(point)
            if len(tmp) < len(self.snake):
                return -1
        return self.score

# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)