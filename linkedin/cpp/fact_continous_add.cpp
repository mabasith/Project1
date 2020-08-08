#include <iostream>

using namespace std;

auto continousAdd = [](int initial , int addBy)
{
    auto total = initial;
    return [total, addBy]() mutable{
        total += addBy;
        return total;
    };
};

int main()
{
    auto x = continousAdd(1000,10);
    cout << x() << endl;
    cout << x() << endl;

    return 0;
}