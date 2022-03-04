#include <iostream>
#include <string>
using namespace std;
int a = 40;
//unsigned int cc = 900000000000;
//long cd = 900000000000;
int num;
int arr[5];
int poparr[5] = {24, 20, 16, 8, 4};
int counter = 1;
string aa = "Send help please";
//bool cb = false;
int* bc = &counter; // This is a pointer towards counter
// to_string()
int main() {
    cout << bc << '\n';
    //cout << cc << ' ' << cd << endl;
    cout << "Numero? " << a << endl << "===============\n";
    cin >> num;
    if (num > 5){
        cout << "Bien hecho!\n\n";
    }
    else if (num == 5){
      cout << "Noooooo\n\n";
    }
    cout << "Number: " << 5 + num << endl << "============\n";
    cout << aa << endl;
    while (counter != 11){
      cout << counter;
      counter++;
    }
    cout << "\n";
    for (int el = 1; el != 11; el++){
      cout << el;
    }
    printf("\n");
    for (int el = 0; el != 6; el++){
      arr[el] = arr[el] + arr[el - 1] + 4;
    }
    for (int el = 0; el != 5; el++){
      cout << arr[el] << ' ';
    }
    printf("\n");
    for (int el = 0; el != 5; el++){
      cout << poparr[el] << ' ';
    }
    return 0;
}
/*
goto crash;
crash:
  printf("Oops!");
  return 0;
*/
