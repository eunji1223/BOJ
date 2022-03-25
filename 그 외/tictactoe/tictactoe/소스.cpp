#define _CRT_SECURE_NO_WARNINGS 
#define WIDTH 3
#define HEIGHT 3
#include <stdio.h>
void display(int b[][HEIGHT])
{
    char ch;
    int i, j;

    printf("    0 1 2\n");
    printf("   ------\n");
    for (i = 0; i < WIDTH; i++)
    {
        printf("%d |", i);
        for (j = 0; j < HEIGHT; j++)
        {
            if (b[i][j] == -1)
                ch = ' ';
            else if (b[i][j] == 0)
                ch = 'X';
            else if (b[i][j] == 1)
                ch = 'O';
            printf(" %c", ch);
        }
        printf("\n");
    }
}

int winCheck(int b[][HEIGHT])
{
    int i, j;
    int sum;
    // ���η� ������ üũ
    if (b[0][0] == b[0][1] && b[0][1] == b[0][2] && b[0][0] != -1)
        return b[0][0];
    else if (b[1][0] == b[1][1] && b[1][1] == b[1][2] && b[1][0] != -1)
        return b[1][0];
    else if (b[2][0] == b[2][1] && b[2][1] == b[2][2] && b[2][0] != -1)
        return b[2][0];

    // ���η� ������ üũ
    if (b[0][0] == b[1][0] && b[1][0] == b[2][0] && b[0][0] != -1)
        return b[0][0];
    else if (b[0][1] == b[1][1] && b[1][1] == b[2][1] && b[0][1] != -1)
        return b[0][1];
    else if (b[0][2] == b[1][2] && b[1][2] == b[2][2] && b[0][2] != -1)
        return b[0][2];

    //�밢�� üũ
    if (b[0][0] == b[1][1] && b[1][1] == b[2][2] && b[0][0] != -1)
        return b[0][0];
    if (b[0][2] == b[1][1] && b[1][1] == b[2][0] && b[0][2] != -1)
        return b[0][2];

    return -1;
}
int main(void)
{
    int board[3][3] = {
        {-1, -1, -1},
        {-1, -1, -1},
        {-1, -1, -1},
    };
    char turn = 'X'; //ó�� turn�� X�� ����

    int r, c;
    int i, j;
    int count;
    int result;
    bool gameRunning = true;

    count = 0;
    display(board);

    while (count < 9)
    {
        printf("Player %c(�� ��):", turn);
        scanf("%d %d", &r, &c);
        printf("\n");

        if (board[r][c] != -1) //�̹� ä���������� �ٽ� �Է� ������Ʈ ����
            continue;      //�ڵ� �����κ����� ���ư�

        count++;

        if (turn == 'X') {

            board[r][c] = 0;
            turn = 'O'; //���� �ٲ���
        }
        else {
            board[r][c] = 1;
            turn = 'X';
        }
        display(board);
        result = winCheck(board);
        if (result == -1)
            continue;
        else if (result == 0) {
            printf("Player X wins!\n");
            gameRunning = false;
            break;
        }
        else if (result == 1) {
            printf("Player O wins!\n");
            gameRunning = false;
            break;
        }
    } //count�� 9 �̸��̸� 3x3 �� �������� �� ä������ ���� ����
    if (gameRunning != false && count == 9) {
        printf("Nobody wins!");
    }
}