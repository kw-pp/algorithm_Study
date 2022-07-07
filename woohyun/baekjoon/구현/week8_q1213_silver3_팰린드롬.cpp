#include <iostream>
#include <algorithm>
#include <map>
using namespace std;

const string sorry = "I'm Sorry Hansoo";
map<char, int> letter_counts;

string palindrome();

int main() {
    string input;
    cin >> input;

    for(int i=0; i<input.size(); i++)   letter_counts[input[i]]++;
    cout << palindrome();

    return 0;
}

string palindrome() {
    string result = "";
    string reversed = "";

    int odd_count = 0;
    char odd_letter = '-';

    for(auto iter = letter_counts.begin(); iter != letter_counts.end(); ++iter) {
        char letter = iter->first;
        int length = iter->second;

        if(length % 2 == 1) {
            odd_count++;
            odd_letter = letter;
        }

        if(odd_count > 1)   return sorry;

        for(int i=0; i<length/2; i++) {
            result += letter;
            reversed += letter;
        }
    }

    reverse(reversed.begin(), reversed.end());

    if(odd_letter == '-')   return result + reversed;
    return result + odd_letter + reversed;
}