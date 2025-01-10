// Prime Familys

//SOLVED IN PYTHON 

#include <iostream>
#include <cmath>
#include <string>
#include <vector>
#include <map>
#include "Prime.cpp"
using namespace std;


bool vet(int num) { // Needs to have at least 1 digit 3+ times
    if(!prime_check(num)) { return false; }
    map<int, int> digToCount;
    int temp = num;
    while(temp != 0) {
        digToCount[temp%10] += 1;
        if(digToCount[temp%10] >= 3) { return true; }
        temp /= 10;
    }
    return false;
}

vector<int> customGenPrimes(int topNum) {
    vector<int> pList;
    int p1, p2;
    for(int k = 2; k < topNum / 6; k++){
        p1 = 6*k - 1;
        p2 = 6*k + 1;
        if(vet(p1)) { pList.push_back(p1); }
        if(vet(p2)) { pList.push_back(p2); }
    }

    return pList;
}



int main(){
    vector<int> pList = customGenPrimes(10000000);
    cout << "size: " << pList.size() << endl;
    // for(int p : pList) {
    //     cout << " | " << p;
    // }
    // cout << endl;
    return 0;
}