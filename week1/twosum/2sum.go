package main

func twoSum(nums []int, target int) []int {
	indices := make(map[int]int)
	for i, num := range nums {
		_target := target - nums[i]
		j, ok := indices[_target]
		if ok {
			return []int{j, i}
		}
		indices[num] = i
	}
	return []int{}
}
