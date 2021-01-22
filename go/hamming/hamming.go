package hamming

import (
	"errors"
	"strings"
)

func Distance(a, b string) (int, error) {
	aSlice := strings.Split(a, "")
	bSlice := strings.Split(b, "")
	distance := 0

	if len(aSlice) != len(bSlice) {
		err := errors.New("the length isn't right")
		return distance, err
	}

	for i, _ := range aSlice {
		if aSlice[i] != bSlice[i] {
			distance++
		}
	}

	return distance, nil
}
