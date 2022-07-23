#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;

int test_case_count;
vector<string> answers;

bool can_go(int from_x, int from_y, int to_x, int to_y);
void test();

int main() {
    cin >> test_case_count;

    for(int i=0; i<test_case_count; i++)    test();
    for(int i=0; i<answers.size(); i++)     cout << answers[i] << endl;

    return 0;
}

void test() {
    int convenience_count;
    int x, y;

    // x, y 순
    vector< pair<int, int> > positions;
    vector<int> paths[102];

    vector<int> visited;
    queue<int> visiting;

    cin >> convenience_count;

    for(int j=0; j<convenience_count+2; j++) {
        cin >> x >> y;

        for(int k=0; k<positions.size(); k++) {
            if(can_go(x, y, positions[k].first, positions[k].second)) {
                paths[k].push_back(positions.size());
                paths[positions.size()].push_back(k);
            }
        }

        positions.push_back(make_pair(x, y));
    }

    visited.push_back(0);
    visiting.push(0);

    while (visiting.size() > 0) {
        int visiting_count = visiting.size();

        for(int i=0; i<visiting_count; i++) {
            int current = visiting.front();
            visiting.pop();

            for(int i=0; i<paths[current].size(); i++) {
                if(find(visited.begin(), visited.end(), paths[current][i]) != visited.end())    continue;

                if(paths[current][i] == convenience_count+1) {
                    answers.push_back("happy");
                    return;
                }

                visited.push_back(paths[current][i]);
                visiting.push(paths[current][i]);
            }   
        }
    }

    answers.push_back("sad");
}

bool can_go(int from_x, int from_y, int to_x, int to_y) {
    return (abs(from_x-to_x) + abs(from_y-to_y)) <= 1000;
}