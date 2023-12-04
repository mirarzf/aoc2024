#include <string>
#include <sstream>
#include <vector>
#include <bits/stdc++.h>
#include <cmath>

#include "Puzzle04.hpp"
#include "Scratchcard.hpp"

using namespace std; 

// Constructors 
Puzzle04::Puzzle04() : input("") {} 

Puzzle04::Puzzle04(string newinput) {
    input = newinput; 
}

// Getters 
string Puzzle04::getSolution(int puzzlepart) {
    stringstream inputSS(input); 
    int somme = 0; 
    int nbOfCards = 0; 
    vector<int> pointsPerCard = {}; 
    while (inputSS.good()) { 
        string cardInput; 
        getline(inputSS, cardInput); 
        if (cardInput.size() > 0) {
            nbOfCards++; 
            Scratchcard card = Scratchcard(cardInput); 
            int points = card.getNbMatches(); 

            if (points > 0) { 
                somme += pow(2, points-1); 
            }; 
            pointsPerCard.push_back(points); 
        }; 
    }; 

    if (puzzlepart == 1) {
        return to_string(somme); 
    } else { // puzzlepart == 2 
        int cardAmount[nbOfCards]; 
        somme = 0; 
        for (int i = 0; i<nbOfCards; i++) { 
            cardAmount[i] = 1; 
        }; 
        for (int i = 0; i<nbOfCards; i++) { 
            for (int j = 0; j<pointsPerCard[i]; j++) { 
                cardAmount[i+j+1]+=cardAmount[i]; 
            }
            somme += cardAmount[i]; 
        }
        return to_string(somme); 
    }; 
}