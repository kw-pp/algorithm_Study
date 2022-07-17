#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int area[5][5];
int sum = 0;

bool visited[10][10][10][10][10][10] = { false, };
int neswY[4] = {-1, 0, 1, 0};
int neswX[4] = {0, 1, 0, -1};

void visit(int y, int x, vector<int> path);
bool is_out_of_bound(int y, int x);
void print();

int main() {
    for(int i=0; i<5; i++) {
        for(int j=0; j<5; j++)  cin >> area[i][j];
    }

    for(int i=0; i<5; i++) {
        vector<int> path;
        for(int j=0; j<5; j++)  visit(i, j, path);
    }

    cout << sum;

    return 0;
}

void visit(int y, int x, vector<int> path) {
    if(path.size() == 6) {
        // if(path[0] == 1 && path[1] == 2 && path[2] == 1 && path[3] == 2 && path[4] == 1 && path[5] == 2) {
        //     cout << path[0] << path[1] << path[2] << path[3] << path[4] << path[5] << endl;
        // }

        if(!visited[path[0]][path[1]][path[2]][path[3]][path[4]][path[5]]) {
            visited[path[0]][path[1]][path[2]][path[3]][path[4]][path[5]] = true;
            sum++;

            // cout << path[0] << path[1] << path[2] << path[3] << path[4] << path[5] << endl;
        }

        return;
    }

    for(int i=0; i<4; i++) {
        int nextY = y+neswY[i];
        int nextX = x+neswX[i];

        if(is_out_of_bound(nextY, nextX))   continue;

        // vector<int> new_path;
        // copy(path.begin(), path.end(), new_path.begin());
        // new_path.push_back(area[y][x]);

        path.push_back(area[y][x]);
        visit(nextY, nextX, path);
        path.pop_back();
    }
}

bool is_out_of_bound(int y, int x) {
    return !(y>=0 && y<5 && x>=0 && x<5);
}