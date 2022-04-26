#include <iostream>
#include <vector>
using namespace std;

int assignmentCount;
int period[10001];
int maxPeriod = 0;

int main() {
    cin >> assignmentCount;

    for(int i=1; i<=assignmentCount; i++) {
        int time, previousCount, work;
        int previousTime = 0;

        cin >> time >> previousCount;

        for(int p=0; p<previousCount; p++) {
            cin >> work;
            previousTime = max(previousTime, period[work]);
        }

        period[i] = previousTime + time;
        maxPeriod = max(maxPeriod, period[i]);
    }

    cout << maxPeriod << endl;

    return 0;
}