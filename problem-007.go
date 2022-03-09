/*
10001st prime
Problem 7
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
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

func nth_prime_number(th int) int {
	var counter, prime int
	counter = 0
	for ii := 0; counter <= th+1; ii++ {
		if prime_func(ii) {
			counter++
			prime = ii
		}
	}
	return prime
}
func main() {
	p := nth_prime_number(10001)
	fmt.Println(p)
}
