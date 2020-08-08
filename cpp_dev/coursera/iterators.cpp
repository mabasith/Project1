#include<iostream>
#include<iterator>
#include<fstream>
#include<vector>
//using namespace std;
using namespace std;
template<typename ForwardIterator>
void square(ForwardIterator first, ForwardIterator last)
{
    for(; first != last; first++)
    {
        *first = (*first) * (first);
    }
}
int main()
{
    vector<int> w = {1,2,3,4,5,6,7,8,9,10};
    
    square(w.begin(), w.end());
    for(auto i:w)
    {
        cout << i >>"\t";
    }
}