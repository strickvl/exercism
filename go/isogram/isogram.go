package isogram

import "strings"

func IsIsogram(s string) bool {
	mp := map[string]int{}
	for _, v := range strings.ToLower(s) {
		char := string(v)
		if char != " " && char != "-" {
			_, ok := mp[char]
			if ok {
				return false
			} else {
				mp[char] = 1
			}
		}
	}
	
	return true
}
