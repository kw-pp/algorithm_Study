#include <iostream>
#include <vector>
using namespace std;

int height, width;
int y, x;
int commandCount;

int field[22][22];
vector<int> answer;

int dice[6] = { 0, };
int diceTop = 0;
int diceFront = 1;
int diceRight = 2;

int ewnsY[4] = {0, 0, -1, 1};
int ewnsX[4] = {1, -1, 0 ,0};

void getTop(int command);
void moveDice(int command);

int main() {
    cin >> height >> width >> y >> x >> commandCount;
    x++;
    y++;

    for(int i=0; i<22; i++) {
        for(int j=0; j<22; j++)  field[i][j] = -1;
    }

    for(int i=1; i<=height; i++) {
        for(int j=1; j<=width; j++)  cin >> field[i][j];
    }

    for(int i=0; i<commandCount; i++) {
        int answerIndex = 0;
        int commandInput;
        cin >> commandInput;

        getTop(commandInput-1);
    }

    for(int i=0; i<answer.size(); i++)   cout << answer[i] << endl;

    return 0;
}

void getTop(int command) {
    int currentY = y+ewnsY[command];
    int currentX = x+ewnsX[command];

    if(field[currentY][currentX] == -1) return;

    moveDice(command);

    y = currentY;
    x = currentX;

    if(field[y][x] == 0)    field[y][x] = dice[5-diceTop];
    else {
        dice[5-diceTop] = field[y][x];
        field[y][x] = 0;
    }

    answer.push_back(dice[diceTop]);
}

void moveDice(int command) {
    int top = diceTop;

    switch (command) {
        case 0:
            diceTop = 5 - diceRight;
            diceRight = top;

            break;

        case 1:
            diceTop = diceRight;
            diceRight = 5 - top;
            
            break;

        case 2:
            diceTop = 5 - diceFront;
            diceFront = top;
            
            break;

        case 3:
            diceTop = diceFront;
            diceFront = 5 - top;
            
            break;
        
        default:
            break;
    }
}