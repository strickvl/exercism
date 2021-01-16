package hamming

import (
	"strings"
	"errors"
)

func Distance(a, b string) (int, error) {
	aSlice := strings.Split(a, "")
	bSlice := strings.Split(b, "")
	distance := 0
	var err error
	
	if len(aSlice) != len(bSlice) {
		err = errors.New("The length isn't right")
		return distance, err
	}
	
	for i, _ := range aSlice {
		if aSlice[i] != bSlice[i] {
			distance++
		}
	}

	return distance, err
}
