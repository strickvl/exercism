package raindrops

import "strconv"

func Convert(i int) (s string) {
	hasFactor := 0
	if i % 3 == 0 {
		s += "Pling"
		hasFactor++
	}
	if i % 5 == 0 {
		s += "Plang"
		hasFactor++
	}
	if i % 7 == 0 {
		s += "Plong"
		hasFactor++
	}
	if hasFactor == 0 {
		s = strconv.Itoa(i)
	}
	return
}
