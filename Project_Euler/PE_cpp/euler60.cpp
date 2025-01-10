// SOLVED
#include <iostream>
#include <cmath>
#include <string>
#include <vector>
#include "Prime.cpp"
using namespace std;

int concat(int a, int b) {
    return stoi(to_string(a) + to_string(b));
} 

bool validPair(int a, int b) {
    return prime_check(concat(a,b)) && prime_check(concat(b,a));
}
bool validTrio(int a, int b, int c) {
    return validPair(a,b) && validPair(b,c) && validPair(a,c);
}
bool validQuad(int d, int c, int b, int a) {
    return validTrio(a, b, c) && validTrio(a, b, d) && validTrio(a, c, d) && validTrio(b, c, d);
}
bool valid5(int a, int b, int e, int d, int c) {
    return validQuad(a, b, c, d) && validQuad(a, b, c, e) && validQuad(a, b, d, e) && validQuad(a, c, d, e) && validQuad(b, c, d, e);
}

bool addPairTrio(int a, int b, int z) { // assummes a and b are good
    return validPair(a,z) && validPair(b,z);
}
bool addPairQuad(int a, int b, int c, int z) { // assummes a and b are good
    return validPair(a,z) && validPair(b,z) && validPair(c,z);
}
bool addPair5(int a, int b, int c, int d, int z) { // assummes a and b are good
    return validPair(a,z) && validPair(b,z) && validPair(c,z) && validPair(d,z);
}

// Runtime: O(p^t), Space O(t)~O(1)
// p is # of primes, t is # in the related group
void bruteForce5(){  // O(p^5)
    vector<int> pList = primes_count(60);
    unsigned size = pList.size();
    for(unsigned a = 0; a < size - 4; a++) {
        int ap = pList[a];
        for(unsigned b = a + 1; b < size - 3; b++) {
            int bp = pList[b];
            for(unsigned c = b + 1; c < size - 2; c++) {
                int cp = pList[c];
                for(unsigned d = c + 1; d < size - 1; d++) {
                    int dp = pList[d];
                    for(unsigned e = d + 1; e < size; e++) {
                        int ep = pList[e];
                        if(valid5(ap, bp, cp, dp, ep)) {
                        cout << "(" << ap << "," << bp << "," << cp << "," << dp << "," << ep << ")" << "_" << endl;
                        cout << "Sum: " << ap + bp + cp + dp + ep;
                        }
                    }
                    
                }
            }
        }
    }
}

// Runtime: O(p^t), Space O(t)~O(1)
// p is # of primes, t is # in the related group
void bruteForce4(){ // 11 seconds to scan 1000 primes, looking for Quad
    vector<int> pList = primes_top(1000);
    unsigned size = pList.size();
    for(unsigned a = 0; a < size - 3; a++) {
        int ap = pList[a];
        for(unsigned b = a + 1; b < size - 2; b++) {
            int bp = pList[b];
            for(unsigned c = b + 1; c < size - 1; c++) {
                int cp = pList[c];
                for(unsigned d = c + 1; d < size; d++) {
                    int dp = pList[d];
                    if(validQuad(ap, bp, cp, dp)) {
                        cout << "(" << ap << "," << bp << "," << cp << "," << dp << ")" << "_" << endl;
                        cout << "Sum: " << ap + bp + cp + dp;

                    }
                }
            }
        }
    }
}

void strat1() {
    vector<int> pList = primes_count(1200);
    unordered_map<int, vector<int> > pairMap; // Index to other Indicies
    int size = pList.size();
    cout << "Top Prime: " << pList[size - 1] << endl;
    int n = 0;
    for(unsigned i = 0; i < size - 1; i++) {
        for(unsigned j = i + 1; j < size; j++) {
            if(validPair(pList[i],pList[j])){
                pairMap[i].push_back(j);
                n++;
            }
        }
    }
    cout << "Map Size: " << pairMap.size() << endl;
    
    cout << "Bef, n is : " << n << endl;

    // for(unsigned i = 0; i < size - 1; i++) {
    //     vector<int>& vect = pairMap[i];
    //     for(unsigned x = 0; x < vect.size() - 1)
    // }

}

