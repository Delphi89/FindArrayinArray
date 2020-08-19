import numpy as np



def findArrayinArray(A, B): 

    #calculate the shapes of the arrays
    m,n = np.shape(A)
    o,p = np.shape(B)
    #calculate the number of elements of array B
    L1 = o*p
    
    #check if the array we search is smaller than the array where we search
    if (m < o) or (n<p):
        print('searched array is larger than the array in which is searched!')    
        return 'End!'
    
    k = 0
    l = 0
    flag = False
        
    #check first if all elements of array B can be found in array A        
    for i in range(0,m): 
        for j in range(0,n):         
                                     
            if A[i][j] == B[k][l]:
                #print('found an identical element')
                if (k==o-1) and (l==p-1):
                    print('All the elements of array B are included in array A')
                    flag = True
                    break
                if (l<(p-1)):
                    l=l+1
                else:
                    l=0
                    if (k<(o-1)):
                        k=k+1
                    else:
                        k=0                   

    count = 0

    #if the first element of array B is part of A, look for the rest of the elements
    if flag == True:
        for i in range(0,m-(o-1)): 
            for j in range(0,n-(p-1)):
                if A[i][j] == B[0][0]:
                    #print('found the first element:', i, j)
                    for i2 in range(0,o):
                        for j2 in range (0,p):
                            if A[i+i2][j+j2] == B[i2][j2]:
                                #print('equal')
                                count = count + 1
                                if (i2==o-1) and (j2==p-1) and (count == L1):
                                    print('Confirmed: Array B is included in Array A! Elements in the correct order')
                            else:
                                count = 0
                                break
                            #print('Count: ',count)
    return m,n,o,p

#example
A = ( [6, 7, 3, 4, 11],
      [1, 3, 3, 4, 9], 
      [5, 7, 7, 8, 10],
      [6, 3, 3, 4, 11])

B = ([3,4],
     [7,8])

print('A: ',A)
print('B: ',B)

findArrayinArray(A, B)


