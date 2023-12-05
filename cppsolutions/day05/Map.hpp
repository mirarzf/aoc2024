#ifndef DEF_SOURCETODESTMAP
#define DEF_SOURCETODESTMAP

#include <string>
#include <vector>

class Map { 
    private: 
    std::string sourceID; 
    std::string destID; 
    std::vector<long long unsigned int> sourceStarts; 
    std::vector<long long unsigned int> destStarts; 
    std::vector<long long unsigned int> mapRanges; 

    public:

    // Constructors  
    Map(); 
    Map(std::string input); 

    // Getters 
    std::vector<long long unsigned int> getDestNbs(std::vector<long long unsigned int> sourceNbs);
}; 

#endif 