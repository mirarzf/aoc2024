#ifndef DEF_PUZZLE03
#define DEF_PUZZLE03

#include <string>

#include "Part.hpp"

class Puzzle03 {
    private: 
    std::string input; 
    
    public: 
    // Constructors 
    Puzzle03(); 
    Puzzle03(std::string newinput); 

    // Getters 
    std::string getSolution(int puzzlepart); 
}; 

#endif 