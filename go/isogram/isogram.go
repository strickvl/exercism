package isogram

import "strings"

func IsIsogram(s string) bool {
	mp := map[string]int{}
	for _, v := range strings.ToLower(s) {
		char := string(v)
		if strings.ContainsAny(char, " -") {
			continue
		} else {
			_, ok := mp[char]
			if ok {
				return false
			}
			mp[char] = 1
		}

	}

	return true
}
