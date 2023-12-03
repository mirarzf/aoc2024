#ifndef ENGINE_GRID
#define ENGINE_GRID 

#include <string> 
#include <vector> 

#include "Part.hpp"

class Grid {
    private: 
    long long unsigned int ncol; 
    long long unsigned int nrow; 
    std::vector<long long unsigned int> schematic; 
    std::vector<Part*> partlist; 

    public: 
    // Constructors 
    Grid(std::string input); 

    // Destructor 
    ~Grid(); 

    // Getters 
    std::vector<long long unsigned int> getSchematic(); 
    std::vector<Part*> getPartList(); 
    long long unsigned int getNCol(); 
    long long unsigned int getNRow(); 
    long long unsigned int getSumPartNextToSymbol(); 
}; 

#endif 