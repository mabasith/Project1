#include<iostream>
using namespace std;
class student
{
	protected:
		int roll_no;
		char name[20];

};

class exam_inherit
{
	protected:
		int sub1;
		int sub2;
		int sub3;
};

class grad:public student, public exam_inherit
{
	private:
		int avg;
	public:
		void input();
		void display();
		void average();
		int total;
		void input_exam();
		void display_exam();
};

void grad :: input()
{
	cout<<" enter roll no: ";
	cin>>roll_no;
	cout<<"Enter name: ";
	cin>>name;
}
void grad :: display()
{
	cout<<"Roll number is: "<<roll_no<<"\n";
	cout<<"Name : "<< name<<"\n";
}
void grad::input_exam()
{
	cout<< "Enter first subject mark: ";
	cin >>sub1;
	cout<<"Enter second subject mark: ";
	cin>>sub2;
	cout<<"Enter third subject mark: ";
	cin>>sub3;
}
void grad::display_exam()
{
	total = sub1+sub2+sub3;
	cout<<"Total is : "<<total<<"\n";
}
void grad::average()
{
	avg=total/3;
	cout<<"Average is : "<<avg<<"\n";
}
int main()
{
	grad gd;
	gd.input();
	gd.input_exam();
	gd.display();
	gd.display_exam();
	gd.average();
	return 0;
}
