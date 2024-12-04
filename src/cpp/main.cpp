#include <iostream>
#include <fstream>
#include "day3.h"
using namespace std;

int main() {
    ifstream f("../day3.txt");
    if(f.is_open()) {
        cout << "File Opened \n";
        int a = day3::partI(f);
    }
    else {
        cout << "Error opening file" << endl;
    }
    return 0;
}