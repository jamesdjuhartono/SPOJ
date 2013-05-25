#include <iostream>
#include <math.h>
#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;

typedef vector<int> vi;

vi list;

void initVector(){
	for(long long i = 0; i <= 100000; i++){
		list.push_back((pow(i,2) + i) / 2);
	}
}

int main(){
	initVector();

	long long num;
	scanf("%lld", &num);

	while (num != -1){
		if (num % 6 == 1 && binary_search(list.begin(), list.end(), (num-1)/6)){
			printf("Y\n");
		} else{
			printf("N\n");
		}
		scanf("%lld", &num);
	}
}