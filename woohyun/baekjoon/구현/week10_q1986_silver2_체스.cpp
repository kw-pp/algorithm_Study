#include <iostream>
#include <vector>
using namespace std;

int width, height, safety_sum;

int area[1000][1000];
int queen_move[8][2] = {
    {-1, 0}, {-1, 1}, {0, 1}, {1, 1}, {1, 0}, {1, -1}, {0, -1}, {-1, -1}
};
int knight_move[8][2] = {
    {-2, 1}, {-1, 2}, {1, 2}, {2, 1}, {2, -1}, {1, -2}, {-1, -2}, {-2, -1}
};

vector< pair<int, int> > queens;
vector< pair<int, int> > knights;

bool is_out_of_bound(int y, int x);

int main() {
    cin >> height >> width;
    safety_sum = width * height;

    for(int i=1; i<=3; i++) {
        int count;
        cin >> count;

        for(int j=0; j<count; j++) {
            int y, x;
            cin >> y >> x;
            
            if(i==1) {
                queens.push_back(make_pair(y-1, x-1));
                area[y-1][x-1] = i;
                safety_sum--;

                continue;
            }

            if(i==2) {
                knights.push_back(make_pair(y-1, x-1));
                area[y-1][x-1] = i;
                safety_sum--;

                continue;
            }

            area[y-1][x-1] = i;
            safety_sum--;
        }
    }

    for(int i=0; i<knights.size(); i++) {
        for(int j=0; j<8; j++) {
            int next_knight_y = knights[i].first + knight_move[j][0];
            int next_knight_x = knights[i].second + knight_move[j][1];

            if(is_out_of_bound(next_knight_y, next_knight_x)) continue;

            if(area[next_knight_y][next_knight_x] == 0) {
                area[next_knight_y][next_knight_x] = 4;
                safety_sum--;
            }
        }
    }

    for(int i=0; i<queens.size(); i++) {
        for(int j=0; j<8; j++) {
            int queen_y = queens[i].first;
            int queen_x = queens[i].second;

            int queen_move_y = queen_move[j][0];
            int queen_move_x = queen_move[j][1];

            int distance = 1;

            while (1) {
                int next_queen_y = queen_y + queen_move_y * distance;
                int next_queen_x = queen_x + queen_move_x * distance;

                if(is_out_of_bound(next_queen_y, next_queen_x)) break;

                if(area[next_queen_y][next_queen_x] == 4) {
                    distance++;
                    continue;
                }

                if(area[next_queen_y][next_queen_x] != 0)   break;

                area[next_queen_y][next_queen_x] = 4;
                safety_sum--;
                distance++;
            }
        }
    }

    cout << safety_sum;

    return 0;
}

bool is_out_of_bound(int y, int x) {
    return !(y>=0 && x>=0 && y<height && x<width);
}