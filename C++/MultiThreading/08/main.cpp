#include <iostream>
#include <thread>
#include <vector>
#include <algorithm>
#include <memory>
#include <chrono>

#include <SFML/Graphics.hpp>

using namespace std;


vector<int> grid;

vector<unique_ptr<sf::Shape>> shapes;

bool isRunning = true;

void update_grid(int x, int y){

    while(isRunning){
        this_thread::sleep_for(chrono::milliseconds(1000));
    }
}