/*
Longest Collatz sequence
Problem 14

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
*/

package main

import (
	"fmt"
)

func collatz_sequence(start int) []int {
	num := start
	if num <= 0 {
		return []int{}
	}
	lst := []int{num}
	for ii := 0; num != 1; ii++ {
		if num%2 == 0 {
			num = num / 2
		} else {
			num = 3*num + 1
		}
		lst = append(lst, num)
	}
	return lst
}

func main() {
	collatz_len := []int{}
	for ii := 0; ii <= 1e6; ii++ {
		collatz_lst := collatz_sequence(ii)
		collatz_len = append(collatz_len, len(collatz_lst))
	}
	var max_num int
	max_leng := 0
	for num, leng := range collatz_len {
		if max_leng < leng {
			max_leng = leng
			max_num = num
		}
	}
	fmt.Println(max_num, max_leng)
}

/*
collatz_lst = []
for num in pyfunc.range_generator(0, 1e6+1):
	#print(num)
	collatz = pyfunc.collatz_sequence(num)
	collatz_lst.append(len(collatz))
m = max(collatz_lst)
print(collatz_lst.index(m))
*/
