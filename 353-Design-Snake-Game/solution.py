class SnakeGame(object):

    def __init__(self, width,height,food):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        :type width: int
        :type height: int
        :type food: List[List[int]]
        """
        self.width=width
        self.height=height
        self.food=collections.deque(food)
        self.position=collections.deque([(0,0)])
        self.moveops={'U':(-1,0),'L':(0,-1),'R':(0,1),'D':(1,0)}
        self.score=0

    def move(self, direction):
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        :type direction: str
        :rtype: int
        """
        if direction not in self.moveops:
            return -1
        peak,tail=self.position[0],self.position[-1]
        self.position.pop()
        idxi,idxj=self.moveops[direction]
        newi,newj=peak[0]+idxi,peak[1]+idxj
        if (newi,newj) in self.position or \
            newi<0 or newi>=self.height or \
            newj<0 or newj>=self.width:
            return -1
        self.position.appendleft((newi,newj))
        if self.food and [newi,newj]==self.food[0]:
            self.food.popleft()
            self.position.append(tail)
            self.score+=1
        return self.score


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)