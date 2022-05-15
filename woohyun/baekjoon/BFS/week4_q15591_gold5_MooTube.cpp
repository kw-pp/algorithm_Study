#include <iostream>
#include <vector>
using namespace std;

int videos;
int questionCount;

vector< pair<int, int> > usadoArray[5001];
int answers[5000] = { 0, };

void recommend(int index, int k, int video, int previous);

// 경로 찾기 -> dfs
int main() {
    cin >> videos >> questionCount;

    for(int i=0; i<videos-1; i++) {
        int p, q, usado;
        cin >> p >> q >> usado;

        usadoArray[p].push_back(make_pair(q, usado));
        usadoArray[q].push_back(make_pair(p, usado));
    }

    for(int i=0; i<questionCount; i++) {
        int k, video;
        cin >> k >> video;

        recommend(i, k, video, -1);
    }

    for(int i=0; i<questionCount; i++) cout << answers[i] << endl;

    return 0;
}

void recommend(int index, int k, int video, int previous) {
    for(int i=0; i<usadoArray[video].size(); i++) {
        if(usadoArray[video][i].first == previous)  continue;
        if(usadoArray[video][i].second < k)         continue;

        answers[index]++;
        recommend(index, k, usadoArray[video][i].first, video);
    }
}