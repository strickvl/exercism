// Package acronym should have a package comment that summarizes what it's about.
package acronym

import (
	"regexp"
	"strings"
)

func TransformString(s string) string {
	re := regexp.MustCompile(`[ ](\-)[ ]`)
	s = re.ReplaceAllString(s, " ")
	re1 := regexp.MustCompile(`[^A-Za-z \-]`)
	s = re1.ReplaceAllString(s, "")
	re2 := regexp.MustCompile(`[ ]{2,}`)
	s = re2.ReplaceAllString(s, " ")
	re3 := regexp.MustCompile(`\-`)
	s = re3 .ReplaceAllString(s, " ")
	
	return s
}

// Abbreviate turns a string into the acronym version of that same string
func Abbreviate(s string) string {
	words := strings.Split(TransformString(s), " ")
	acronym := ""

	for _, v := range words {
		acronym += strings.ToUpper(string(v[0]))
	}
	
	return acronym
}
