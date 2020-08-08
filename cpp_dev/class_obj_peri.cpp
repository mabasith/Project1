#include<iostream>
using namespace std;
class circle
{
	int r;
	public:
	double perimeter(int);
};
double circle :: perimeter(int a)
{
	r = a;
	return 2*3.14*r;
}
int main()
{
	circle peri;
	cout<<"Perimeter of a given circle is "<<peri.perimeter(4)<<"\n";
	return 0;
}
