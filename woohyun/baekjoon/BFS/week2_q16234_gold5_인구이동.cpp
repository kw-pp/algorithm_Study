#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <queue>
using namespace std;

int width;
int **area;
bool **visited;

int lowBound;
int highBound;

int neswY[4] = {-1, 0, 1, 0};
int neswX[4] = {0, 1, 0, -1};

bool peopleMoved;
int moveCount;

void move();
void visit(int y, int x);

int main() {
    cin >> width;
    cin >> lowBound;
    cin >> highBound;

    peopleMoved = false;
    moveCount = 0;

    area = new int*[width];
    visited = new bool*[width];

    for(int row=0; row<width; row++) {
        area[row] = new int[width];
        visited[row] = new bool[width];
        
        for(int col=0; col<width; col++) {
            cin >> area[row][col];
            visited[row][col] = false;
        }
    }

    move();

    cout << moveCount << endl;

    return 0;
}

void move() {
    while(1) {
        for (int y=0; y<width; y++) {
            for(int x=0; x<width; x++) {
                if(visited[y][x])   continue;
                visit(y, x);
            }
        }

        if(!peopleMoved)    return;

        for(int y=0; y<width; y++) {
            for(int x=0; x<width; x++) {
                visited[y][x] = false;
            }
        }
        
        peopleMoved = false;
        moveCount++;
    }
}

void visit(int y, int x) {
    queue< pair<int, int> > visitedQueue;
    queue< pair<int, int> > bfsQueue;

    int populationSum = area[y][x];
    int areaSum = 1;
    int average;

    visitedQueue.push(make_pair(y, x));
    bfsQueue.push(make_pair(y, x));

    visited[y][x] = true;

    while (!bfsQueue.empty()) {
        int queueSize = bfsQueue.size();

        for(int count=0; count<queueSize; count++) {
            int currentY = bfsQueue.front().first;
            int currentX = bfsQueue.front().second;
            bfsQueue.pop();

            for(int nesw=0; nesw<4; nesw++) {
                int nearY = currentY + neswY[nesw];
                if(nearY < 0 || nearY >= width) continue;;

                int nearX = currentX + neswX[nesw];
                if(nearX < 0 || nearX >= width) continue;;

                if(visited[nearY][nearX]) continue;

                int populationGap = abs(area[currentY][currentX] - area[nearY][nearX]);

                if(populationGap < lowBound || populationGap > highBound)   continue;
                
                visitedQueue.push(make_pair(nearY, nearX));
                bfsQueue.push(make_pair(nearY, nearX));

                populationSum += area[nearY][nearX];
                areaSum++;

                visited[nearY][nearX] = true;
                peopleMoved = true;
            }
        }
    }

    if(areaSum == 1)    return;

    average = populationSum / areaSum;

    while (!visitedQueue.empty()) {
        pair<int, int> current = visitedQueue.front();
        visitedQueue.pop();

        area[current.first][current.second] = average;
    }
}