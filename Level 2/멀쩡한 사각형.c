#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

long long solution(int w, int h) {
    // 반으로 나누고 마지막에 *2를 한다.
    long long answer = 1;
    answer = 0;
    // 1열에 에대하여 h/w를 rate로 한다면 0 * rate, i열에 대하여 rate * (i-1)만큼 더한다.
    // 단, 부동소수점 오차를 없애기 위하여 곱하기를 먼저하고 나누기를 마지막에 한다.
    for (int i = 0; i<w; i++) {
        answer += (int)(h * (double)i / (double)w);
    }
    return answer * 2;
}
// 1/11 해결(4주차 풀이 링크1)