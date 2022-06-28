'''
두 수의 합으로 타겟을 만들 수 있는 두 수의 인덱스를 구하시오
(데이터는 오름차순 정렬되어 있으며 중복되지 않음)

입력: nums = [2, 7, 11, 15, 29] target = 9

출력: [0, 1]
'''

nums = [2, 7, 11, 15, 29]
target = 9

# for i in range(len(nums) - 1):
#     for j in range(i+1, len(nums)):
#         if nums[i] + nums[j] > target:
#             break
#         elif nums[i] + nums[j] == target:
#             print('[{},{}]'.format(i, j))

'''
feedback
    enumerate 함수를 이용하여, 하나의 for 문으로 해결!
'''

nums_map = {}
for i, num in enumerate(nums):
    val = target - num
    if val in nums_map:
        print('[{}, {}]'.format(nums_map[val], i))
    nums_map[num] = i