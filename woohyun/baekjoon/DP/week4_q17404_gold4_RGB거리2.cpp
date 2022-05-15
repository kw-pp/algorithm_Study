#include <iostream>
#include <algorithm>
using namespace std;

int houseCount;
int red[1000][3];       // 시작이 빨강 & rgb 순
int green[1000][3];     // 시작이 초록
int blue[1000][3];      // 시작이 파랑
int cheapest;

void dp();
int min(int a, int b, int c);

int main() {
    cin >> houseCount;
    
    for(int i=0; i<houseCount; i++) {
        int cost;

        for(int color=0; color<3; color++) {
            cin >> cost;

            red[i][color] = cost;       // 빨강
            green[i][color] = cost;     // 초록
            blue[i][color] = cost;      // 파랑
        }
    }

    dp();

    cout << cheapest << endl;

    return 0;
}

void dp() {
    red[0][1] = 1000000;
    red[0][2] = 1000000;
    red[houseCount-1][0] = 1000000;
    green[0][0] = 1000000;
    green[0][2] = 1000000;
    green[houseCount-1][1] = 1000000;
    blue[0][0] = 1000000;
    blue[0][1] = 1000000;
    blue[houseCount-1][2] = 1000000;

    for(int house=1; house < houseCount; house++) {
        for(int i=0; i<3; i++) {
            red[house][i] += min(red[house-1][(i+1)%3], red[house-1][(i+2)%3]);
            green[house][i] += min(green[house-1][(i+1)%3], green[house-1][(i+2)%3]);
            blue[house][i] += min(blue[house-1][(i+1)%3], blue[house-1][(i+2)%3]);
        }
    }

    int redFirst = min(red[houseCount-1][0], red[houseCount-1][1], red[houseCount-1][2]);
    int greenFirst = min(green[houseCount-1][0], green[houseCount-1][1], green[houseCount-1][2]);
    int blueFirst = min(blue[houseCount-1][0], blue[houseCount-1][1], blue[houseCount-1][2]);

    cheapest = min(redFirst, blueFirst, greenFirst);
}

int min(int a, int b, int c) {
    return min(a, min(b, c));
}