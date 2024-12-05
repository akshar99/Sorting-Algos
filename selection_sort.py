"""
Selection sort involves comparison sorting by index, it repeatedly selects 
the smallest or largest element from the unsorted part of the array and moving
it to the sorted part.

-first loop is for iterating and making min_index as i
-In second loop it checks if from the reaming array i.e. nums[i:] if 
    any value is smaller the value at min index and updating the min_index.
-if i is not equal to min_index then we swap the values at the respective indexes 
"""

def selection_sort(nums):
    
    for i in range(len(nums) - 1):
        min_index = i

        for j in range(i+1, len(nums)):
            if nums[j] < nums[min_index]:
                min_index = j

        if i != min_index:
            temp = nums[i]
            nums[i] = nums[min_index]
            nums[min_index] = temp
    
    return nums

print(selection_sort([8,5,4,0,1,3,9,45,-2,-46]))
