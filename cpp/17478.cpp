#include <bits/stdc++.h>
#define FASTIO ios::sync_with_stdio(false); cin.tie(0); cout.tie(0);
using namespace std;

int cnt, cur;

void solve() {
    string s; for (int i=0; i<cur; i++) s += "____";

    if (cur == cnt) {
        cout << s << "\"����Լ��� ������?\"" << '\n';
        cout << s << "\"����Լ��� �ڱ� �ڽ��� ȣ���ϴ� �Լ����\"" << '\n';
        cout << s << "��� �亯�Ͽ���." << '\n';
        return;
    }
    

    cout << s << "\"����Լ��� ������?\"" << '\n';
    cout << s << "\"�� ����. �������� �� �� ����⿡ �̼��� ��� ������ ����� ������ �־���." << '\n';
    cout << s << "���� ������� ��� �� ���ο��� ������ ������ �߰�, ��� �����Ӱ� ����� �־���." << '\n';
    cout << s << "���� ���� ��κ� �ǾҴٰ� �ϳ�. �׷��� ��� ��, �� ���ο��� �� ���� ã�ƿͼ� ������.\"" << '\n';
    
    cur += 1;
    solve();
    cur -= 1;

    cout << s << "��� �亯�Ͽ���." << '\n';
}

int main()
{
    FASTIO
    cin >> cnt;
    cout << "��� �� ��ǻ�Ͱ��а� �л��� ������ �������� ã�ư� ������." << '\n';
    solve();
    return 0;
}