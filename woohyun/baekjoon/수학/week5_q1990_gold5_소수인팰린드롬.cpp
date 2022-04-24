#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int minValue, maxValue;

vector<int> primes;
vector<int> palindromes;
vector<int> answers;

int reverseOf(int number);
int powersOfTen(int multi);
void setPrimes();
void setPalindromes();
void findAnswers();

// 입력이 1억까지 => 소수부터 찾으면 시간 초과 날 가능성이 높음
// palindrome부터 구해 queue에 넣고 소수 구하기
int main() {
    cin >> minValue >> maxValue;
    int ceiling = sqrt(maxValue) + 1;

    setPrimes();
    setPalindromes();
    findAnswers();

    for(int i=0; i<answers.size(); i++) cout << answers[i] << endl;
    cout << -1 << endl;

    return 0;
}

void setPrimes() {
    vector<int> primeVector;
    int sqrtMaxValue = sqrt(maxValue)+1;

    for(int i=5; i<=sqrtMaxValue; i += 2) {
        if(i%3 != 0)    primeVector.push_back(i);
    }

    int index=-1;

    while (1) {
        index++;

        if(index >= primeVector.size())                 break;
        if(primeVector[index] > sqrt(sqrtMaxValue)+1)   break;

        if(primeVector[index] == -1)                    continue;

        for(int j=0; j<primeVector.size(); j++) {
            if(primeVector[j]%primeVector[index] != 0)  continue;
            if(primeVector[j] != primeVector[index])    primeVector[j] = -1;
        }
    }

    for(int i=0; i<primeVector.size(); i++) {
        if(primeVector[i] != -1)    primes.push_back(primeVector[i]);
    }
}

void setPalindromes() {
    int maxLength = to_string(maxValue).size();

    if(minValue <= 5)   palindromes.push_back(5);
    if(minValue <= 7)   palindromes.push_back(7);

    for(int i=2; i<=maxLength; i++) {
        for(int j=powersOfTen((i-1)/2); j<powersOfTen((i+1)/2); j++) {
            int palindrome;

            if(i%2 == 0)    palindrome = j*powersOfTen(i/2) + reverseOf(j);
            else            palindrome = j*powersOfTen(i/2) + reverseOf(j/10);

            if(palindrome%2 == 0)       continue;
            if(palindrome%3 == 0)       continue;
            if(palindrome < minValue)   continue;
            if(palindrome > maxValue)   break;

            palindromes.push_back(palindrome);
        }
    }
}


void findAnswers() {
    for(int i=0; i<primes.size(); i++) {
        for(int j=0; j<palindromes.size(); j++) {
            if(palindromes[j] % primes[i] == 0 && palindromes[j] != primes[i]) {
                palindromes[j] = -1;
            }
        }
    }

    for(int i=0; i<palindromes.size(); i++) {
        if(palindromes[i] != -1)    answers.push_back(palindromes[i]);
    }
}

int powersOfTen(int multi) {
    if(multi == 0)  return 1;
    return 10*powersOfTen(multi-1);
}

int reverseOf(int number) {
    string numberString = to_string(number);
    reverse(numberString.begin(), numberString.end());

    return stoi(numberString);
}