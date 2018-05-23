package main

import "time"

func main() {
	AddGigasecond("1977-06-13")

}

func AddGigasecond(t time.Time) time.Time {
	start := t
	gigavalue := start.Add(time.Second * (10 ^ 9))
	return gigavalue
}
