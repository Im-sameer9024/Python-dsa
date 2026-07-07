

class SpiralMatrix:
    def __init__(self,rows,cols):
        matrix = [[0]*cols for _ in range(rows)]
        top = 0
        left = 0
        bottom = rows -1
        right = cols -1
        num = 1
        while top <= bottom and left <= right:

            # Left to Right 
            for i in range(left,right+1):
                matrix[top][i] = num
                num+=1
            top+=1

            # Top to Bottom 
            for i in range(top,bottom+1):
                matrix[i][right] = num
                num+=1
            right-=1
            
            # Right to Left 
            if top <= bottom :
                for i in range(right,left-1,-1):
                    matrix[bottom][i] = num
                    num+=1
                bottom-=1
            
            # Bottom to top 
            if left <= right:
                for i in range(bottom,top-1,-1):
                    matrix[i][left] = num
                    num+=1
                left+=1
        
        for row in matrix:
            print(*row)


SpiralMatrix(4,5)