#include <iostream>

using namespace std;

// int gcd(int a, int b){
// 	if (a >= b){
// 		if (a % b == 0){
// 			return b;
// 		}
// 		else {
// 			gcd(b,a-b);
// 		}
// 	}
// 	else{
// 		gcd(b,a);
// 	}
// }

int gcd (int a, int b) {
	if (b == 0)
		return a;
	else
		return gcd (b, a % b);
}
// 24 18 18 6 6 3 6 0

int main()
{
	int a,b;
	cin>>a>>b;
	cout<<gcd(a,b);
	return 0;
}