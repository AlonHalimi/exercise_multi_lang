package main

import "fmt"
import "sync"

func main(){
	var vg sync.WaitGroup

	for i := 0; i<5; i++{
		vg.Add(1)
		go func(ii int){
			defer vg.Done()
			fmt.Printf("go routine %d", ii)
		}(i)
	}

	vg.Wait()
}