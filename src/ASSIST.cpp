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
#define MAX 35000

int main(){
	bool flag[MAX];
	for(int i = 0; i < MAX; i++){
		flag[i] = true;
	}
	vi lucky;

	for(int i = 2; i < MAX; i++){
		if(flag[i]){ 
			lucky.push_back(i);
			int step = 0;
			for(int j = i+1; j < MAX; j++){
				if(flag[j]){
					step++;
				}
				if(step == i){
					flag[j] = false;
					step = 0;
				}
			}
		}
	}
	int n;
	while(scanf("%d", &n) && n != 0){
		printf("%d\n", lucky[n-1]);
	}
}
