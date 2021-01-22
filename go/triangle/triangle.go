package triangle

import "math"

type Kind string

const (
	NaT = "NaT" // not a triangle
	Equ = "Equ" // equilateral
	Iso = "Iso"  // isosceles
	Sca = "Sca" // scalene
)

func IsInvalidTriangle(a, b, c float64) bool {
	if a <= 0 || b <= 0 || c <= 0 {
		return true
	} else if a + b < c || b + c < a || c + a < b {
		return true
	} else if math.IsNaN(a) || math.IsNaN(b) || math.IsNaN(c) || math.IsInf(a, 0) || math.IsInf(b, 0) || math.IsInf(c, 0) {
		return true
	}
	return false
}

// KindFromSides returns a triangle's type given the length of its sides
func KindFromSides(a, b, c float64) (k Kind) {
	if IsInvalidTriangle(a, b, c) {
		k = Kind(NaT)
	} else if a == b && b == c && c == a {
		k = Kind(Equ)
	} else if a == b || b == c || c == a {
		k = Kind(Iso)
	} else if a != b && b != c && c != a {
		k = Kind(Sca)
	}
	return
}
