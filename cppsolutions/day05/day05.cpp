#include <fstream>
#include <iostream>
#include <sstream>
#include <string> 
#include <vector>
#include <bits/stdc++.h>

// INCLUDE HERE THE NECESSARY CLASSES 
#include "Puzzle05.hpp"

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
    
    Puzzle05 puzzle = Puzzle05(ss.str()); 

    cout << "Currently calculating the solution... \n"; 

    // Solution to part 1 : 19135
    cout << "The solution to part one is: " << puzzle.getSolution(1) << "\n"; 
    // Solution to part 2 : 5704953
    cout << "The solution to part two is: " << puzzle.getSolution(2) << "\n"; 

    cout << "Tap x and enter to close the program. \n";
    char wait;
    cin >> wait; 

    return 0; 
} 