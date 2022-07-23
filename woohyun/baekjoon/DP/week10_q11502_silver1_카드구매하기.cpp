#include <iostream>
#include <vector>
using namespace std;

int card_count;
vector<int> prices;

void get_max_price();

int main() {
    cin >> card_count;

    for(int i=0; i<card_count; i++) {
        int price;
        cin >> price;

        prices.push_back(price);
    }
    
    get_max_price();

    return 0;
}

void get_max_price() {
    for(int i=0; i<prices.size(); i++) {
        for(int j=0; j<(i+1)/2; j++) {
            prices[i] = prices[j] + prices[i-1-j] > prices[i] ? prices[j] + prices[i-1-j] : prices[i];
        }
    }

    cout << prices[card_count - 1];
}