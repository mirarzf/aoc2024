#include <string>
#include <sstream>
#include <vector>
#include <bits/stdc++.h>

#include "Puzzle03.hpp"
#include "Grid.hpp"

using namespace std; 

// Constructors 
Puzzle03::Puzzle03() : input("") {} 

Puzzle03::Puzzle03(string newinput) {
    input = newinput; 
}

// Getters 
string Puzzle03::getSolution(int puzzlepart) {
    Grid enginegrid = Grid(input); 
    long long unsigned int sum = enginegrid.getSumPartNextToSymbol(); 

    if (puzzlepart == 1) {
        return to_string(sum); 
    } else {
        return to_string(0); 
    }; 
}