// Package gigasecond takes a start date and time and returns the value plus a gigasecond.
package gigasecond

// import path for the time package from the standard library.
import "time"

// AddGigasecond is the main function of the package.
func AddGigasecond(t time.Time) time.Time {
	start := t
	gigavalue := start.Add(time.Second * (10 ^ 9))
	return gigavalue
}
