#include <iostream>
#include <vector>
using namespace std;

int truckCount, bridgeLength, maxLoad;
vector<int> trucks;

// 트럭들 사이에 0을 넣어 어느 구간에서도 bridgeLength의 길이만큼의 합이 maxLoad보다 안 넘도록 함
void setTrucks();

int main() {
    cin >> truckCount >> bridgeLength >> maxLoad;

    setTrucks();

    cout << trucks.size() << endl;

    return 0;
}

void setTrucks() {
    // 초기 다리 하중
    int currentWeight = 0;

    // 어차피 마지막 트럭도 다리를 건너야 하므로 trucks의 길이와 bridgeLength가 더해져 결과값이 도출된다
    // 따라서 trucks 앞에다가 뒤에 들어갈 bridgeLength만큼 0을 넣어 index out of bound 방지
    for(int i=0; i<bridgeLength; i++)   trucks.push_back(0);

    for(int i=0; i< truckCount; i++) {
        int input;
        cin >> input;

        while (1) {
            currentWeight -= trucks[trucks.size() - bridgeLength];
            if(currentWeight + input <= maxLoad)    break;

            trucks.push_back(0);
        }

        currentWeight += input;
        trucks.push_back(input);
    }
}