#include <bits/stdc++.h>
#define FASTIO                   \
    ios::sync_with_stdio(false); \
    cin.tie(0);                  \
    cout.tie(0);
using namespace std;

int n, ans;
bool check1[14], check2[27], check3[27];

void solve(int idx)
{
    if (idx == n)
    {
        ans++;
        return;
    }

    for (int i = 0; i < n; i++)
    {
        if (check1[i] || check2[idx + i] || check3[idx - i + n - 1])
            continue;

        check1[i] = true;
        check2[idx + i] = true;
        check3[idx - i + n - 1] = true;

        //퀸 배치 - 체크 배열 수정

        solve(idx + 1);

        check1[i] = false;
        check2[idx + i] = false;
        check3[idx - i + n - 1] = false;

        //퀸 배치 원상태로 돌리기 - 체크 배열 수정
    }
}

int main()
{
    FASTIO
    cin >> n;
    solve(0);
    cout << ans;
    return 0;
}

/*
한 줄에 하나씩만 올 수 있다.
따라서 전부 막히는 줄이 발생하면 가지치기를 해줘야 한다.

check 배열로 세로/좌대각/우대각을 확인해준다.
한 줄에 하나씩만 배치하므로 가로를 확인해줄 필요는 없다.
check 배열의 경우 x좌표로 세로를, x+y의 합으로 대각선 존재 여부를 확인해준다.
*/