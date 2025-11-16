#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int lcs(string s1, string s2) {
    int m = s1.length();
    int n = s2.length();
    int dp[m+1][n+1]; // Initialize the 2D array

    // Fill the first row and column with 0
    for(int i=0; i<=m; i++) dp[i][0] = 0;
    for(int j=0; j<=n; j++) dp[0][j] = 0;

    // Fill the rest of the array using dynamic programming
    for(int i=1; i<=m; i++) {
        for(int j=1; j<=n; j++) {
            if(s1[i-1] == s2[j-1]) dp[i][j] = 1 + dp[i-1][j-1];
            else dp[i][j] = max(dp[i-1][j], dp[i][j-1]);
        }
    }

    // Return the length of the LCS
    return dp[m][n];
}




string lcs_string(string s1, string s2) {
    int m = s1.length();
    int n = s2.length();
    int dp[m+1][n+1];

    // Initialize the 2D array
    for(int i=0; i<=m; i++) dp[i][0] = 0;
    for(int j=0; j<=n; j++) dp[0][j] = 0;

    // Fill the rest of the array using dynamic programming
    for(int i=1; i<=m; i++) {
        for(int j=1; j<=n; j++) {
            if(s1[i-1] == s2[j-1]) dp[i][j] = 1 + dp[i-1][j-1];
            else dp[i][j] = max(dp[i-1][j], dp[i][j-1]);
        }
    }

    // Find the LCS string by backtracking through the 2D array
    string lcs_str = "";
    int i = m, j = n;
    while(i > 0 && j > 0) {
        if(s1[i-1] == s2[j-1]) {
            lcs_str = s1[i-1] + lcs_str;
            i--;
            j--;
        } else if(dp[i-1][j] > dp[i][j-1]) {
            i--;
        } else {
            j--;
        }
    }

    return lcs_str;
}

int main() {
    string s1 = "ABAABA";
    string s2 = "BABBAB";

    // Test the first function
    int lcs_length = lcs(s1, s2);
    cout << "Length of LCS: " << lcs_length << endl;

    // Test the second function
    string lcs_str = lcs_string(s1, s2);
    cout << "LCS: " << lcs_str << endl;

    return 0;
}
