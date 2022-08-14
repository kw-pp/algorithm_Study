#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>

using namespace std;

vector<int>* road_array;
bool* visited;

int shortest(int start, int finish);

vector<int> solution(int n, vector<vector<int>> roads, vector<int> sources, int destination) {
    vector<int> answer;
    road_array = new vector<int>[n+1];

    for(int i=0; i<roads.size(); i++) {
        road_array[roads[i][0]].push_back(roads[i][1]);
        road_array[roads[i][1]].push_back(roads[i][0]);
    }

    for(int i=0; i<sources.size(); i++) {
        visited = new bool[n+1];
        answer.push_back(shortest(destination, sources[i]));
    }

    return answer;
}

int shortest(int start, int finish) {
    queue<int> visiting;
    int distance = 0;

    visiting.push(start);
    visited[start] = true;

    while(visiting.size() > 0) {
        int current_visiting_count = visiting.size();

        for(int i=0; i<current_visiting_count; i++) {
            int current = visiting.front();
            visiting.pop();

            if(current == finish)   return distance;

            for(int j=0; j<road_array[current].size(); j++) {
                int next = road_array[current][j];

                if(visited[next])  continue;

                visiting.push(next);
                visited[next] = true;
            }
        }

        distance++;
    }

    return -1;
}