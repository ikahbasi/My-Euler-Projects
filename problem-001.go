/*
Multiples of 3 or 5
Problem 1
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000. 
*/

package main

import "fmt"

func main() {
    var sum int
    sum = 0
    for ii:=1; ii<1000; ii++ {
        if (ii%3==0) || (ii%5==0) {
           sum += ii
           }
    }
fmt.Println(sum)
} 
