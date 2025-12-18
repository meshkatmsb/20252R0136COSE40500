from typing import List

def longest_common_subsequence(a: str, b: str) -> int:
    """
    Longest Common Subsequence (LCS)

    Dynamic Programming approach.
    Time Complexity: O(n * m)
    Space Complexity: O(n * m)
    """
    n, m = len(a), len(b)
    dp: List[List[int]] = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[n][m]


if __name__ == "__main__":
    s1 = "ABCBDAB"
    s2 = "BDCAB"
    print(longest_common_subsequence(s1, s2))
