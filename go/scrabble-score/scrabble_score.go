package scrabble

import "unicode"

func CalculateLetterScore(c rune) (i int) {
	switch unicode.ToUpper(c) {
	case 'A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T':
		return 1
	case 'D', 'G':
		return 2
	case 'B', 'C', 'M', 'P':
		return 3
	case 'F', 'H', 'V', 'W', 'Y':
		return 4
	case 'K':
		return 5
	case 'J', 'X':
		return 8
	case 'Q', 'Z':
		return 10
	}
	return
}

func Score(s string) (i int) {
	for _, v := range s {
		i += CalculateLetterScore(v)
	}
	return
}
