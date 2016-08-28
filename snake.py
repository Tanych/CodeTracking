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
        self.food=food
        self.width=width
        self.height=height
        self.positions=[(0,0)]
        self.score=0
        self.moveOps = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
        
    def move(self, direction):
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        :type direction: str
        :rtype: int
        """
        head=self.positions[0]
        tail=self.positions[-1]
        self.positions.pop()
        if direction not in self.moveOps:
            return -1
        di,dj=self.moveOps[direction]
        newhead=(head[0]+di,head[1]+dj)
        if newhead in self.positions or \
           newhead[0]<0 or newhead[0]>=self.height or \
           newhead[1]<0 or newhead[1]>=self.width:
            return -1
        
        self.positions.insert(0,newhead)
        if self.food and [newhead[0],newhead[1]]==self.food[0]:
            self.food.pop(0)
            self.positions.append(tail)
            self.score+=1

        return self.score
    
