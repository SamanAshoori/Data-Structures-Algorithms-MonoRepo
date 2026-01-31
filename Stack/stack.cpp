//Stack Implementation in C++
#include <iostream>

template<typename T>
class Stack {
private:
    int size;
    int top;
    T* arr;

public:
    //constructors and destructors
    Stack(int s) : size(s), top(-1), arr(new T[s]) {}
    //destructor to free allocated memory
    ~Stack() {
        delete[] arr;
    }

    //no copying allowed
    Stack(const Stack&) = delete;
    Stack& operator=(const Stack&) = delete;

    void push(T input){
        if(top == size - 1){
            std::cout << "Stack is full" << std::endl;
            return;
        }
        top++;
        arr[top] = input;
    }

    void pop(){
        if(top == -1){
            std::cout << "Nothing to pop" << std::endl;
            return;
        }
        top--;
    }

    void peek() const {
        if(top == -1){
            std::cout << "Stack is empty" << std::endl;
            return;
        }
        std::cout << "Top element: " << arr[top] << std::endl;
    }
    
    void print() const {
        if(top == -1){
            std::cout << "Stack is empty" << std::endl;
            return;
        }
        for(int i = top; i >= 0; --i){
            std::cout << arr[i] << " ";
        }
        std::cout << std::endl;
    }

    void copy_and_resize(int new_size) {
        if(new_size <= size){
            std::cout << "New size must be greater than current size" << std::endl;
            return;
        }
        T* new_arr = new T[new_size];
        for(int i = 0; i <= top; ++i){
            new_arr[i] = arr[i];
        }
        delete[] arr;
        arr = new_arr;
        size = new_size;
    }
};

int main(){
    Stack<int> s(5);
    s.push(10);
    s.print();
    s.push(20);
    s.print();
    s.push(30);
    s.print();
    s.peek();
    s.pop();
    s.print();
    s.pop();
    s.print();
    s.pop(); // Attempt to pop from empty stack

    return 0;
}