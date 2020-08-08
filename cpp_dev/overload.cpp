#include<iostream>
using namespace std;
int add(int a, int b, int c)
{
	return(a+b+c);
}
float add(float d,float e)
{
	return(d+e);
}
int main()
{
	int add(int, int, int);
	float add(float, float);
	int a,b,c;
	float d,e,sum;
	cout<<"Enter three numbers \n";
	cin>>a>>b>>c;
	sum = add(a,b,c);
	cout<<"Sum of integer is "<<sum<<"\n";
	cout<<"Enter float numbers \n";
	cin>>d>>e;
	sum = add(d,e);
	cout<<"sum of float is "<<sum<<"\n";
	return 0;
}

