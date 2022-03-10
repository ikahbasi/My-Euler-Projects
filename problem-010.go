/*
Summation of primes
Problem 10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
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
	var sum int
	sum = 0
	for ii := 2; ii < 2e6; ii++ {
		if prime_func(ii) {
			sum += ii
		}
	}
	fmt.Println(sum)
}
