#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <numeric>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <cctype>
#include <climits>
#include <string>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

#define INF	(int)1e9
#define EPS 1e-9

int main(){
	int n;
	while(scanf("%d", &n) != EOF && n != 0){
		queue<int> q;
		stack<int> s;

		for(int i = 0; i < n; i++){
			int num;
			scanf("%d", &num);
			q.push(num);
		}

		int idx = 1;
		bool possible = true;
		while(!q.empty()){
			int curr = q.front();
			q.pop();

			while(!s.empty() && s.top() == idx){ //try to see if those on side-road can move
				s.pop();
				idx++;
			}
			if(curr == idx){ //maybe after the move, the current truck can move
				idx++;
			} else{ //if still not possible, try to move curr truck to side-road
				if(!s.empty() && curr > s.top()){
					possible = false;
					break;
				} else{
					s.push(curr);
				}
			}
		}

		if(possible){
			printf("yes\n");
		} else{
			printf("no\n");
		}
	}
}