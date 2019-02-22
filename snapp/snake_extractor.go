package main

import (
	"encoding/csv"
	_ "encoding/csv"
	"encoding/json"
	"fmt"
	"io/ioutil"
	"os"
	"strings"
)

// Snake structure to hold the contents describing the animal
type Snake struct {
	Family   string        `json:"family"` //index 2
	Genus    string        `json:"genus"`  //index 1
	AllNames SnakeSynonyms `json:"allNames"`
}

// SnakeSynonyms structure to hold the original name and associated (unique) synonyms
type SnakeSynonyms struct {
	Name       string   `json:"binomial"`
	CommonName string   `json:"commonName"`
	Synonyms   []string `json:"synonyms"` //12 > ? (must test for  number of columns  with text(or use no_syn at index 9)
}

func handleErr(err error) {
	if err != nil {
		panic(err)
	}
}

func stringExists(needle string, haystack []string) bool {
	for _, h := range haystack {
		if strings.ToLower(needle) == strings.ToLower(h) {
			return true
		}
	}
	return false
}

func loadCSV(csvLoc string) {
	f, err := os.Open(csvLoc)
	handleErr(err)
	defer f.Close()
	reader := csv.NewReader(f)
	_, err = reader.Read()
	lines, err := reader.ReadAll()
	handleErr(err)
	fmt.Println(len(lines))
	snakes := make([]Snake, len(lines))
	snakeLength := 0
	for index, line := range lines {
		if len(strings.TrimSpace(line[3])) == 0 {
			continue
		}
		binomial := strings.TrimSpace(line[4])
		family := strings.Trim(line[2], " ")
		if len(family) == 0 {
			fmt.Println(family, index)
		}
		genus := strings.Trim(line[3], " ")
		commonName := strings.Trim(line[44], " ")
		if commonName == "NA" {
			commonName = ""
		}
		synonymSplit := strings.Split(line[46], ",")
		synonyms := make([]string, len(synonymSplit))
		if strings.Contains(line[46], "NA") == false {
			synLength := 0
			for i := 0; i < len(synonymSplit); i++ {
				if len(synonymSplit[i]) > 0 {
					synonyms[synLength] = strings.Trim(synonymSplit[i], " ")
					synLength++
				}
			}
			synonyms = append([]string(nil), synonyms[:synLength]...)
		}
		if len(synonyms) == 1 && synonyms[0] == "" {
			synonyms = nil
		}
		a := SnakeSynonyms{Name: binomial, Synonyms: synonyms, CommonName: commonName}
		s := Snake{Family: family, Genus: genus, AllNames: a}
		snakes[index] = s
		snakeLength++

		// numSynonymsStr := line[9]
		// if len(numSynonymsStr) > 0 {
		// 	numSynonyms, err := strconv.Atoi(numSynonymsStr)
		// 	handleErr(err)

		// 	if numSynonyms > 0 {
		// 		synLength := 0
		// 		for i := 12; i < 12+numSynonyms; i++ {
		// 			syn := strings.TrimSpace(line[i])
		// 			// TODO ignore existing synonyms
		// 			if strings.Contains(syn, "?") == false && len(syn) != 0 && strings.Compare(syn, binomial) != 0 && strings.Compare(syn, "NA") != 0 && !stringExists(syn, synonyms) {
		// 				fmt.Println(len(syn), syn)
		// 				syn = strings.Replace(syn, "(", "", -1)
		// 				synonyms[synLength] = syn
		// 				synLength++
		// 			}
		// 		}
		// 		synonyms = append([]string(nil), synonyms[:synLength]...)
		// 		a := SnakeSynonyms{Name: binomial, Synonyms: synonyms}
		// 		s := Snake{Family: family, Genus: genus, AllNames: a}
		// 		snakes[index] = s
		// 		snakeLength++
		// 	}
		// }
	}
	snakes = append([]Snake(nil), snakes[:snakeLength]...)
	snakeJSON, _ := json.MarshalIndent(snakes, "", " ")
	err = ioutil.WriteFile("./data/snakes.json", snakeJSON, 0644)
	handleErr(err)
}

func parseSnakes(line []string) (s Snake) {
	s = Snake{}
	return s
}

func main() {
	loadCSV("./data/trd18-splitted-synonyms-jagged-families_amd_mod_withHM.csv")
}
