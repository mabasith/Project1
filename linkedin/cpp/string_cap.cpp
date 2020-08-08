#include <string>
#include <algorithm>
#include <locale>
#include <iostream>
#include "capital.h"
using namespace std;

int main()
{
    string s1 = "this is a string";
    cout << s1 << "\n";
    string s2(s1.size(),'.');
    cout << s2 <<"\n";
    transform(s1.begin(), s1.end(), s2.begin(), title_case());
    cout << s2 <<"\n";

}