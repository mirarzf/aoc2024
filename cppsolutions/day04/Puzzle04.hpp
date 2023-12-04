#ifndef DEF_PUZZLE04
#define DEF_PUZZLE04

#include <string>

class Puzzle04 {
    private: 
    std::string input; 
    
    public: 
    // Constructors 
    Puzzle04(); 
    Puzzle04(std::string newinput); 

    // Getters 
    std::string getSolution(int puzzlepart); 
}; 

#endif 