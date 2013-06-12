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
		int n;
		scanf("%d", &n);

		int grid[101][101];

		memset(grid, 0, sizeof grid);

		for(int i = 0; i < n; i++){
			int a, b;
			scanf("%d %d", &a, &b);
			grid[a][b] = 1;
		}

		int maxcolor = 0;
		for(int i = 1; i <= 100; i++){
			for(int j = 1; j <= 100; j++){
				if(grid[i][j] == 1){
					int count = 0;
					if(i+2 <= 100 && j+1 <= 100 && grid[i+2][j+1] == 1) count++;
					if(i+2 <= 100 && j-1 >= 0 && grid[i+2][j-1] == 1) count++;
					if(i+1 <= 100 && j+2 <= 100 && grid[i+1][j+2] == 1) count++;
					if(i+1 <= 100 && j-2 >=0 && grid[i+1][j-2] == 1) count++;
					if(i-2 >= 0 && j+1 <= 100 && grid[i-2][j+1] == 1) count++;
					if(i-2 >= 0 && j-1 >= 0 && grid[i-2][j-1] == 1) count++;
					if(i-1 >= 0 && j+2 <= 100 && grid[i-1][j+2] == 1) count++;
					if(i-1 >= 0 && j-2 >= 0 && grid[i-1][j-2] == 1) count++;

					maxcolor = max(maxcolor, count);
				}
			}
			if(maxcolor == 8) break;
		}
		printf("%d\n", maxcolor);
	}
}