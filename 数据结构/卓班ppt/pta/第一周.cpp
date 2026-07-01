#include <stdio.h>
#include <time.h>

int main(void)
{
    clock_t start, end;
    volatile long long sum = 0;  // volatile 防止编译器优化
    long long count = 0;

    start = clock();
    while (1)
    {
        for (int i = 0; i < 1000000; i++)
            sum += i;

        count += 1000000;
        end = clock();

        double elapsed = (double)(end - start) / CLOCKS_PER_SEC;
        if (elapsed >= 1.0)  // 运行大约 1 秒
        {
            printf("运行时间: %.3f 秒\n", elapsed);
            printf("执行总次数: %lld 次\n", count);
            printf("平均每秒执行约: %.0f 次\n", count / elapsed);
            break;
        }
    }

    return 0;
}
