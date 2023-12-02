#ifndef DEF_PUZZLE02
#define DEF_PUZZLE02

#include <string>

#include "Game.hpp"

class Puzzle02 {
    private: 
    std::string input; 
    
    public: 
    // Constructors 
    Puzzle02(); 
    Puzzle02(std::string newinput); 

    // Getters 
    std::string getSolution(int puzzlepart); 
}; 

#endif 