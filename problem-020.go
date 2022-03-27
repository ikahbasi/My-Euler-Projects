/*
Factorial digit sum
Problem 20

n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
*/

package main

import "fmt"

func factorial(num int) int64 {
	var fac int64
	fac = int64(num)
	for num != 1 {
		num -= 1
		fac *= int64(num)
	}
	return fac
}

func sum_of_digits(num int) int {
	var sum, reminder int
	sum = 0
	for num != 0 {
		reminder = num % 10
		sum += reminder
		num /= 10
	}
	return sum
}

func main() {
	var num, fac, sum int
	num = 100
	fac = factorial(num)
	sum = sum_of_digits(fac)
	fmt.Println(fac, sum)
}
