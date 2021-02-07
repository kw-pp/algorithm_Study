#pragma warning(disable:4996)
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
int cnt = 0;

void NQueen(int N, int r, int** arr) {
    for (int j = 0; j < N; j++) {

        if (arr[r][j] == 0 && j == N - 1) {
            //printf("%d %d 백트래킹\n", r, j);
            return;
        }

        if (arr[r][j] == 0) {
            continue;
        }


        if (arr[r][j] == 1) {
            if (r == N - 1) {
                cnt++;
                //printf("%d %d NQueen찾기 성공!!!\n", r, j);
                return 1;
            }

            int** b;
            b = (int**)malloc(sizeof(int*) * N);
            for (int i = 0; i < N; i++) {
                b[i] = (int*)malloc(sizeof(int) * N);
                for (int j = 0; j < N; j++) b[i][j] = arr[i][j];
            }

            int** b;
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) b[i][j] = arr[i][j];
            }
            for (int z = 0; r + z < N; z++) {


                if (r + z < N) {
                    b[r + z][j] = 0;
                }
                if (r + z < N && j + z < N) {
                    b[r + z][j + z] = 0;
                }
                if (j - z >= 0) {
                    b[r + z][j - z] = 0;
                }

            }
            //for (int c = 0; c < N; c++) {
            //    for (int l = 0; l < N; l++) {

            //        printf("%d ", b[c][l]);

            //    }
            //    printf("\n");

            //}

            NQueen(N, r + 1, b);
        }

    }
    return 0;
}

int main(void)
{

    int N = 0;
    scanf("%d", &N);
    int r = 0;

    int** arr;
    arr = (int**)malloc(sizeof(int*) * N);
    for (int i = 0; i < N; i++) {
        arr[i] = (int*)malloc(sizeof(int) * N);
        for (int j = 0; j < N; j++) arr[i][j] = 1;
    }


    NQueen(N, r, arr);
    printf("%d", cnt);

}
