#include <iostream>
using namespace std;

int day;
int *periodArray;
int *costArray;
int maxCost;

void dfs(int today, int cost);

int main() {
    cin >> day;

    maxCost = 0;
    periodArray = new int[day];
    costArray = new int[day];

    for(int index = 0; index < day; index++) {
        cin >> periodArray[index];
        cin >> costArray[index];
    }

    dfs(0, 0);

    cout << maxCost << endl;

    return 0;
}

void dfs(int today, int cost) {
    if(today >= day) {
        maxCost = maxCost < cost ? cost : maxCost;
        return;
    }

    int nextPossibleDay = today + periodArray[today];
    int todayCost = cost + costArray[today];

    if(nextPossibleDay <= day)  dfs(nextPossibleDay, todayCost);
    dfs(today+1, cost);
}

// 1차 오답

// 오답 사유: 상담을 수락하고 마무리가 되는(n - m)번째 날, 그 날 시작하는 상담요청이 (m + a)일짜리라면
//          재귀 종료가 아닌 상담을 거절하고 다음날로 넘어가야 하는데, 그대로 종료 해버림

// 반례)     ...      5      6      7       의 경우, 5일차에 상담이 끝났다면 선택을 해야하는데,
//          ...      4      1      1       5일차를 스킵하고 6, 7일차의 상담을 수락해야 정답인데
//          ...      10     5      5       5일차에서 종료를 했기 때문에 오답이 발생했다

// 오답 코드
// void dfs(int today, int cost) {
//     if(today >= day) {
//         maxCost = maxCost < cost ? cost : maxCost;
//         return;
//     }

//     int nextPossibleDay = today + periodArray[today];
//     int todayCost = cost + costArray[today];

//     if(nextPossibleDay > day) {
//         maxCost = maxCost < cost ? cost : maxCost;
//         return;
//     }

//     dfs(nextPossibleDay, todayCost);
//     dfs(today+1, cost);
// }