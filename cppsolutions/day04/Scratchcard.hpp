#ifndef DEF_SCRATCHCARD
#define DEF_SCRATCHCARD

#include <string> 
#include <vector>
#include <sstream> 

class Scratchcard { 
    private: 
    std::vector<int> winningNb; 
    std::vector<int> myNb; 

    public: 
    // Constructors 
    Scratchcard(); 
    Scratchcard(std::string input); 

    // Getters 
    int getNbMatches(); 
}; 

#endif 