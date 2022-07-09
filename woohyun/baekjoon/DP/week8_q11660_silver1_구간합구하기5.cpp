#include <iostream>
#include <algorithm>
using namespace std;

int number_pad[1025][1025];

int main() {
    ios::sync_with_stdio(0);
	cin.tie(0);

    int pad_size;
    int test_case_count;
    int input;

    cin >> pad_size >> test_case_count;

    for(int i=1; i<=pad_size; i++) {
        for(int j=1; j<=pad_size; j++) {
            cin >> input;
            number_pad[i][j] = input + number_pad[i-1][j] + number_pad[i][j-1] - number_pad[i-1][j-1];
        }
    }

    for(int i=0; i<test_case_count; i++) {
        int x1, y1, x2, y2;
        cin >> x1 >> y1 >> x2 >> y2;

        cout << number_pad[x2][y2] + number_pad[x1-1][y1-1] - number_pad[x1-1][y2] - number_pad[x2][y1-1] << endl;
    }

    return 0;
}
