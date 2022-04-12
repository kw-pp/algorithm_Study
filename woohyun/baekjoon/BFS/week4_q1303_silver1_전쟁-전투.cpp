#include <iostream>
#include <queue>
using namespace std;

int width, height;
char ground[100][100] =  { ' ', };
int soldier[2] = {0, 0};

bool visited[100][100] = { false, };
int neswY[4] = {-1, 0, 1, 0};
int neswX[4] = {0, 1, 0, -1};

void bfs(int y, int x, char whiteOrBlue);

int main() {
    cin >> width >> height;

    for(int i=0; i<height; i++) {
        for(int j=0; j<width; j++)  cin >> ground[i][j];
    }

    for(int i=0; i<height; i++) {
        for(int j=0; j<width; j++) {
            if(visited[i][j])   continue;

            visited[i][j] = true;
            bfs(i, j, ground[i][j]);
        }
    }

    cout << soldier[0] << " " << soldier[1] << endl;

    return 0;
}

void bfs(int y, int x, char whiteOrBlue) {
    queue< pair<int, int> > positions;
    int allyCount = 0;

    positions.push(make_pair(y, x));

    while (!positions.empty()) {
        int positionCount = positions.size();
        allyCount += positionCount;

        for(int i=0; i<positionCount; i++) {
            pair<int, int> current = positions.front();
            positions.pop();

            for(int nesw=0; nesw<4; nesw++) {
                int nextY = current.first + neswY[nesw];
                int nextX = current.second + neswX[nesw];

                if(nextY < 0 || nextY >= height || nextX < 0 || nextX >= width) continue;
                if(ground[nextY][nextX] != whiteOrBlue || visited[nextY][nextX])  continue;

                positions.push(make_pair(nextY, nextX));
                visited[nextY][nextX] = true;
            }
        }
    }

    if(whiteOrBlue == 'W')    soldier[0] += allyCount * allyCount;
    if(whiteOrBlue == 'B')    soldier[1] += allyCount * allyCount;
}