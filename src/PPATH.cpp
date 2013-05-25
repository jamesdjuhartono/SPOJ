#include <iostream>
#include <algorithm>
#include <vector>
#include <string.h>
#include <map>
#include <math.h>
#include <stdio.h>
#include <queue>

using namespace std;

typedef vector<int> vi;

bool isPrime[10001];
map<int,vi> graph;

void fillPrimes();
void makeGraph();

int main(){
	fillPrimes();
	makeGraph();

	int tc;
	int start, end;
	map<int, int> dist;
	queue<int> q;

	cin >> tc;
	while(tc-- > 0){
		scanf("%d %d",&start,&end);
		dist.clear();
		while(!q.empty()) q.pop();

		dist[start] = 0;
		q.push(start);

		while(!q.empty()){
			int u = q.front();
			q.pop();
			
			if (u == end){
				cout << dist[u] << endl;
				break;
			}

			vi adj = graph[u];
			for(int j = 0; j < adj.size(); j++){
				int next = adj[j];

				if(dist.count(next) == 0){
					q.push(next);
					dist[next] = dist[u] + 1;
				}
			}
		}
	}
}

void fillPrimes(){
	memset(isPrime, true, sizeof isPrime);
	isPrime[0] = isPrime[1] = false;

	for(int i = 2; i < 10001; i++){
		if(isPrime[i]){
			for(int j = 2*i; j < 10001; j+=i){
				isPrime[j] = false;
			}
		}
	}
}

void makeGraph(){
	for(int i = 1000; i < 10001; i++){
		vi adjacent;

		if(isPrime[i]){
			int digits[] = {(i/1000)%10, (i/100)%10, (i/10)%10, i%10};

			for(int j = 0; j < 4; j++){
				int num = i - digits[j]*pow(10,3-j);

				for(int k = 0; k < 10; k++){
					if(j == 0 && k == 0) continue;
					int newnum = num + k*pow(10,3-j);
					if(isPrime[newnum] && newnum != i){
						adjacent.push_back(newnum);
					}
				}
			}
			graph[i] = adjacent;
		}
	}
}