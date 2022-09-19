package main

import (
	"fmt"
)

func maxProfit(prices []int) int {
	maxProf, curMin := 0, prices[0]

	/*
	 * Time Complexity  --- O(n)
	 * Space complexity --- O(1)
	 *
	*/

	for _, v := range prices {
		if v < curMin {
			curMin = v
		} else if maxProf < v - curMin {
			maxProf = v - curMin
		}
	}

    return maxProf
}

func main() {
	fmt.Println(maxProfit([]int{7,1,5,3,6,4}))	
	fmt.Println(maxProfit([]int{7,6,4,3,1}))	
}