#冒泡排序算法函数(从大到小)
def bubble_sort_1(nums):
    for i in range((len(nums) - 1)):
        for j in range(((len(nums) - i) - 1)):
            if nums[j] < nums[j + 1]:
                nums[j], nums[(j + 1)] = nums[(j + 1)], nums[j]
    return nums

#冒泡排序算法函数(从小到大)
def bubble_sort_2(nums):
    for i in range((len(nums) - 1)):
        for j in range(((len(nums) - i) - 1)):
            if nums[j] > nums[j + 1]:
                nums[j], nums[(j + 1)] = nums[(j + 1)], nums[j]
    return nums








print("输入数字：", 3, 32, 54, 62, 25, 49.39, 392, 853, 132.32, 124, 34, 16, 65)
print("输出数字：（从大到小）", bubble_sort_1(
    [3, 32, 54, 62, 25, 49.39, 392, 853, 132.32, 124, 34, 16, 65]))

print("输入数字：", 3, 32, 54, 62, 25, 49.39, 392, 853, 132.32, 124, 34, 16, 65)
print("输出数字：（从小到大）", bubble_sort_2(
    [3, 32, 54, 62, 25, 49.39, 392, 853, 132.32, 124, 34, 16, 65]))
