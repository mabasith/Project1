#include<iostream>
using namespace std;
class Division
{
	int a, b;
	public:
	Division(int, int);
	int div()
	{
		return(a/b);
	}
};
Division :: Division (int x, int y)
{
	a = x;
	b = y;
}
int main()
{
	Division d(8,4);
	cout<< "Division is "<< d.div()<<"\n";
	return 0;
}

