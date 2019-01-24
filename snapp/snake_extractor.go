package main

import (
	"encoding/csv"
	_ "encoding/csv"
	"encoding/json"
	"fmt"
	"io/ioutil"
	"os"
	"strconv"
	"strings"
)

type Snake struct {
	Binomial string  `json:"name"`// index 3
	Family string `json:"family"`//index 2
	Genus string `json:"genus"` //index 1
	AllNames SnakeSynonyms `json:"allNames"`
}
type SnakeSynonyms struct {
	Name string `json:"binomial"`
	Synonyms []string `json:"synonyms"` //12 > ? (must test for  number of columns  with text(or use no_syn at index 9)
}

func handleErr(err error) {
	if err != nil {
		panic(err)
	}
}

func loadCSV(csvLoc string) () {
	f, err := os.Open(csvLoc)
	handleErr(err)
	defer f.Close()
	reader := csv.NewReader(f)
	_, err = reader.Read()
	lines, err := reader.ReadAll()
	handleErr(err)
	fmt.Println(len(lines))
	snakes := make([]Snake, len(lines))
	for index, line := range lines {
		if len(strings.TrimSpace(line[3])) == 0 {
			continue
		}
		binomial := strings.TrimSpace(line[3])
		family := strings.Trim(line[2], " ")
		genus := strings.Trim(line[1], " ")
		numSynonymsStr := line[9]
		if len(numSynonymsStr) > 0 {
			numSynonyms, err := strconv.Atoi(numSynonymsStr)
			handleErr(err)
			synonyms := make([]string, numSynonyms)
			if numSynonyms > 0 {
				synLength := 0
				for i := 12; i < 12+numSynonyms; i++ {
					syn := strings.TrimSpace(line[i])

					if strings.Contains(syn, "?") == false  && len(syn) != 0 && strings.Compare(syn, binomial) != 0 && strings.Compare(syn, "NA") != 0 {
						fmt.Println(len(syn), syn)
						synonyms[synLength] = syn
						synLength++
					}
				}
				a := SnakeSynonyms{Name:binomial, Synonyms:synonyms}
				s := Snake{Binomial: binomial, Family: family, Genus: genus, AllNames: a}
				snakes[index] = s
			}
		}
		//fmt.Println(binomial, family, genus, numSynonyms)
	}
	snakeJson, _ := json.MarshalIndent(snakes, "", " ")
	err = ioutil.WriteFile("/Users/encima/dev/go/uzh_tools/snapp/data/snakes.json", snakeJson, 0644)
	handleErr(err)
}

func parseSnakes(line []string) (s Snake) {
	s = Snake{}
	return s
}

func main() {
	loadCSV("/Users/encima/dev/go/uzh_tools/snapp/data/trd18-splitted-synonyms-jagged-families.csv")
}
