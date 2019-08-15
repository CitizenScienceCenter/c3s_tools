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

	if info.IsDir() && strings.Contains(info.Name(), "AVI") {
	    output := strings.Replace(src.Name(), ".AVI", ".mp4", -1)
        cmdString := fmt.Sprintf("ffmpeg -i %s/%s %s/%s", dir, src.Name(), dir, output)
        err = runCmd(cmdString)
        if err != nil {
            fmt.Println(err)
            break
        }
        output = strings.Replace(src.Name(), ".AVI", ".jpg", -1)
        cmdString = fmt.Sprintf("ffmpeg -ss 00:05:00 -i %s/%s -vframes 1 -q:v 2 %s/%s", dir, src.Name(), dir, output)
        err = runCmd(cmdString)
        if err != nil {
            fmt.Println(err)
            break
        }
	}
	return nil
}

func runCmd(cmdString string) error {
    cmdArgs := strings.Fields(cmdString)
    fmt.Println(cmdString)
    cmd := exec.Command(cmdArgs[0], cmdArgs[1:]...)
    err := cmd.Start()
    if err != nil {
        fmt.Println(err)
        return err
    }
    err = cmd.Wait()
    if err != nil {
        fmt.Println(err)
        return err
    }
    return nil
}

func main() {
	srcDir := "/mnt/data/uploads/mustelids/"
	err := filepath.Walk(srcDir, walkDir)
	if err != nil {
		fmt.Printf("error walking the path %q: %v\n", srcDir, err)
		return
	}
}
