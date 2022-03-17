#include <iostream>
#include <queue>
#include <algorithm>
using namespace std;

queue<int> virusIndexQueue;

int* labArea;
int* safeArea;
int labWidth, labHeight;
int safeAreaInitialCount = 0;

int finalMaxSafeAreaCount();
int eachMaxSafeAreaCount(int *newLabArea, queue<int> virusQueueCopy);

int main() {
    cin >> labHeight >> labWidth;

    labArea = new int[labHeight * labWidth];
    safeArea = new int[labHeight * labWidth];

    for(int index = 0; index < labHeight * labWidth; index++) {
        cin >> labArea[index];

        if(labArea[index] == 2) virusIndexQueue.push(index);
        if(labArea[index] == 0) safeArea[safeAreaInitialCount++] = index;
    }

    cout << finalMaxSafeAreaCount() << endl;

    return 0;
}

int finalMaxSafeAreaCount() {
    int max = 0;

    for(int first = 0; first < safeAreaInitialCount - 2; first++) {
        for(int second = first + 1; second < safeAreaInitialCount - 1; second++) {
            for(int third = second + 1; third < safeAreaInitialCount; third++) {
                int newLabArea[labWidth * labHeight];

                copy(labArea, labArea + labWidth*labHeight, newLabArea);
                newLabArea[safeArea[first]] = 1;
                newLabArea[safeArea[second]] = 1;
                newLabArea[safeArea[third]] = 1;

                int currentMax = eachMaxSafeAreaCount(newLabArea, virusIndexQueue);
                max = max < currentMax ? currentMax : max; 
            }
        }
    }

    return max;
}

int eachMaxSafeAreaCount(int *newLabArea, queue<int> virusQueueCopy) {
    int maxSafeArea = safeAreaInitialCount - 3;             // 초기 안전구역 수 복사
    int contagionCount = -1;                            // 신규 감염 수 (while문 진입을 위해 -1로 초기화)

    // 경계 조건
    // 상 - index - width < 0 
    // 하 - index + width >= width*height
    // 좌 - index % width == 0
    // 우 - index % width == width - 1

    // 감염 조건
    // 상 - index - width == 0
    // 하 - index - width == 0
    // 좌 - index - 1 == 0
    // 우 - index + 1 == 0
    
    while(contagionCount != 0) {
        int virusCount = virusQueueCopy.size();
        contagionCount = 0;

        for(int i = 0; i < virusCount; i++) {
            int current = virusQueueCopy.front();   // 현재 방
            virusQueueCopy.pop();
            virusQueueCopy.push(current);

            if(current - labWidth >= 0) {
                if(newLabArea[current - labWidth] == 0) {
                    newLabArea[current - labWidth] = 2;
                    virusQueueCopy.push(current - labWidth);
                    
                    contagionCount++;
                }
            }

            if(current + labWidth < labWidth * labHeight) {
                if(newLabArea[current + labWidth] == 0) {
                    newLabArea[current + labWidth] = 2;
                    virusQueueCopy.push(current + labWidth);

                    contagionCount++;
                }
            }

            if(current % labWidth != 0) {
                if(newLabArea[current - 1] == 0) {
                    newLabArea[current - 1] = 2;
                    virusQueueCopy.push(current - 1);

                    contagionCount++;
                }
            }

            if(current % labWidth != labWidth - 1) {
                if(newLabArea[current + 1] == 0) {
                    newLabArea[current + 1] = 2;
                    virusQueueCopy.push(current + 1);

                    contagionCount++;
                }
            }
        }

        maxSafeArea -= contagionCount;
    }

    return maxSafeArea;
}