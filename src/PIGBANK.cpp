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
	scanf("%d", &tc);

	while(tc-- > 0){
		int e, f, n, c;
		scanf("%d %d", &e, &f);
		c = f-e;

		scanf("%d", &n);

		int p[n+1], w[n+1];
		for(int i = 1; i <= n; i++){
			scanf("%d %d", &p[i], &w[i]);
		}

		int dp[c+1]; dp[0] = 0;
		for(int i = 1; i <= c; i++){
			dp[i] = -1;
		}

		for(int i = 1; i <= c; i++){
			dp[i] = INF;
			for(int j = 1; j <= n; j++){
				if(w[j] <= i && p[j] + dp[i-w[j]] < dp[i]){
					dp[i] = p[j] + dp[i-w[j]];
				}
			}
		}
		if(dp[c] == INF){
			printf("This is impossible.\n");
		} else{
			printf("The minimum amount of money in the piggy-bank is %d.\n", dp[c]);
		}
	}
}