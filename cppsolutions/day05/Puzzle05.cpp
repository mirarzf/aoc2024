#include <string>
#include <sstream>
#include <vector>
#include <bits/stdc++.h>
#include <cmath>

#include "Puzzle05.hpp"
#include "Map.hpp"

using namespace std; 

// Constructors 
Puzzle05::Puzzle05() : input("") {} 

Puzzle05::Puzzle05(string newinput) {
    input = newinput; 
}

// Getters 
string Puzzle05::getSolution(int puzzlepart) {
    vector<int> seeds = {}; 
    stringstream ssInput(input); 
    string seedsline; 
    getline(ssInput, seedsline, ':'); 
    getline(ssInput, seedsline); 
    stringstream ssSeeds(seedsline); 
    while (ssSeeds.good()) { 
        int nb; 
        ssSeeds >> nb; 
        seeds.push_back(nb); 
    }; 

    vector<Map*> mapsPtr; 

    string line; 
    getline(ssInput, line); 
    while(ssInput.good()) { 
        string mapInput; 
        getline(ssInput, line); 
        while(!line.empty()) { 
            mapInput.append(line); 
            mapInput.append("\n"); 
            getline(ssInput, line); 
        }; 
        Map* mapPtr = new Map(mapInput); 
        mapsPtr.push_back(mapPtr); 
    }; 

    for (unsigned i = 0; i < mapsPtr.size(); i++) { 
        seeds = mapsPtr[i]->getDestNbs(seeds); 
    }; 
    unsigned mini; 
    for (unsigned i = 0; i < seeds.size(); i++) { 
        if (seeds[i] < mini) { 
            mini = seeds[i]: 
        }
    }

    for (unsigned i = 0; i < mapsPtr.size(); i++) {
        delete mapsPtr[i]; 
    }; 

    if (puzzlepart == 1) {
        return to_string(0); 
    } else { // puzzlepart == 2 
        return to_string(0); 
    }; 
}