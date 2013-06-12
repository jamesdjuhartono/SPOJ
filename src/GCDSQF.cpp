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
#include <bitset>

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
	scanf("%d\n", &tc);

	while(tc-- > 0){
		string a, b;
		cin >> a >> b;
		reverse(a.begin(), a.end());
		reverse(b.begin(), b.end());

		bitset<1001> first (a);
		bitset<1001> second(b);
		bitset<1001> ans = first&second;

		if(ans.none()){
			printf("relatively prime\n");
		} else{
			int iter = 0;
			int curr = 0;
			int count = ans.count();
			while(curr < count){
				if(ans[iter]){
					curr++;
				}
				printf("%d", ans[iter] & 0x1);
				iter++;
			}
			printf("\n");
		}
	}
}