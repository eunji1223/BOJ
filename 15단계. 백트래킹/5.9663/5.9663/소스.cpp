#include <iostream>
using namespace std;

int col[15];
int N, total = 0;

bool check(int level) {
    for (int i = 0; i < level; i++) {
        if (col[i] == col[level] || abs(col[level] - col[i]) == level - i) {
            return false;
        }
    }
    return true;
}
void nqueens(int x) {
    if (x == N)
        total++;
    else {
        for (int i = 0; i < N; i++) {
            col[x] = i;
            if (check(x))
                nqueens(x + 1);
        }
    }
}
int main() {
    cin >> N;
    nqueens(0);
    cout << total;
}