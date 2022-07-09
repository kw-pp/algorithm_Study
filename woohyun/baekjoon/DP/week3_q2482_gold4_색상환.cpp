#include <iostream>
using namespace std;

int colorCount;
int selectCount;

int linear[1001][1001];

int main() {
    cin >> colorCount >> selectCount;

    for(int i=0; i<=colorCount; i++) {
        for(int j=0; j<=selectCount; j++) {
            if(j==0) {
                linear[i][j] = 1;
                continue;
            }

            if(j==1) {
                linear[i][j] = i;
                continue;
            }

            if(i < 2*j-1) continue;

            linear[i][j] = (linear[i-1][j] + linear[i-2][j-1]) % 1000000003;
        }
    }

    cout << (linear[colorCount-3][selectCount-1] + linear[colorCount-1][selectCount]) % 1000000003 << endl;

    return 0;
}