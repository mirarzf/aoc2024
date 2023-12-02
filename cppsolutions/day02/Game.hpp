#ifndef GAME
#define GAME

#include <string>

class Game { 
    private: 
    int gameID; 
    int red; 
    int green; 
    int blue; 

    public: 
    // Constructors 
    Game(); 
    Game(std::string gamerow); 

    // Getters 
    int getID(); 
    int getRed(); 
    int getGreen(); 
    int getBlue(); 
    bool isGamePossibleWith(int amountRed, int amountGreen, int amountBlue); 

    // Setters 
    void setRed(int amount); 
    void setGreen(int amount); 
    void setBlue(int amount); 
}; 

#endif