#include <iostream>
using namespace std;
#include <string>

int main(){
    cout << "sizeof int: " << sizeof(int) << endl;
    cout << "sizeof char: " << sizeof(char) << endl;
    cout << "sizeof float: " << sizeof(float) << endl;
    cout << "sizeof bool: " << sizeof(bool) << endl;
    string a[17];
    cout << "sizeof a var: " << sizeof(a)/sizeof(a[0]) << endl;
    int b[15];
    cout << "sizeof b var: " << sizeof(b)/sizeof(b[0]) << endl;
    return 0; // Ponéle una sizeof(arr) / sizeof(arr[0]) Ó sizeof(arr)[0] para sacar el número de elementos en arr!
}
