package main

import (
	"fmt"
	"os"
	"path/filepath"
)

var vids = make([]os.File, 100)

func walkDir(path string, info os.FileInfo, err error) error {
	if err != nil {
		fmt.Printf("prevent panic by handling failure accessing a path %q: %v \n", path, err)
		return err
	}
	if !info.IsDir() && info.Name() != "sample_data" {
		fmt.Printf("%s, %s, %dMB", info.Name(), info.ModTime().String(), (info.Size()/1024)/1024)
		fmt.Printf(" visited file or dir: %q \n", path)

	}

	return nil
}

func main() {

	srcDir := "./sample_data"
	err := filepath.Walk(srcDir, walkDir)
	if err != nil {
		fmt.Printf("error walking the path %q: %v\n", srcDir, err)
		return
	}
}
