#include <string>
#include <sstream>
#include <vector>
#include <bits/stdc++.h>

#include "Puzzle02.hpp"

using namespace std; 

// Constructors 
Puzzle02::Puzzle02() : input("") {} 

Puzzle02::Puzzle02(string newinput) {
    input = newinput; 
}

// Getters 
string Puzzle02::getSolution(int puzzlepart) {
    stringstream ss(input); 
    string row; 
    int sumValidIDs = 0; 
    long long unsigned int sumPower = 0; 
    
    while (ss.good()) { 
        getline(ss, row); 
        if (row.size() > 0) { 
            Game gamerow = Game(row); 
            if (puzzlepart == 1 && gamerow.isGamePossibleWith(12, 13, 14)) { 
                sumValidIDs = sumValidIDs + gamerow.getID(); 
            };
            if (puzzlepart == 2) { 
                int power = gamerow.getRed() * gamerow.getGreen() * gamerow.getBlue(); 
                sumPower = sumPower + (long long unsigned int) power; 
            }
        }; 
    }; 

    if (puzzlepart == 1) {
        return to_string(sumValidIDs); 
    } else {
        return to_string(sumPower); 
    }; 
}