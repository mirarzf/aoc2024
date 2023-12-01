#include <string>
#include <sstream>
#include <vector>
#include <bits/stdc++.h>

#include "Puzzle01.hpp"

using namespace std; 

// Constructors 
Puzzle01::Puzzle01() : input("") {} 

Puzzle01::Puzzle01(string newinput) {
    input = newinput; 
}

// Getters 
string Puzzle01::getSolution(int puzzlepart) {
    stringstream ss(input); 
    string row; 

    string digitstext[9] = {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"}; 

    int firstDigit = 0;
    int lastDigit = 0; 

    size_t posFirstDigit = string::npos; 
    size_t posLastDigit = 0; 

    bool first = true;  
    int sumDigits = 0; 
    
    while (ss.good()) { 
        getline(ss, row); 
        first = true; 
        for(size_t i = 0; i < row.length(); i++) {
            if ( int(row[i]) > 47 && int(row[i]) < 58 ) {
                if (first) {
                    firstDigit = int(row[i])-48; 
                    posFirstDigit = i; 
                    first = false; 
                }; 
                lastDigit = int(row[i])-48; 
                posLastDigit = i; 
            }; 

            if (puzzlepart == 2) {
                for(size_t index=0; index < 9; index++) {
                    size_t foundFirst = row.find(digitstext[index]); 
                    if (foundFirst != string::npos && foundFirst < posFirstDigit) {
                        posFirstDigit = foundFirst; 
                        firstDigit = (int) index+1; 
                    }; 

                    size_t foundLast = row.rfind(digitstext[index]); 
                    if (foundLast != string::npos && foundLast > posLastDigit) {
                        posLastDigit = foundLast; 
                        lastDigit = (int) index+1; 
                    }; 
                }; 
            }; 
        }; 
        sumDigits = sumDigits + 10*firstDigit + lastDigit; 
        firstDigit = 0; 
        lastDigit = 0; 
        posFirstDigit = string::npos; 
        posLastDigit = 0; 
    }
    return to_string(sumDigits); 
}