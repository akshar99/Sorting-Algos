def bubble_sort(nums):

    for i in range(len(nums) - 1, 0 , -1):
        for j in range(i):

            if nums[j] > nums[i]:
                print(nums[j])
                print(nums[j+1])
                tmp = nums[j]
                nums[j] = nums[j+1]
                nums[j + 1] = tmp

    return nums


print(bubble_sort([1,5,8,3,0,2]))
