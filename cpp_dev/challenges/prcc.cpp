#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <iomanip>
using namespace std;
void get_data(vector<double> &data)
{
    for(auto &item:data)
        cin>>item;
}
int find_rank(vector<double> v, int i)
{
    vector<double> vsort;
    vsort = v;
    sort(vsort.begin(),vsort.end());
    vector<double>::iterator it;
    it = find(vsort.begin(),vsort.end(),v[i]);
    return distance(vsort.begin(), it) +1;
}
int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    double rankdiff = 0.0,prcc = 0.0;  
    int n;
    cin>>n;
    vector<double> x(n);
    vector<double> y(n);
    get_data(x);
    get_data(y);
    for(int i =0 ; i<n; i++)
    {
        //cout<<pow((find_rank(x,i)-find_rank(y, i)),2)<<endl;
        rankdiff +=pow((find_rank(x,i)-find_rank(y, i)),2);  
    }
    prcc = 1- (6*rankdiff)/(n*(pow(n,2)-1));
    cout<<fixed<<setprecision(3)<<prcc;
    return 0;
}