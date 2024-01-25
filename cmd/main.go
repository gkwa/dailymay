package main

import (
	"os"

	"github.com/taylormonacelli/dailymay"
)

func main() {
	code := dailymay.Execute()
	os.Exit(code)
}
