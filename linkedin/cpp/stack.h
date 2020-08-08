#ifndef _STACK
#define _STACK

#include <exception>

//simple exception class

class StackException : public std::exception {
    const char * msg;
    StackException(){};
    public:
    explicit StackException(const char * s) throw() : msg(s) {}
    const char * what() const throw() {return msg;}
};

// simple fixed size LIFO stack templete

template <typename T>
class Stack
{
private:
    static const int defaultSize = 10;
    static const int maxSize = 1000;
    int _size;
    int _top;
    T * stackPtr;
public:
    explicit Stack(int s = defaultSize);
    ~Stack(){ delete[] stackPtr;}
    T & push(const T &)
    T & pop();
    bool isEmpty() const {return _top<0;}
    bool isFull() const { return _top >= _size - 1;}
    int top() const { return _top;}
    int size() const { return _size;}

};

#endif // _STACK


