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
	int tc;
	scanf("%d" ,&tc);

	while(tc-- > 0){
		int n;
		scanf("%d", &n);
		int towns[n][n];

		for(int i = 0; i < n; i++){
			for(int j = 0; j < n; j++){
				scanf("%d", &towns[i][j]);
			}
		}

		for(int i = 0; i < n; i++){
			for(int j = i+1; j < n; j++){
				int currdist = towns[i][j];
				bool neighbour = true;
				for(int k = 0; k < n; k++){
					if(k == i || k == j) continue;
					else if(towns[i][k] + towns[k][j] == currdist){
						neighbour = false;
						break;
					}
				}
				if(neighbour) printf("%d %d\n", i+1, j+1);
			}
		}
		if(tc) printf("\n");
	}
}
