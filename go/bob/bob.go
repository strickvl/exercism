// Package bob should have a package comment that summarizes what it's about.
package bob

import (
	"strings"
	"regexp"
)

// TransformRemark removes any spacing characters
func TransformRemark(remark string) string {
	return strings.Trim(remark, "\n\t \r")
}

// IsAllCaps checks whether a string has any letter characters and
// whether they are all upper case or not
func IsAllCaps(remark string) bool {
	re := regexp.MustCompile(`[A-Za-z]`)
	charCount := len(re.FindAll([]byte(remark), -1))
	
	if strings.ToUpper(remark) == remark && charCount > 0 {
		return true
	}
	return false
}

// IsQuestion checks whether a string has a question mark at the end
func IsQuestion(remark string) bool {
	finalChar := string(remark[len(remark) - 1])

	if finalChar == "?" {
		return true
	}
	return false
}

// IsShoutingQuestion checks whether a statement is a question
// and is all upper case
func IsShoutingQuestion(remark string) bool {
	finalChar := string(remark[len(remark) - 1])

	if finalChar == "?" && IsAllCaps(remark) {
		return true
	}
	return false
}

// HasNoCharacters checks for empty strings
func HasNoCharacters(remark string) bool {
	if remark == "" {
		return true
	}
	return false
}

// Hey checks the content of a remark and
// returns a response depending on what was passed in
func Hey(remark string) string {
	remark = TransformRemark(remark)

	if HasNoCharacters(remark) {
		return "Fine. Be that way!"
	} else if IsShoutingQuestion(remark) {
		return "Calm down, I know what I'm doing!"
	} else if IsQuestion(remark) {
		return "Sure."
	} else if IsAllCaps(remark) {
		return "Whoa, chill out!"
	} else {
		return "Whatever."
	}
	return remark
}
