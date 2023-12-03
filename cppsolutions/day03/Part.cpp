#include <string> 
#include <vector> 
#include <cmath> 

#include "Part.hpp"

using namespace std; 

// Constructors 

Part::Part(long long unsigned int locationID, int digit) {
    partLocations = {locationID}; 
    partDigits = {digit}; 
    adjacentToSymbol = false; 
}; 

// Getters 

vector<long long unsigned int> Part::getPartLocations() { 
    return partLocations; 
}; 

long long unsigned int Part::getPartNumber() { 
    long long unsigned int n = partDigits.size(); 
    long long unsigned int partNb = 0; 
    for (long long unsigned int i = 0; i < n; i++) {
        partNb += (long long unsigned int) partDigits[i]*pow(10.0, n-1-i); 
    }; 
    return partNb; 
}; 

bool Part::isAdjacentToSymbol() { 
    return adjacentToSymbol; 
}; 

// Setters 

void Part::addDigitToPart(long long unsigned int location, int digit) { 
    partLocations.push_back(location); 
    partDigits.push_back(digit); 
}; 

void Part::changeAdjacentStatus(bool newstatus) { 
    adjacentToSymbol = newstatus; 
}; 