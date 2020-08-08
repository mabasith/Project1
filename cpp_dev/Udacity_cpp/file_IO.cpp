#include<iostream>
#include<fstream>
#include<string>

using namespace std;

int main()
{
    string line;
    // create an out put stream to write to the file
    //append the new lines to the end of the file
    ofstream myfileI ("input.txt", ios::app);
    if(myfileI.is_open())
    {
        myfileI <<"\n I am adding a line. \n";
        myfileI <<"I am adding another line. \n";
        myfileI.close();
    }
    else
    {
    cout << " Unable to open file for writing";
    }

    ifstream myfileO ("input.txt");
    if (myfileO.is_open())
    {
        while(getline(myfileO,line))
        {
            cout << line <<'\n';
        }
        myfileO.close();
    }
    else
    {
        cout << "Unable to read file";
    }
    
    
}