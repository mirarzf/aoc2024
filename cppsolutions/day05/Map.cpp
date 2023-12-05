#include <vector>
#include <string>
#include <sstream> 

#include "Map.hpp"

using namespace std; 

//Constructors 

Map::Map() : sourceID("source"), destID("dest"), sourceStarts({0}), destStarts({0}), mapRanges({1}) {} 

Map::Map(string input) { 
    stringstream ssInput(input); 
    string id; 
    getline(ssInput, id, '-'); 
    sourceID = id; 
    getline(ssInput, id, '-'); 
    getline(ssInput, id, ' '); 
    destID = id; 
    getline(ssInput, id); 
    while (ssInput.good()) {
        string line; 
        getline(ssInput, line); 
        if (line.size() > 0) {
            stringstream ssLine(line); 
            long long unsigned int nb; 
            ssLine >> nb; 
            destStarts.push_back(nb); 
            ssLine >> nb; 
            sourceStarts.push_back(nb); 
            ssLine >> nb; 
            mapRanges.push_back(nb); 
        }; 
    }; 
} 

// Getters 

vector<long long unsigned int> Map::getDestNbs(vector<long long unsigned int> sourceNbs) { 
    vector<long long unsigned int> destNbs = {}; 
    for (unsigned j = 0; j < sourceNbs.size(); j++) {
        long long unsigned int sourceNb = sourceNbs[j];  
        unsigned i = 0; 
        while (i < sourceStarts.size()) { 
            if (sourceNb > sourceStarts[i] && sourceNb < sourceStarts[i]+mapRanges[i]) { 
                destNbs.push_back(sourceNb + destStarts[i]-sourceStarts[i]); 
            }; 
            i++; 
        }; 
        if (destNbs.size() == j) { 
            destNbs.push_back(sourceNb); 
        }
    }; 
    return destNbs; 
}