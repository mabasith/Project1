#include <iostream>
using namespace std;
int f(int &x, int c) {
c--; x--; // LINE-1
cout<<"before check : "<< c<<endl;
if (c == 0) return 1; // LINE-2
cout<<"after check : "<< c<<endl;
cout<<f(x, c) * x<<endl;
return f(x, c) * x; // LINE-3
}
int main() {
int a = 2, b = 2;
int c = f(a, b);
cout << c << endl;
return 0;
}