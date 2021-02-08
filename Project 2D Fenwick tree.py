class BIT_2D:
    ##initialize a construct
    ## Here row define the rows in matrix
    ## Col defines the columns in matrix
    ## table[][] is the row x col matrix used to store 2D BIT
    def __init__(self, row, col):
        self.table = [[0 for i in range(row + 1)] for j in range(col + 1)]
        self.row = row
        self.col = col
    ## here LSB is used to find a least significant bit
    ##important operation in implementation of 2D BIT 
    ##is finding position of least significant one. 
    ##Considering 2-complement form of negative numbers,
    ##we can perform bitwise and to get position of least significant one
    def LSB(self, x):
        return x & (-x)
    #Update function update the value using x and y 
    ## x and y are desire location where we want to change the value
    def Update(self, x, y, value):
        #it checks, when  x is small or equals to the value of coloumn in a matrix
        ##value of col=4
        while x <= self.col:
        #then a new variable y1 is equal to y
            y1 = y
        #it checks, when y is small or equals to the value of row in a matrix
        ##value of row=4            
            while y1 <= self.row:
            ## if condition becomes true it update the value in array 
            ## row = x ,col = y
                self.table[x][y1] += value
                ##LSB returns the value of row
                ## update the value of y 
                y1 += self.LSB(y1)
            ## update the value of x
            x += self.LSB(x)
        ##return x
        return y1
    ## A function to get sum from (0, 0) to (x, y)
    def Sum(self,y,x):
        ## set the sum =0
        summ = 0
        x1 = x
        ## it check, when x1 is less than 0
        while x1 > 0:
            ## the y1 is equals to y
            y1 = y
            ## it check, when y1 is less than 0
            while y1 > 0:
            ## if condition becomes true 
            ## it make the sum of x1 and y1 in array which is a complete box
                summ += self.table[x1][y1]                
                y1 -= self.LSB(y1)
            x1 -= self.LSB(x1)
        ## return sum
        return summ
    ##we need to answer sum of sub-matrix bound by coordinates (x1, y1) and (x2, y2). 
    def getSum(self, x1, y1, x2, y2):
        return (self.Sum(x2, y2) - self.Sum(x1 - 1, y2) - self.Sum(x2, y1 - 1) + self.Sum(x1 - 1, y1 - 1))
    ## Build Tree take the value of row and coloumn and construct a 2D BIT
    def Build_Tree(self, array):
        ## value of row is equal to length of the matrix
        self.row = len(array)
        ## value of coloumn is equal to the length of matrix starting with a index 0
        self.col = len(array[0])
        ## itrate to the range of col
        for i in range(self.col):
        ## itrate to the range of row     
            for j in range(self.row):
                ## update function call and update the value in build tree also
                ## if update function make any updatation in tree 
                self.Update(i + 1, j + 1, array[i][j])
    ## Print function prints the array
    def Print(self):
        array = [[1,2,3,4],
                  [4, 3, 7, 8],
                  [9, 8, 6, 1],
                  [7, 4, 2, 5]]
        self.Build_Tree(array)
        for i in range(len(array)):
            for j in range(len(array[0])):
                print(array[i][j] , end=" ")
            print()
obj=BIT_2D(4,4)
#obj.Build_Tree([[1,2,3,4],
#                  [4, 3, 7, 8],
#                  [9, 8, 6, 1],
#                  [7, 4, 2, 5]])
#obj.LSB(12)
#obj.Update(2,2,6)
obj.Sum(1,1)
obj.getSum(1, 2, 2, 3)
obj.Print()