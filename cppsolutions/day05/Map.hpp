#ifndef DEF_SOURCETODESTMAP
#define DEF_SOURCETODESTMAP

#include <string>
#include <vector>

class Map { 
    private: 
    std::string sourceID; 
    std::string destID; 
    std::vector<int> sourceStarts; 
    std::vector<int> destStarts; 
    std::vector<int> mapRanges; 

    public:

    // Constructors  
    Map(); 
    Map(std::string input); 

    // Getters 
    std::vector<int> getDestNbs(std::vector<int> sourceNbs);
}; 

#endif 