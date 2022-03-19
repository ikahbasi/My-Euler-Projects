/*
Power digit sum
Problem 16
215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 21000?
*/

package main

import (
	"fmt"
	"math/big"
)

func sumDigits(number int) int {
	remainder := 0
	sumResult := 0
	for number != 0 {
		//fmt.Println(number)
		remainder = number % 10
		sumResult += remainder
		number = number / 10
	}
	return sumResult
}

func main() {
	//num := big.NewInt(math.Pow(2.0, 1000.0))
	num := big.NewInt(10715086071862673209484250490600018105614048117055336074437503883703510511249361224931983788156958581275946729175531468251871452856923140435984577574698574803934567774824230985421074605062371141877954182153046474983581941267398767559165543946077062914571196477686542167660429831652624386837205668069376)
	fmt.Println(num)
	//sum_digit := sumDigits(num)
	//fmt.Println(sum_digit)

}
