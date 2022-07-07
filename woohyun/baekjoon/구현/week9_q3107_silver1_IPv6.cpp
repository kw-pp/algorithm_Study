#include <iostream>
#include <algorithm>
#include <vector>
#include <sstream>
using namespace std;

string short_address;

vector<string> split_by_single_colon(string input);
vector<string> split_by_double_colon(string input);

void restore();

int main() {
    cin >> short_address;
    restore();

    return 0;
}

vector<string> split_by_single_colon(string input) {
    vector<string> result;
    stringstream string_stream(input);
    string part;
 
    while (getline(string_stream, part, ':')) {
        result.push_back(part);
    }
 
    return result;
}

vector<string> split_by_double_colon(string input) {
    vector<string> result;
    string delimeter = "::";

    size_t pos = 0;
    string token;

    while ((pos = input.find(delimeter)) != string::npos) {
        token = input.substr(0, pos);
        result.push_back(token);
        input.erase(0, pos + delimeter.length());
    }
    
    result.push_back(input);
 
    return result;
}

void restore() {
    auto double_colon_splitted = split_by_double_colon(short_address);
    string double_colon_restored = "";
    int omitted_index = -1;

    for(int a=0; a<double_colon_splitted.size(); a++) {        
        auto single_colon_splitted = split_by_single_colon(double_colon_splitted[a]);
        string single_colon_restored = "";
        
        if(a == 0)  omitted_index = single_colon_splitted.size();

        if(a == 1) {
            for(int i=0; i<8-omitted_index-single_colon_splitted.size(); i++) {
                double_colon_restored += "0000:";
            }
        }
        
        for(int i=0; i<single_colon_splitted.size(); i++) {
            while (single_colon_splitted[i].size() != 4) {
                single_colon_splitted[i] = "0" + single_colon_splitted[i];
            }

            single_colon_splitted[i] += ":";
            single_colon_restored += single_colon_splitted[i];
        }

        double_colon_restored += single_colon_restored;
    }

    double_colon_restored.pop_back();
    cout << double_colon_restored << endl;
}