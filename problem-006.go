package main

import (
	"fmt"
)

func sum(array ...int) int {
	result := 0
	for _, val := range array {
		result += val
	}
	return result
}

func arr_range(start, end, step int) []int {
	length := (end - start) / step
	arr := make([]int, length)
	for ii := 0; ii < end-1; ii++ {
		arr[ii] = start + (ii * step)
	}
	return arr
}

func power(arr ...int) {
	for ind, val := range arr {
		arr[ind] = val * val
	}
}

func main() {
	//var a [10]int
	arr := arr_range(1, 101, 1)
	s1 := sum(arr...)
	s1 = s1 * s1
	power(arr...)
	s2 := sum(arr...)
	fmt.Println(s1, s2)
	fmt.Println(s1 - s2)
}
