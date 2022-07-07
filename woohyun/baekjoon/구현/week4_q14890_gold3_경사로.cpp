#include <iostream>
#include <cstdlib>
using namespace std;

int width;
int inclineLength;
int road[102][102] = { 0, };
bool installed[102][102] = { false, };
int ways = 0;

void goRow(int row);
void goColumn(int col);

int main() {
    cin >> width >> inclineLength;

    for(int i=1; i<=width; i++) {
        for(int j=1; j<=width; j++) cin >> road[i][j];
    }

    for(int row=1; row<=width; row++) goRow(row);

    for(int i=0; i<102; i++) {
        for(int j=0; j<102; j++) installed[i][j] = false;
    }

    for(int col=1; col<=width; col++) goColumn(col);

    cout << ways << endl;

    return 0;
}

void goRow(int row) {
    for(int col=1; col<width; col++) {
        int floor = road[row][col];
        int nextFloor = road[row][col+1];
        
        if(floor == nextFloor)          continue;
        if(abs(floor-nextFloor) > 1)    return;

        if(floor > nextFloor) {
            for(int length=1; length<=inclineLength; length++) {
                int block = road[row][col+length];

                if(block != nextFloor || block == 0)    return;
                installed[row][col+length] = true;
            }
        }

        if(floor < nextFloor) {
            for(int length=0; length<inclineLength; length++) {
                if(installed[row][col-length] || road[row][col-length] == 0)  return;

                installed[row][col-length] = true;
            }
        }
    }

    ways++;
}

void goColumn(int col) {
    for(int row=1; row<width; row++) {
        int floor = road[row][col];
        int nextFloor = road[row+1][col];
        
        if(floor == nextFloor)          continue;
        if(abs(floor-nextFloor) > 1)    return;

        if(floor > nextFloor) {
            for(int length=1; length<=inclineLength; length++) {
                int block = road[row+length][col];

                if(block != nextFloor || block == 0)    return;
                installed[row+length][col] = true;
            }
        }

        if(floor < nextFloor) {
            for(int length=0; length<inclineLength; length++) {
                if(installed[row-length][col] || road[row-length][col] == 0)  return;

                installed[row-length][col] = true;
            }
        }
    }

    ways++;
}