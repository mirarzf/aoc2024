#ifndef ENGINE_PART
#define ENGINE_PART 

#include <string> 
#include <vector> 

class Part {
    private: 
    std::vector<long long unsigned int> partLocations; 
    std::vector<int> partDigits; 
    bool adjacentToSymbol; 

    public: 
    // Constructors 
    Part() : partLocations(0), partDigits(0), adjacentToSymbol(false) {}; 
    Part(long long unsigned int locationID, int digit); 

    // Getters 
    std::vector<long long unsigned int> getPartLocations(); 
    long long unsigned int getPartNumber(); 
    bool isAdjacentToSymbol(); 

    // Setters 
    void addDigitToPart(long long unsigned int location, int digit); 
    void changeAdjacentStatus(bool newstatus); 
}; 

#endif 