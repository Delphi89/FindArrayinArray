#. This implementation uses a nested loop to iterate 
#. over the possible starting indices for the subarray 
#. in the larger array, and checks if the corresponding 
#. elements of the subarray and the larger array match 
#. at each position.

#. This implementation has a time complexity of O(mn), 
#. where m is the number of rows and n is the number 
#. of columns in array. It is efficient for arrays of 
#. moderate size, but may not be suitable for very 
#. large arrays.

def search_subarray(array, subarray):
    sub_rows = len(subarray)
    sub_cols = len(subarray[0])
    for i in range(len(array) - sub_rows + 1):
        for j in range(len(array[0]) - sub_cols + 1):
            found = True
            for ii in range(sub_rows):
                for jj in range(sub_cols):
                    if array[i+ii][j+jj] != subarray[ii][jj]:
                        found = False
                        break
                if not found:
                    break
            if found:
                return True
    return False

# Example usage
array = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
subarray = [[7, 8], [11, 12]]

if search_subarray(array, subarray):
    print("Found subarray!")
else:
    print("Subarray not found.")
