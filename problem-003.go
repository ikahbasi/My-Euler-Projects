/*
Largest prime factor
Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
*/

package main

import (
	"fmt"
	"math"
)

func prime_func(num int) bool {
	var _prime bool
	_prime = true
	sqrt_num := int(math.Sqrt(float64(num)))
	for ii := 2; ii <= sqrt_num; ii++ {
		if num%ii == 0 {
			_prime = false
			break
		}
	}
	return _prime
}
func main() {
	var _prime bool
	var largest_prime_factor int
	value := 600851475143
	sqrt_value := int(math.Sqrt(float64(value)))
	for num := 1; num < sqrt_value; num++ {
		_prime = prime_func(num)
		if _prime {
			factor := (value%num == 0)
			if factor {
				largest_prime_factor = num
			}
		}
	}
	fmt.Println(largest_prime_factor)
}
