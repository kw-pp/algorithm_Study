#include <iostream>
#include <algorithm>
#include <queue>
using namespace std;

queue< pair<int, int> > redQueue;
queue< pair<int, int> > blueQueue;

int width, height;
char **maze;
int minRotate;
int swneX[4] = {0, -1, 0, 1}; // 남쪽이 0
int swneY[4] = {1, 0, -1, 0};

void bfs();

int main() {
    cin >> height >> width;

    maze = new char *[height];
    minRotate = -1;

    pair<int, int> blueYX;
    pair<int, int> redYX;

    for (int i = 0; i < height; i++) {
        maze[i] = new char[width];

        for (int j = 0; j < width; j++) {
            char input;
            cin >> input;

            if (input == 'R') {
                redYX = make_pair(i, j);
                maze[i][j] = '.';
            }

            if (input == 'B') {
                blueYX = make_pair(i, j);
                maze[i][j] = '.';
            }

            maze[i][j] = input;
        }
    }

    redQueue.push(redYX);
    blueQueue.push(blueYX);

    bfs();

    cout << minRotate << endl;

    return 0;
}

void bfs() {
    int rotateCount = 0;

    while (1) {
        if(redQueue.empty())    return;

        rotateCount++;
        if(rotateCount > 10)    return;

        int queueSize = redQueue.size();

        for (int i = 0; i < queueSize; i++) {
            pair<int, int> red = redQueue.front();
            pair<int, int> blue = blueQueue.front();

            redQueue.pop();
            blueQueue.pop();

            for(int swne = 0; swne < 4; swne++) {
                int redY = red.first;
                int redX = red.second;
                int blueY = blue.first;
                int blueX = blue.second;

                bool isRedOut = false;
                bool isBlueOut = false;

                bool beadsOnLine = (swne%2 == 0 && redX == blueX) || (swne%2 == 1 && redY == blueY);

                if (beadsOnLine) {
                    bool isRedFirst = ((redY + redX) - (blueY + blueX)) * (swneY[swne] + swneX[swne]) > 0;
                    
                    if (isRedFirst) { // 빨강이 아래에 위치
                        while (1) { // 빨강
                            if (maze[redY + swneY[swne]][redX + swneX[swne]] == 'O') {
                                isRedOut = true;
                                break;
                            }
                            if (maze[redY + swneY[swne]][redX + swneX[swne]] == '#')    break;

                            redY += swneY[swne];
                            redX += swneX[swne];
                        }

                        while (1) { // 파랑
                            if (maze[blueY + swneY[swne]][blueX + swneX[swne]] == 'O') {
                                isBlueOut = true;
                                break;
                            }
                            if (maze[blueY + swneY[swne]][blueX + swneX[swne]] == '#')  break;
                            if (redY == blueY + swneY[swne] && redX == blueX + swneX[swne]) {
                                if(isRedOut)    isBlueOut = true;
                                break;
                            }

                            blueY += swneY[swne];
                            blueX += swneX[swne];
                        }
                    }
                    else {
                        while (1) { // 파랑
                            if (maze[blueY + swneY[swne]][blueX + swneX[swne]] == 'O') {
                                isBlueOut = true;
                                break;
                            }
                            if (maze[blueY + swneY[swne]][blueX + swneX[swne]] == '#')  break;

                            blueY += swneY[swne];
                            blueX += swneX[swne];
                        }

                        while (1) { // 빨강
                            if (maze[redY + swneY[swne]][redX + swneX[swne]] == 'O') {
                                isRedOut = true;
                                break;
                            }
                            if (maze[redY + swneY[swne]][redX + swneX[swne]] == '#')    break;
                            if (blueY == redY + swneY[swne] && blueX == redX + swneX[swne]) break;


                            redY += swneY[swne];
                            redX += swneX[swne];
                        }
                    }
                }
                else {
                    while (1) { // 빨강
                        if (maze[redY + swneY[swne]][redX + swneX[swne]] == 'O') {
                            minRotate = rotateCount;
                            return;
                        }
                        if (maze[redY + swneY[swne]][redX + swneX[swne]] == '#')    break;

                        redY += swneY[swne];
                        redX += swneX[swne];
                    }

                    while (1) { // 파랑
                        if (maze[blueY + swneY[swne]][blueX + swneX[swne]] == 'O') {
                            isBlueOut = true;
                            break;
                        }
                        if (maze[blueY + swneY[swne]][blueX + swneX[swne]] == '#')  break;
                    

                        blueY += swneY[swne];
                        blueX += swneX[swne];
                    }
                }

                if(isBlueOut)   continue;
                if(isRedOut) {
                    minRotate = rotateCount;
                    return;
                }

                redQueue.push(make_pair(redY, redX));
                blueQueue.push(make_pair(blueY, blueX));
            }
        }
    }
}