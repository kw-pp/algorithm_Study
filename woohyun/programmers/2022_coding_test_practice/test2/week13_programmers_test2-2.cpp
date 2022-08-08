#include <string>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

int solution(vector<int> topping) {
    int answer = 0;

    map<int, int> forward;
    map<int, int> backward;

    vector<int> forward_count;
    vector<int> backward_count;

    for(int i=0; i<topping.size()-1; i++) {
        forward[topping[i]]++;
        backward[topping[topping.size() - i - 1]]++;

        forward_count.push_back(forward.size());
        backward_count.push_back(backward.size());
    }

    for(int i=0; i<forward_count.size(); i++) {
        if(forward_count[i] == backward_count[forward_count.size() - i - 1])    answer++;
    }

    return answer;
}