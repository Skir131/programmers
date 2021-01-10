#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

long long solution(int w, int h) {
    long long answer = 1;
    answer = 0;
    for (int i = 0; i<w; i++) {
        answer += (int)(h * (double)i / (double)w);
    }
    return answer * 2;
}
// 1/11 해결