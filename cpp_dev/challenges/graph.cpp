#include<iostream>
#include<vector>
using namespace std;

int elements[4]={2,5,7,9};
vector<vectror<int>> v(4);
v(4).resize(4);
for(int i =0; i<4;i++)
{
    int src, dest;
    cin>> src >> dest;
    for(int j =0; j<4; j++)
    {
        if ( src == elements[i] && dest == elements[j])
        {
            v[i][j] =1;
        }
        else
        {
            v[i][j] =0;
        }
    }
}


