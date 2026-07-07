class Pattern:
    def __init__(self,rows,columns):
        for i in range(1,rows+1):
            pattern = ""
            for j in range(1,columns+1):
                pattern+="* "
            print(pattern)



Pattern(5,10)