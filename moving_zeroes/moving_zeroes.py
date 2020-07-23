'''
Input: a List of integers
Returns: a List of integers
'''
import numpy as np

def moving_zeroes(arr):

    # Your code here

    nonzeroes = []
    zeroes = []
    
    
    for i in arr:
        

        if i !=0:
            nonzeroes.append(i)
        elif i == 0:
            zeroes.append(i) 
        

    mainlist = np.concatenate((nonzeroes, zeroes), axis=None)            

    return mainlist       
             



if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")