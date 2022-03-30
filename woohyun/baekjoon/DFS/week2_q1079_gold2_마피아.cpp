#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int player;
int **relation;
int eunjin;
int maxNight;

void dfs(vector<int> playerList, vector<int> guiltyList, int nightCount);
bool isGameOver(vector<int> playerList);

// 1차 구상: 매 밤 최상의 조건을 판별하여 진행 -> 그 조건이 최상의 조건인지 알 수 있는 방법이 없음 ( ex) 바둑, 오목 )
// 2차: DFS -> 모든 경우의 수를 탐색하여 최대의 nightCount 출력
int main() {
    vector<int> playerList;
    vector<int> guiltyList;

    cin >> player;         

    relation = new int*[player];
    maxNight = 0;

    for(int i=0; i<player; i++) {
        int guilty;
        cin >> guilty;

        playerList.push_back(i);                                // 참가자 벡터에 넣기
        guiltyList.push_back(guilty);                           // 유죄 지수 벡터에 넣기
    }

    for(int i=0; i<player; i++) {
        relation[i] = new int[player];

        for(int j=0; j<player; j++) cin >> relation[i][j];      // 관계 배열 입력
    }

    cin >> eunjin;

    dfs(playerList, guiltyList, 0);

    cout << maxNight << endl;

    return 0;
}

void dfs(vector<int> playerList, vector<int> guiltyList, int nightCount) {
    if(isGameOver(playerList)) {
        maxNight = maxNight < nightCount ? nightCount : maxNight;
        return;
    }

    if(playerList.size() % 2 == 0) {
        for(int i=0; i<playerList.size(); i++) {
            if(playerList[i] == eunjin) continue;

            int playerIIndex = playerList[i];

            vector<int> copiedPlayerList = playerList;
            vector<int> copiedGuiltyList = guiltyList;
        
            for(int j=0; j<copiedPlayerList.size(); j++) {
                if(i == j)  continue;

                int playerJIndex = copiedPlayerList[j];
                copiedGuiltyList[j] += relation[playerIIndex][playerJIndex];
            }

            copiedPlayerList.erase(copiedPlayerList.begin() + i);
            copiedGuiltyList.erase(copiedGuiltyList.begin() + i);

            dfs(copiedPlayerList, copiedGuiltyList, nightCount+1);
        }
    }
    else {
        int executedIndex = 0;          // 제거할 플레이어의 인덱스
        int maxGuilty = 0;              // max guilty index

        for(int i=0; i<guiltyList.size(); i++) {
            if(maxGuilty < guiltyList[i]) {      // <= 연산자가 아닌 < 연산자를 사용하여 maxGuilty 값이 
                maxGuilty = guiltyList[i];       // 여러명일 경우 맨 처음 사람이 지목되게 한다
                executedIndex = i;
            }
        }

        playerList.erase(playerList.begin() + executedIndex);   // execute max guilty player
        guiltyList.erase(guiltyList.begin() + executedIndex);

        dfs(playerList, guiltyList, nightCount);
    }

}

bool isGameOver(vector<int> playerList) {
    bool lose = find(playerList.begin(), playerList.end(), eunjin) == playerList.end();
    bool win = playerList.size() == 1;      // lose 인지 먼저 판별하고 win 인지 판별하므로
                                            // 은진이가 처형당하지 않았는데 playerList의 길이가 1이라는 것은
                                            // 은진(마피아 팀) 외에는 아무도 남지 않았다는 뜻이므로
                                            // 승리조건으로 충분하다
    

    return lose || win;
}