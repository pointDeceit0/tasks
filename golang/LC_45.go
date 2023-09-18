package main

import (
	"fmt"
)

func jump(nums []int) int {
	
	for i := 1; i < len(nums); i++ {
		nums[i] = max(nums[i] + i, nums[i - 1])
	}

	i, ans := 0, 0

	for i < len(nums) - 1 {
		ans++
		i = nums[i]
	}
	
	return ans
}


func test() {

	fmt.Println(jump([]int{2,3,1,1,4}), 2)
	fmt.Println(jump([]int{2,3,0,1,4}), 2)
	//fmt.Println(jump([]int{0,0,0,0,0}), 0)
	fmt.Println(jump([]int{10,0,0,0,0}), 1)
	fmt.Println(jump([]int{0}), 0)
	fmt.Println(jump([]int{2,1,3,0,0,1}), 2)
	fmt.Println(jump([]int{1,1,1,1,1,0}), 5)
	fmt.Println(jump([]int{0,1,0,0,0,0,0}), 0)
	
}



