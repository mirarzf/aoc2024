#include <vector>
#include <string>
#include <sstream>

#include "Scratchcard.hpp" 

using namespace std; 

// Constructors 

Scratchcard::Scratchcard() : winningNb({0}), myNb({0}) {} 

Scratchcard::Scratchcard(string input) {
    winningNb = {}; 
    stringstream ssInput(input); 
    string winningNbString; 
    getline(ssInput, winningNbString, ':'); 
    getline(ssInput, winningNbString, '|'); 
    stringstream ssWinningNb(winningNbString.substr(0, winningNbString.size()-1)); 
    while(ssWinningNb.good()) { 
        int nb; 
        ssWinningNb >> nb; 
        winningNb.push_back(nb); 
    }; 
    string myNbString; 
    getline(ssInput, myNbString); 
    stringstream ssMyNb(myNbString); 
    while(ssMyNb.good()) { 
        int nb; 
        ssMyNb >> nb; 
        myNb.push_back(nb); 
    }; 
}

// Getters 

int Scratchcard::getNbMatches() { 
    int counter = 0; 
    for (int nb : myNb) { 
        for (int wnb : winningNb) {
            if (nb == wnb) { 
                counter++; 
            }; 
        }; 
    }; 
    return counter; 
}