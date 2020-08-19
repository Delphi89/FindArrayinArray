# FindArrayinArray
Python code that checks if a given 2d array is part of another given 2d array

The user arrays can be given at the end of the provided code.

The function can be run as: 

findArrayinArray(A, B)

or 

    if (findArrayinArray(A, B)): 
        print("Array B included in Array A"); 
    else: 
        print("Array B NOT included in Array A");



#example 1

A = ( [6, 7, 3, 4, 11],
      [1, 3, 3, 4, 9], 
      [5, 7, 7, 8, 10],
      [6, 3, 3, 4, 11])

B = ([3,4],
     [7,8])
     
Array B is part of Array A with all the elements in the correct order




#example 2

A = ( [6, 7, 3, 4, 11],
      [1, 3, 3, 4, 9], 
      [5, 7, 7, 8, 10],
      [6, 3, 3, 4, 11])

B = ([33,44],
     [7,8])
     
Array B is NOT part of Array A
     
