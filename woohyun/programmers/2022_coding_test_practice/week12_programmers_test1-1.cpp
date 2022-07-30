#include <string>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

string solution(string x, string y) {
    string answer = "";
    bool is_zero = true;
    bool has_jjak_goong = false;

    map<char, int> x_map;
    x_map['0'] = 0;
    x_map['1'] = 0;
    x_map['2'] = 0;
    x_map['3'] = 0;
    x_map['4'] = 0;
    x_map['5'] = 0;
    x_map['6'] = 0;
    x_map['7'] = 0;
    x_map['8'] = 0;
    x_map['9'] = 0;

    map<char, int> y_map;
    y_map['0'] = 0;
    y_map['1'] = 0;
    y_map['2'] = 0;
    y_map['3'] = 0;
    y_map['4'] = 0;
    y_map['5'] = 0;
    y_map['6'] = 0;
    y_map['7'] = 0;
    y_map['8'] = 0;
    y_map['9'] = 0;

    for(int i=0; i<x.size(); i++)   x_map[x[i]]++;
    for(int i=0; i<y.size(); i++)   y_map[y[i]]++;

    for(int i=9; i>=0; i--) {
        char number_to_char = i+48;
        int common_count = min(x_map[number_to_char], y_map[number_to_char]);

        if(common_count > 0) {
            if(i==0)    has_jjak_goong = true;
            else {
                has_jjak_goong = true;
                is_zero = false;
            }
        }

        for(int j=0; j<common_count; j++)  answer.push_back(number_to_char);
    }

    if(!has_jjak_goong)   return "-1";
    if(is_zero)     return "0";

    return answer;
}