#include <iostream>
#include <queue>
#include <algorithm>
using namespace std;

int height, width;
char floor[50][50];
int tileCount;

void countTile();

int main() {
    cin >> height >> width;
    tileCount = 0;

    for(int i=0; i<height; i++) {
        string input;
        cin >> input;

        for(int j=0; j<width; j++) floor[i][j] = input[j];
    }

    countTile();

    cout << tileCount << endl;

    return 0;
}

void countTile() {
    for(int i=0; i<height; i++) {
        for(int j=0; j<width; j++) {
            if(floor[i][j] == '-') {
                if(j == 0 || floor[i][j - 1] != '-') {
                    tileCount++;
                    continue;
                }
            }

            if(floor[i][j] == '|') {
                if(i == 0 || floor[i - 1][j] != '|') {
                    tileCount++;
                    continue;
                }
            }
        }
    }
}