#include <string>
#include <sstream> 

#include "Game.hpp"

using namespace std; 

// Constructors 

Game::Game() : gameID(0), red(0), green(0), blue(0) {} 

Game::Game(string gamerow) { 
    int amountRed = 0; 
    int amountGreen = 0; 
    int amountBlue = 0; 
    red = 0; 
    green = 0; 
    blue = 0; 

    stringstream ssrow(gamerow); 
    string gameContent;
    getline(ssrow, gameContent, ':'); 
    gameID = stoi(gameContent.substr(5, gameContent.size()-5)); 
    getline(ssrow, gameContent, ':'); 

    stringstream ssGameContent(gameContent); 
    string match; 
    while(ssGameContent.good()) { 
        getline(ssGameContent, match, ';'); 

        stringstream ssMatchContent(match); 
        string marbles; 
        while(ssMatchContent.good()) { 
            getline(ssMatchContent, marbles, ','); 
            
            stringstream ssMarbles(marbles); 
            string marblesNb; 
            string marblesColor; 
            getline(ssMarbles, marblesNb, ' '); 
            getline(ssMarbles, marblesNb, ' '); 
            getline(ssMarbles, marblesColor); 
            if (marblesColor == "red") { 
                amountRed = stoi(marblesNb); 
                if (amountRed > red) { 
                    red = amountRed; 
                }
            } else if (marblesColor == "green") { 
                amountGreen = stoi(marblesNb); 
                if (amountGreen > green) { 
                    green = amountGreen; 
                }
            } else { 
                amountBlue = stoi(marblesNb); 
                if (amountBlue > blue) { 
                    blue = amountBlue; 
                }
            }
        }; 
    }; 
}; 

// Getters 
int Game::getID() { 
    return gameID; 
}; 

int Game::getRed() {
    return red; 
}; 

int Game::getGreen() { 
    return green; 
}; 

int Game::getBlue() { 
    return blue; 
}; 

bool Game::isGamePossibleWith(int amountRed, int amountGreen, int amountBlue) {
    return (red <= amountRed && green <= amountGreen && blue <= amountBlue); 
}; 

// Setters 

void Game::setRed(int amount) { 
    red = amount; 
}; 

void Game::setGreen(int amount) {
    green = amount; 
}; 

void Game::setBlue(int amount) { 
    blue = amount; 
}; 