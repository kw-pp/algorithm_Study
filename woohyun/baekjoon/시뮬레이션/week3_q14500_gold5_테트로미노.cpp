#include <iostream>
#include <algorithm>
using namespace std;

int height, width;
int paper[500][500];
int maxSum;

void searchRow(int row);
void searchColumn(int col);

// 모든 경우를 최대한 효율적으로 탐색하기 위해 최대한 겹쳐서 탐색하는 경우를 배제해야 함
// 모양대로 가로, 세로 한 번씩 탐색

int main() {
    cin >> height >> width;
    maxSum = 0;

    for(int i=0; i<height; i++) {
        for(int j=0; j<width; j++)  cin >> paper[i][j];
    }

    for(int row=0; row<height; row++) searchRow(row);       // 행마다 시행
    for(int col=0; col<width; col++) searchColumn(col);       // 행마다 시행

    cout << maxSum << endl;

    return 0;
}

void searchRow(int row) {
    int sum = paper[row][0] + paper[row][1] + paper[row][2];

    for(int i=3; i<width; i++) {
        sum += paper[row][i];
        maxSum = max(maxSum, sum);
        sum -= paper[row][i-3];
    }

    if(row == height-1) return;

    for(int col=0; col<width; col++) {
        sum = 0;
            
        for(int block=0; block<3; block++) {
            int underBlock = 2 - block;
            sum += paper[row][col+block];

            for(int underCol = col-underBlock; underCol <= col+block; underCol++) {
                if(underCol < 0 || underCol >= width)    continue;

                int underSum = 0;

                for(int ub = 0; ub <= underBlock; ub++) {
                    underSum += paper[row+1][underCol+ub];
                }

                maxSum = max(maxSum, sum+underSum);
            }
        }
    }
}

void searchColumn(int col) {
    int sum = paper[0][col] + paper[1][col] + paper[2][col];

    for(int i=3; i<height; i++) {
        sum += paper[i][col];
        maxSum = max(maxSum, sum);
        sum -= paper[i-3][col];
    }

    if(col == width-1) return;

    for(int row=0; row<height; row++) {
        sum = 0;
            
        for(int block=0; block<3; block++) {
            int rightBlock = 2 - block;
            sum += paper[row+block][col];

            for(int rightRow = row-rightBlock; rightRow <= row+block; rightRow++) {
                if(rightRow < 0 || rightRow >= height)    continue;

                int rightSum = 0;

                for(int rb = 0; rb <= rightBlock; rb++) {
                    rightSum += paper[rightRow+rb][col+1];
                }

                maxSum = max(maxSum, sum+rightSum);
            }
        }
    }
}

