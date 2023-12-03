#include <vector> 
#include <string> 
#include <sstream> 

#include "Grid.hpp" 
#include "Part.hpp"

using namespace std; 

// Constructors 

Grid::Grid(string input) { 
    long long unsigned int lineCounter = 0; 
    schematic = {};    
    partlist = {};  
    
    bool addNewPart = true; 
    long long unsigned int partNb = 1; 

    stringstream ssInput(input); 
    string line; 
    while (ssInput.good()) {
        getline(ssInput, line); 
        if (line.size() > 0) { 

            if (lineCounter == 0) { 
                ncol = line.size(); 
            }; 
            
            lineCounter++; 

            for (long long unsigned int i = 0; i < ncol; i++) {
                if (int(line[i]) > 47 && int(line[i]) < 58) { 
                    if (addNewPart) { 
                        partNb++; 
                        Part* partPtr = new Part(i, int(line[i])-48); 
                        partlist.push_back(partPtr); 
                        addNewPart = false; 
                    } else { 
                        Part* partPtr = partlist[partNb-2]; 
                        partPtr->addDigitToPart(i, int(line[i]-'0')); 
                    }; 
                    schematic.push_back(partNb); 
                } else if (line[i] == '.') { 
                    schematic.push_back(0); 
                    if (!addNewPart) { 
                        addNewPart = true; 
                    }; 
                } else { // line[i] is a symbol
                    schematic.push_back(1);
                    if (!addNewPart) { 
                        addNewPart = true; 
                    }; 
                }; 
            }; 
        }; 
    }; 

    nrow = lineCounter;  

    // Modify the "Part"s that are pointed to to say if they are adjacent to a symbol or not 
    long long unsigned int indexToCheck = 0; 
    for (long long unsigned int index = 0; index < ncol*nrow; index++) { 
        if (schematic[index] == 1) { 
            long long unsigned int i = index / ncol; 
            long long unsigned int j = index % ncol; 

            if (i>0) {
                if (j>0) { 
                    indexToCheck = (i-1)*ncol + j-1; 
                    if (schematic[indexToCheck] > 1) { 
                        Part* partPtr = partlist[schematic[indexToCheck]-2]; 
                        partPtr->changeAdjacentStatus(true); 
                    }; 
                }; 
                
                indexToCheck = (i-1)*ncol + j; 
                if (schematic[indexToCheck] > 1) { 
                    Part* partPtr = partlist[schematic[indexToCheck]-2]; 
                    partPtr->changeAdjacentStatus(true); 
                }; 
                
                if (j+1<ncol) { 
                    indexToCheck = (i-1)*ncol + j+1; 
                    if (schematic[indexToCheck] > 1) { 
                        Part* partPtr = partlist[schematic[indexToCheck]-2]; 
                        partPtr->changeAdjacentStatus(true); 
                    }; 
                }; 
            }; 

            if (j>0) { 
                indexToCheck = i*ncol + j-1; 
                if (schematic[indexToCheck] > 1) { 
                    Part* partPtr = partlist[schematic[indexToCheck]-2]; 
                    partPtr->changeAdjacentStatus(true); 
                }; 
            }; 
            
            if (j+1<ncol) { 
                indexToCheck = i*ncol + j+1; 
                if (schematic[indexToCheck] > 1) { 
                    Part* partPtr = partlist[schematic[indexToCheck]-2]; 
                    partPtr->changeAdjacentStatus(true); 
                }; 
            }; 

            if (i+1<nrow) {
                if (j>0) { 
                    indexToCheck = (i+1)*ncol + j-1; 
                    if (schematic[indexToCheck] > 1) { 
                        Part* partPtr = partlist[schematic[indexToCheck]-2]; 
                        partPtr->changeAdjacentStatus(true); 
                    }; 
                }; 
                
                indexToCheck = (i+1)*ncol + j; 
                if (schematic[indexToCheck] > 1) { 
                    Part* partPtr = partlist[schematic[indexToCheck]-2]; 
                    partPtr->changeAdjacentStatus(true); 
                }; 
                
                if (j+1<ncol) { 
                    indexToCheck = (i+1)*ncol + j+1; 
                    if (schematic[indexToCheck] > 1) { 
                        Part* partPtr = partlist[schematic[indexToCheck]-2]; 
                        partPtr->changeAdjacentStatus(true); 
                    }; 
                }; 
            }; 
        }; 
    }; 
    
}

// Destructor 
Grid::~Grid() { 
    for (long long unsigned int i = 0; i < partlist.size(); i++) { 
        delete partlist[i]; 
    }
}; 

// Getters 

vector<long long unsigned int> Grid::getSchematic() { 
    return schematic; 
}

vector<Part*> Grid::getPartList() { 
    return partlist; 
}

long long unsigned int Grid::getNCol() { 
    return ncol; 
}

long long unsigned int Grid::getNRow() { 
    return nrow; 
}

long long unsigned int Grid::getSumPartNextToSymbol() { 
    long long unsigned int sum = 0; 
    for (Part* partPtr: partlist) { 
        if (partPtr->isAdjacentToSymbol()) { 
            sum += partPtr->getPartNumber(); 
        }; 
    }; 
    return sum; 
}