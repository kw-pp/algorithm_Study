#include <iostream>
using namespace std;

int width, height;
int x, y, starringAt;
int area[50][50] = {0,};
int neswX[4] = {0, 1, 0, -1};
int neswY[4] = {-1, 0, 1, 0};

bool isOutOfBound(int x, int y);
int cleanAreaCount();

int main() {
    cin >> height >> width;
    cin >> y >> x >> starringAt;

    for(int i = 0; i < height; i++) {
        for(int j = 0; j < width; j++)  {
            cin >> area[i][j];
        }
    }

    cout << cleanAreaCount() << endl;

    return 0;
}

int cleanAreaCount() {
    int cleaned = 0;

    while (1) {
        if(area[y][x] == 0) {
            area[y][x] = 2;
            cleaned++;
        }

        for(int rotate = 1; rotate <= 4; rotate++) {
            starringAt = (starringAt + 3) % 4;

            int nextX = x + neswX[starringAt];
            int nextY = y + neswY[starringAt];

            if(isOutOfBound(nextX, nextY) || area[nextY][nextX] != 0) {
                if(rotate == 4) {
                    int backX = x - neswX[starringAt];
                    int backY = y - neswY[starringAt];

                    if(isOutOfBound(backX, backY) || area[backY][backX] == 1) {
                        return cleaned;
                    }

                    x = backX;
                    y = backY;
                    break;
                }

                continue;
            }

            x = nextX;
            y = nextY;
            break;
        }
    }
}

bool isOutOfBound(int x, int y) {
    return !(x >= 0 && y >= 0 && x < width && y < height);
}