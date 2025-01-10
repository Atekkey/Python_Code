#include <iostream>
#include <vector>
#include <cmath>
#include <chrono>
using namespace std::chrono;

bool prime_check(int num) {
    int cap = (int) (sqrt(num) + 1);
    for(int i = 2; i < cap; i++) {
        if(num % i == 0) { return false; }
    }
    return true;
}

std::vector<int> primes_top(int topNum) {
    std::vector<int> pList;
    pList.push_back(2);
    for(int x = 3; x < topNum; x += 2) {
        if(prime_check(x)==true) { pList.push_back(x); }
    }
    return pList;
}

std::vector<int> primes_count(int inCount) {
    std::vector<int> pList;
    pList.push_back(2);
    int x = 3;
    int count = 0;
    while(count != inCount) {
        if(prime_check(x)==true) { 
            pList.push_back(x); 
            count++;
        }
        x += 2;
    }
    return pList;
}

std::vector<int> primesCongr1(int inCount) {
    std::vector<int> pList;
    int k = 1;
    int count = 0;
    int p;
    while(count != inCount) {
        p = 6*k + 1;
        if(prime_check(p) == true) { 
            pList.push_back(p); 
            count++;
        }
        k += 1;
    }
    return pList;
}

std::vector<int> primesCongr2(int inCount) {
    std::vector<int> pList;
    pList.push_back(2);
    int k = 1;
    int count = 0;
    int p;
    while(count != inCount) {
        p = 6*k - 1;
        if(prime_check(p) == true) { 
            pList.push_back(p); 
            count++;
        }
        k += 1;
    }
    return pList;
}

// int main() {
//     auto start = high_resolution_clock::now();

//     std::cout << primes_top(500000).back() << std::endl;

//     auto stop = high_resolution_clock::now();
//     auto duration = duration_cast<milliseconds>(stop - start);
//     std::cout << duration.count() << " ms" << std::endl;

// }