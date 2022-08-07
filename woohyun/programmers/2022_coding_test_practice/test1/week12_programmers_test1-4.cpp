#include <string>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

int solution(vector<vector<int>> beginning, vector<vector<int>> target) {
    vector< vector<int> > flipped;
    map< string, vector<int> > row_serial;
    map< string, vector<int> > column_serial;

    int answer = 0;

    for(int i=0; i<beginning.size(); i++) {
        vector<int> row;

        for(int j=0; j<beginning[i].size(); j++)    row.push_back((beginning[i][j] + target[i][j])%2);
        flipped.push_back(row);
    }

    for(int i=0; i<flipped.size(); i++) {
        string serial_number = "";
        for(int j=0; j<flipped[0].size(); j++)  serial_number += flipped[i][j];

        row_serial[serial_number].push_back(i);
    }

    for(int i=0; i<flipped[0].size(); i++) {
        string serial_number = "";
        for(int j=0; j<flipped.size(); j++)  serial_number += flipped[i][j];

        column_serial[serial_number].push_back(i);
    }

    if(row_serial.size() > 2 && column_serial.size() > 2)   return -1;

    int x = row_serial.begin()->second[0];
    int y = column_serial.begin()->second[0];

    if(flipped[x][y] == 0) {
        int total = row_serial.begin()->second.size() + column_serial.begin()->second.size();
        int opposite = flipped.size() + flipped[0].size() - total;

        answer = min(total, opposite);
    }

    if(flipped[x][y] == 1) {
        int total = flipped.size() - row_serial.begin()->second.size() + column_serial.begin()->second.size();
        int opposite = flipped.size() + flipped[0].size() - total;

        answer = min(total, opposite);
    }

    return answer;
}