void strat2() { 
    // n = 100 -- > 90 seconds --> 41.5 --> 1.16 -->
    // n = 200 --> 31 seconds --> 1.86
    // n = 300 --> 7.80 --> 5.3  // n = 500 --> 53 --> 31

    int n = 300;
    vector<int> pList1 = primesCongr1(n); // Primes Congruent 1 mod3 (Won't reach digit sum congr 0 Mod3 (composite))
    vector<int> pList2 = primesCongr2(n + 2);  // // Primes Congruent 2 mod 3
    pList2.erase(pList2.begin()+1); // removing 2 and 5 (concat is always composite)
    pList2.erase(pList2.begin());

    cout << "highest prime: " << pList2[n-1] << endl;
    for(int a = 0; a < n - 4; a++) {
        int a1 = pList1[a];
        int a2 = pList2[a];
        for(int b = a+1; b < n - 3; b++) {
            int b1 = pList1[b];
            int b2 = pList2[b];
            if(!(validPair(a1,b1) || validPair(a2,b2))) {
                continue;
            }
            for(int c = b+1; c < n - 2; c++) {
                int c1 = pList1[c];
                int c2 = pList2[c];
                if(!(validTrio(a1,b1,c1) || validTrio(a2,b2,c2))) {
                    continue;
                }
                for(int d = c+1; d < n - 1; d++) {
                    int d1 = pList1[d];
                    int d2 = pList2[d];
                    if(!(validQuad(a1,b1,c1, d1) || validQuad(a2,b2,c2,d2))) {
                        continue;
                    }
                    for(int e = d+1; e < n  ; e++) {
                        int e1 = pList1[e];
                        int e2 = pList2[e];

                        if(valid5(a1, b1, c1, d1, e1)) {
                            cout << "(" << a1 << "," << b1 << "," << c1 << "," << d1 << "," << e1 << ")" << "_" << endl;
                            cout << "Sum: " << a1 + b1 + c1 + d1 + e1;
                        }
                        if(valid5(a2, b2, c2, d2, e2)) {
                            cout << "(" << a2 << "," << b2 << "," << c2 << "," << d2 << "," << e2 << ")" << "_" << endl;
                            cout << "Sum: " << a2 + b2 + c2 + d2 + e2;
                        }
                    }
                }
            }
        }
    }
}


void strat3() { 
    // n = 500 --> 5.50 seconds
    int n = 600; // 10 seconds, Solved
    vector<int> pList1 = primesCongr1(n); // Primes Congruent 1 mod3 (Won't reach digit sum congr 0 Mod3 (composite))
    vector<int> pList2 = primesCongr2(n + 2);  // // Primes Congruent 2 mod 3
    pList2.erase(pList2.begin()+1); // removing 2 and 5 (concat is always composite)
    pList2.erase(pList2.begin());
    vector<int> pList = pList1;

    cout << "highest prime: " << pList[n-1] << endl;
    for(int a = 0; a < n - 4; a++) {
        int a1 = pList[a];
        for(int b = a+1; b < n - 3; b++) {
            int b1 = pList[b];
            if(!(validPair(a1,b1))) { continue; }
            for(int c = b+1; c < n - 2; c++) {
                int c1 = pList[c];
                if(!(addPairTrio(a1,b1,c1))) { continue; }
                for(int d = c+1; d < n - 1; d++) {
                    int d1 = pList[d];
                    if(!(addPairQuad(a1,b1,c1,d1))) { continue; }
                    for(int e = d+1; e < n  ; e++) {
                        int e1 = pList[e];
                        if(addPair5(a1, b1, c1, d1, e1)) {
                            cout << "(" << a1 << "," << b1 << "," << c1 << "," << d1 << "," << e1 << ")" << "_" << endl;
                            cout << "Sum: " << a1 + b1 + c1 + d1 + e1 << endl;
                        }
                    }
                }
            }
        }
    }

    pList = pList2;
    for(int a = 0; a < n - 4; a++) {
        int a1 = pList[a];
        for(int b = a+1; b < n - 3; b++) {
            int b1 = pList[b];
            if(!(validPair(a1,b1))) { continue; }
            for(int c = b+1; c < n - 2; c++) {
                int c1 = pList[c];
                if(!(addPairTrio(a1,b1,c1))) { continue; }
                for(int d = c+1; d < n - 1; d++) {
                    int d1 = pList[d];
                    if(!(addPairQuad(a1,b1,c1,d1))) { continue; }
                    for(int e = d+1; e < n  ; e++) {
                        int e1 = pList[e];
                        if(addPair5(a1, b1, c1, d1, e1)) {
                            cout << "(" << a1 << "," << b1 << "," << c1 << "," << d1 << "," << e1 << ")" << "_" << endl;
                            cout << "Sum: " << a1 + b1 + c1 + d1 + e1;
                        }
                    }
                }
            }
        }
    }
}


int main(){
    strat3();
    // SOLVED
}