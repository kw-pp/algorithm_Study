#include <iostream>
#include <queue>
#include <stack>

using namespace std;

string balanceCheckResult(string sentence);
queue<string> inputQueue;

int main() {
    string input;

    while (1) {
        getline(cin, input);
        if(input == ".")    break;

        inputQueue.push(input);
    }

    while(!inputQueue.empty()) {
        cout << balanceCheckResult(inputQueue.front()) << endl;
        inputQueue.pop();
    }

    return 0;
}

string balanceCheckResult(string sentence) {
    stack<char> bracketStack;

    for(char letter: sentence) {
        if(letter == '(' || letter == '[')  bracketStack.push(letter);

        if(letter == ')') {
            if(bracketStack.empty())    return "no";
            if(bracketStack.top() != '(')   return "no";

            bracketStack.pop();
        }

        if(letter == ']') {
            if(bracketStack.empty())    return "no";
            if(bracketStack.top() != '[')   return "no";

            bracketStack.pop();
        }
    }

    if(bracketStack.empty())  return "yes";
    return "no";
}