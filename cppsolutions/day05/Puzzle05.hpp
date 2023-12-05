#ifndef DEF_PUZZLE05
#define DEF_PUZZLE05

#include <string>

class Puzzle05 {
    private: 
    std::string input; 
    
    public: 
    // Constructors 
    Puzzle05(); 
    Puzzle05(std::string newinput); 

    // Getters 
    std::string getSolution(int puzzlepart); 
}; 

#endif 