#include <stdio.h>

int main()
{
    int T, H, W, N;
    scanf("%d", &T);

    for (int i = 0; i < T; i++)
    {
        scanf("%d %d %d", &H, &W, &N);

        int F = H;
        int B = N / H;

        if (N % H != 0)
        {
            F = N % H;
            B = N / H + 1;
        }

        printf("%d\n", 100 * F * B);
    }
}