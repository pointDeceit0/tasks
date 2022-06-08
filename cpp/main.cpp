#include <iostream>

int main() {
    for (int a = 0; a < 2; a++) {
        for (int b = 0; b < 2; b++) {
            for (int c = 0; c < 2; c++) {
                for (int d = 0; d < 2; d++) {
                    if (a || b || !c || d)
                        std::cout << "1\n";
                    else std::cout << "0\n";
                }
            }
        }        
    }

    return 0;
}


