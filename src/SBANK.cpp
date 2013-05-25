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
	int n, tc;
	char str[100];

	scanf("%d", &tc);

	while(tc-- > 0) {
		map<string, int> accts;
		map<string, int> :: iterator it;
		scanf("%d\n", &n);

		for(int i = 0; i < n;i++) {
			gets(str);
			accts[(string)str]++;
		}

		for(it = accts.begin(); it != accts.end(); it++) printf("%s %d\n",(*it).first.c_str(), (*it).second); 
		if(tc > 0) printf("\n");
	}
	return 0;
}
