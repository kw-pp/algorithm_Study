#include <string>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

bool can_buy_all(vector<string> want, map<string, int> jung_hyeon, map<string, int> copied);

int solution(vector<string> want, vector<int> number, vector<string> discount) {
    map<string, int> jung_hyeon_want, jung_hyeon_copy;
    int answer = 0;

    for(int i; i<want.size(); i++) {
        jung_hyeon_want[want[i]] = number[i];
        jung_hyeon_copy[want[i]] = 0;
    }

    for(int i=0; i<10; i++) jung_hyeon_copy[discount[i]]++;
    if(can_buy_all(want, jung_hyeon_want, jung_hyeon_copy)) answer++;

    for(int i=1; i<discount.size()-9; i++) {
        jung_hyeon_copy[discount[i-1]]--;
        jung_hyeon_copy[discount[i+9]]++;

        if(can_buy_all(want, jung_hyeon_want, jung_hyeon_copy)) answer++;
    }

    return answer;
}

bool can_buy_all(vector<string> want, map<string, int> jung_hyeon, map<string, int> copied) {
    for(int i=0; i<want.size(); i++) {
        if(jung_hyeon[want[i]] > copied[want[i]])   return false;
    }

    return true;
}