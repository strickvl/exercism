// Package twofer should have a package comment that summarizes what it's about.
package twofer

import "fmt"

// ShareWith returns a string depending on what is passed in as input
func ShareWith(name string) (final string) {
	finalStr := "One for %s, one for me."

	if name != "" {
		return fmt.Sprintf(finalStr, name)
	}
	return fmt.Sprintf(finalStr, "you")
}
