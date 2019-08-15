package main

import (
	// "database/sql"
	"fmt"
	// _ "github.com/mattn/go-sqlite3"
	// "log"
	"os"
	"os/exec"
	"path/filepath"
	"time"
	"strings"
	"io/ioutil"
)

type Video struct {
	Path    string
	Name    string
	ModTime time.Time
}

var vids []os.FileInfo
var dirs []string
var relatedGroups [][]string
var outFile os.File
var maxGap time.Duration = 1 * time.Minute

func walkDir(path string, info os.FileInfo, err error) error {
	if err != nil {
		fmt.Printf("prevent panic by handling failure accessing a path %q: %v \n", path, err)
		return err
	}

	if info.IsDir() {
		dirs = append(dirs, path)
	}
	return nil
}

func diffCalc(src time.Time, cmp time.Time) time.Duration {
	if cmp.After(src) {
		src, cmp = cmp, src
	}

	return src.Sub(cmp)
}

func checkDiff(src os.FileInfo, cmp os.FileInfo) bool {
	diff := diffCalc(src.ModTime(), cmp.ModTime())
	if diff <= maxGap && src.Name() != cmp.Name() && strings.Contains(cmp.Name(), "AVI") {
		return true
	}
	return false
}



func main() {
	outFile, err := os.OpenFile("all_files.txt", os.O_CREATE|os.O_APPEND|os.O_WRONLY, 0600)
	if err != nil {
		panic(err)
	}
	defer outFile.Close()

	srcDir := "/mnt/data/uploads/mustelids/"
	err := filepath.Walk(srcDir, walkDir)
	if err != nil {
		fmt.Printf("error walking the path %q: %v\n", srcDir, err)
		return
	}

	for dirInd := range(dirs) {
		dir := dirs[dirInd]
		vids, err := ioutil.ReadDir(dir)
		if err != nil {
			panic(err)
		}

		for srcInd := 0; srcInd < len(vids) - 1; srcInd++ {
			src := vids[srcInd]
			var related []string
			if strings.Contains(src.Name(), "AVI") {
				rangeRelated := 1
				if _, err = outFile.WriteString(fmt.Sprintf("%s/%s,", dir, src.Name())); err != nil {
					panic(err)
				}
				cmp := vids[srcInd+rangeRelated]
				for checkDiff(src, cmp) {
					rangeRelated++
					fmt.Sprintf("%s %s", src, cmp)
					if srcInd+rangeRelated < len(vids) {
						src = cmp
						cmp = vids[srcInd+rangeRelated]
						if _, err = outFile.WriteString(fmt.Sprintf("%s/%s,", dir, cmp.Name())); err != nil {
							panic(err)
						}
					} else {
						break
					}
				}
				if _, err = outFile.WriteString("\n"); err != nil {
					panic(err)
				}
				srcInd = srcInd + rangeRelated
			}
		}
	}
}
