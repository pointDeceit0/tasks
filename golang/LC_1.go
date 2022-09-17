package main

import (
	//"fmt"
)

func twoSumBrute(nums []int, target int) []int {

    for i := 0; i < len(nums) - 1; i++ {
		for j := i + 1; j < len(nums); j++ {
			if nums[i] + nums[j] == target {
				return []int{i, j}
			}
		}
	}
	return []int{}
}


func twoSum(nums []int, target int) []int {
	return []int{}
}

/*
func main() {
	fmt.Println(twoSumBrute([]int{2,7,11,15}, 9))
	fmt.Println(twoSumBrute([]int{3,2,4}, 6))
}
*/