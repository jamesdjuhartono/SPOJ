#include <iostream>

using namespace std;

int main(){
	int query;
	int ans[101];

	ans[0] = 0;
	for(int i = 1; i < 101; i++){
		ans[i] = ans[i-1] + (i*i);
	}

	cin >> query;
	while(query != 0){
		cout << ans[query] << endl;
		cin >> query;
	}
}