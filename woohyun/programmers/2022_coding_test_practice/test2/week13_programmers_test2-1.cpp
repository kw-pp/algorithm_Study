#include <string>
#include <algorithm>
#include <vector>

using namespace std;

int solution(vector<int> number) {
    int answer = 0;

    for(int a=0; a<number.size()-2; a++) {
        for(int b=a+1; b<number.size()-1; b++) {
            for(int c=b+1; c<number.size(); c++) {
                if(number[a] + number[b] + number[c] == 0)  answer++;
            }
        }
    }

    return answer;
}