#include<iostream>
using namespace std;

long int factorial(int n)
{
	return (n < 2) ? 1 : (n * factorial(n-1));
}
double combination(int sides)
{
	return factorial(sides)/(factorial(3)*factorial(sides - 3));
}
int main()
{
	int num_test;
	cin >> num_test;
	while(num_test != 0)
	{
		int num_sides, v_black1, v_black2;
		cin >> num_sides >> v_black1 >> v_black2;
		cout << combination(num_sides-2);
		num_test -= 1;
	}
	return 0;
}g