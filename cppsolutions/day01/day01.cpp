#include <fstream>
#include <iostream>
#include <sstream>
#include <string> 
#include <vector>
#include <bits/stdc++.h>

// INCLUDE HERE THE NECESSARY CLASSES 
#include "Puzzle01.hpp"

using namespace std;

int main () { 
    /* Instantiation of the file */ 
    string filename; 
    cout << "Filename of the input in input folder: "; 
    cin >> filename; 
    filename = "../../input/" + filename; 
    cout << "Opening the file " << filename << "\n"; 

    /* Instantiate the puzzle class */
    ifstream file; 
    file.open(filename); 

    stringstream ss; 
    string line; 
    while (file.good()) { 
        getline(file, line);
        ss << line; 
        ss << "\n"; 
    } 
    file.close(); 
    
    Puzzle01 puzzle = Puzzle01(ss.str()); 

    cout << "Currently calculating the solution... \n"; 

    // Solution to puzzle 1 : 
    cout << "The solution to part one is: " << puzzle.getSolution(1) << "\n"; 
    // Solution to puzzle 2 : 
    cout << "The solution to part two is: " << puzzle.getSolution(2) << "\n"; 

    cout << "Tap x and enter to close the program. \n";
    char wait;
    cin >> wait; 

    return 0; 
} 