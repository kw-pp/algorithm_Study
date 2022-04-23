#include <iostream>
#include <vector>
using namespace std;

int numberCount;
int *numbers;
int maxValue;
int minValue;

void search(int previous, int index, int currentOperator, vector<int> otherOperators);
int calculate(int value, int operand, int currentOperator);


int main() {
    int operatorCount;
    vector<int> operators;

    cin >> numberCount;
    numbers = new int[numberCount];

    minValue = 1000000000;
    maxValue = -1000000000;
    
    for(int i = 0; i < numberCount; i++)    cin >> numbers[i];
    for(int i = 0; i < 4; i++) {
        cin >> operatorCount;
        
        for(int j = 0; j < operatorCount; j++)  operators.push_back(i);
    }

    search(0, 0, 0, operators);

    cout << maxValue << endl << minValue << endl;

    return 0;
}

void search(int previous, int index, int currentOperator, vector<int> otherOperators) {
    int result = calculate(previous, numbers[index], currentOperator);

    if(otherOperators.size() == 0) {
        maxValue = maxValue < result ? result : maxValue;
        minValue = minValue > result ? result : minValue;

        return;
    }

    for(int i = 0; i < otherOperators.size(); i++) {
        int nextOperator = otherOperators[i];

        vector<int> nextOperators = otherOperators;
        nextOperators.erase(nextOperators.begin() + i);

        search(result, index + 1, nextOperator, nextOperators);
    }
}

int calculate(int value, int operand, int currentOperator) {
    if(currentOperator == 0)   return value + operand;
    if(currentOperator == 1)   return value - operand;
    if(currentOperator == 2)   return value * operand;
    if(currentOperator == 3)   return value / operand;
}