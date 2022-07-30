#include <string>
#include <vector>
#include <stack>

using namespace std;

int solution(vector<int> order) {
    stack<int> sub_belt;
    sub_belt.push(-1);

    int parcel_index = 0;
    int parcel_number = 1;
    int answer = 0;

    while(1) {
        int current = order[parcel_index];

        if(current == sub_belt.top()) {
            sub_belt.pop();
            parcel_index++;
            answer++;

            continue;
        }

        if(parcel_number == order.size()+1)   break;

        if(current == parcel_number) {
            parcel_number++;
            parcel_index++;
            answer++;

            continue;
        }

        sub_belt.push(parcel_number++);
    }

    return answer;
}