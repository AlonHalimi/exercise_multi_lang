package main

import (
	"fmt"
	"time"
)

func main() {
	input := make(chan string)
	ticker := time.NewTicker(time.Second * 1)
	go func() {
		for i := 0; i <= 12; i++ {
			<-ticker.C
			val := <-input
			fmt.Printf("value received %s", val)
		}
	}()

	for i := 0; i < 5; i++ {
		go func() {
			for counter := 1; ; counter++ {
				input <- fmt.Sprintf("from routing %d for the %d time\n", i, counter)
				time.Sleep(time.Millisecond * 100)
			}
		}()
	}


	time.Sleep(time.Hour)
}
