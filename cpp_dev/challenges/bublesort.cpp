#include<iostream>
#include<vector>
using namespace std;
void swap(long int &a, long int &b)
{
	a = a + b;
	b = a - b;
	a = a - b;
}
long int BubbleSort(vector<long int> v)
{
	long int count = 0;
	long int size = v.size();
	bool swapped = true;
	while(swapped != false)
	{
		swapped = false;
		count += 1;
		for(int i = 0 ; i < size - 1; i++)
		{
			if(v[i]>v[i+1])
			{
				swap(v[i],v[i+1]);
				swapped = true;
			}
		}
	}
	return count;
}
int main()
{
	long int n;
	cin >> n;
	vector<long int> arr(n);
	for(auto &item: arr)
		cin >> item;
	cout << BubbleSort(arr);
	return 0;
}
