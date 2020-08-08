// static variable are initialized to zero before first object is created
// only one copy of the ststic variable exists for the whole program
// all the object will share that variable
// it will remain in the memory till the program
// a static function may be called by itself without depending on any object
// to access a static function we use classname :: staticfunction()
#include<iostream>
using namespace std;

class statex
{
	int x;
	public:
	static int sum;
	statex()
	{
		x=sum++;
		cout<<" Constructor called "<< sum<<"\n";
	}
	static void stat()
	{
		cout << "Result is: "<< sum << "\n";
	}
	void number()
	{
		cout << "Number: "<< x<< "\n";
	}
};
int statex :: sum;
int main()
{
	statex o1,o2;
	o1.number();
	statex :: stat();
	cout << "Now static var sum is "<<o1.sum<<"\n";
	return 0;
}

