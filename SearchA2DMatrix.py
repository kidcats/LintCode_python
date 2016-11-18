def searchMatrix( matrix, target):
        # write your code here
        if(len(matrix)==0):
            return False
        y=len(matrix[0])-1
        x=len(matrix)-1
        while y>=0:
            if(matrix[x][y])==target:
                return True
            else:
                if(matrix[x-1][y]>=target) and x>0:
                    x-=1
                else:
                    if(matrix[x][y-1]==target):
                        return True
                    else:
                        y-=1
        return False

if __name__=='__main__':
    a=searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]],1)
    print(a)