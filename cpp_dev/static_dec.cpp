#include<iostream>
using namespace std;
class stated
{
	int x;
	public:
	static int dec;
	stated()
	{
		x = dec--;
	}
	void number()
	{
		cout << "Number is" << x << "\n";
	}
};
int stated :: dec;

int main()
{
	stated o1,o2;
	o1.number();
	o2.number();
	return 0;
}

			
