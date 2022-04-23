#include <iostream>
using namespace std;

int bridgeCount(int leftSite, int rightSite);
int factorial(int number);

int main() {
    int testCaseCount;
    cin >> testCaseCount;

    int leftSiteNumber[testCaseCount];
    int rightSiteNumber[testCaseCount];

    for(int test = 0; test < testCaseCount; test++) {
        cin >> leftSiteNumber[test];
        cin >> rightSiteNumber[test];
    }

    
    for(int test = 0; test < testCaseCount; test++) {
        cout << bridgeCount(leftSiteNumber[test], rightSiteNumber[test]) << endl;
    }
    
    return 0;
}

int bridgeCount(int left, int right) {
    int gap = right - left;

    if(gap == 0)    return 1;

    return right * bridgeCount(left, right - 1) / gap;
}

// 오답 (설명: 재귀 함수 / 사유: 시간 초과)

// int bridgeCount(int leftSite, int rightSite) {
//     int bridgeSum = 0;
    
//     if(leftSite == rightSite)   return 1;
//     if(leftSite == 2)    return rightSite - 1;
    
//     for(int gap = 1; gap <= rightSite - leftSite; gap++) {
//         bridgeSum += bridgeCount(leftSite - 1, leftSite - 1 + gap);
//     }
    
//     return bridgeSum + 1;
// }