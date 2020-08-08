// A constructor is a member fuction. It has the same name as class name.
// constructor can not return values. It automatically create when an object is created.


#include<iostream>
using namespace std;
class Addition
{
	int a, b;
	public:
	Addition (int, int);
	int add()
	{
		return (a+b);
	}
	~Addition();
};
Addition :: Addition(int x, int y)
{
	a = x;
	b = y;
}
Addition :: ~Addition()
{
	cout<< "Memory Deallocation\n";
}
int main()
{
	Addition obj (3,4);
	cout << "Sum is "<<obj.add() << "\n";
	return 0;
}

