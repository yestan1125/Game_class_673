#include <iostream>
#include <algorithm> 
#include <cstdlib>
#include <ctime>

using namespace std;
// 用于打印棋盘的函数
void printBoard(int board[4][4]) {
    for (int i = 0; i < 4; ++i) {
        for (int j = 0; j < 4; ++j) {
            cout.width(4);//保证棋盘数字对齐
            cout << board[i][j] << " ";
        }
        cout << endl;
    }
}
// 初始化棋盘，所有位置设为0
void initBoard(int board[4][4]) {
    for (int i = 0; i < 4;++i) {
        for (int j = 0; j < 4; ++j) {
            board[i][j] = 0;
        }
    }
}
// 在棋盘上随机位置添加一个2或4
void random(int board[4][4]) {
    bool placed = false;
    while (!placed) {
        int x = rand() % 4;
        int y = rand() % 4;
        if (board[x][y] == 0) {
            board[x][y] = (rand() % 2) ? 2 : 4;
            placed = true;
        }
    }
}
// 检查游戏是否胜利（是否有2048的数字）
bool hasWon(int board[4][4]) {
    for (int i = 0; i < 4; ++i) {
        for (int j = 0; j < 4; ++j) {
            if (board[i][j] == 2048) {
                return true;
            }
        }
    }
    return false;
}
// 检查游戏是否结束（没有可移动的数字）
bool canMove(int board[4][4]) {
    for (int i = 0; i < 4; ++i) {
        for (int j = 0; j < 4 - 1; ++j) {
            if (board[i][j] == 0 || board[i][j + 1] == 0 || board[i][j] == board[i][j + 1]) {
                return true;
            }
        }
    }
    for (int j = 0; j < 4; ++j) {
        for (int i = 0; i < 3; ++i) {
            if (board[i][j] == 0 || board[i + 1][j] == 0 || board[i][j] == board[i + 1][j]) {
                return true;
            }
        }
    }
    return false;
}
// 压缩棋盘上的数字，将所有非零数字移动到一起
void compress(int board[4][4]) {
    for (int i = 0; i < 4; ++i) {   //开始一个循环，从第0行到第3行（共4行），每次循环处理数组的一行
        int k = 0;//在每次处理新行时，初始化一个计数器k，它将用来跟踪非零元素在压缩后的位置
        for (int j = 0; j < 4; ++j) {  //对于当前行，开始一个循环，从第0列到第3列（共4列），每次循环处理数组的一个元素
            if (board[i][j] != 0) {  //检查当前元素是否非零
                board[i][k++] = board[i][j];//如果当前元素非零，将其复制到当前行的k位置，并将k增加1，以便下一次复制时k指向下一个位置
            }
        }
        while (k < 4) {  // 检查是否还有空位需要填充零（即k是否小于4）
            board[i][k++] = 0;//如果k小于4，将当前行的k位置设置为0，并增加k
        }
    }
}
// 合并棋盘上的相同数字
void merge(int board[4][4]) {
    for (int i = 0; i < 4; ++i) {
        for (int j = 0; j < 3; ++j) {
            if (board[i][j] == board[i][j + 1] && board[i][j] != 0) {
                board[i][j] *= 2;
                board[i][j + 1] = 0;
            }
        }
    }
}
// 向左移动棋盘上的数字
void moveLeft(int board[4][4]) {
    compress(board);
    merge(board);
    compress(board);
}
// 向右移动棋盘上的数字
void moveRight(int board[4][4]) {
    for (int i = 0; i < 4; ++i) {
        reverse(board[i], board[i] + 4);//运用了reverse，实现行逆转
    }
    moveLeft(board);
    for (int i = 0; i < 4; ++i) {
        reverse(board[i], board[i] + 4);
    }
}
// 向上移动棋盘上的数字
void moveUp(int board[4][4]) {
    int tempBoard[4][4];
    for (int i = 0; i < 4; ++i) {
        for (int j = 0; j < 4; ++j) {
            tempBoard[j][i] = board[i][j];//先求矩阵的转置
        }
    }
    moveLeft(tempBoard);//对转置矩阵进行左移
    for (int i = 0; i < 4; ++i) {
        for (int j = 0; j < 4; ++j) {
            board[i][j] = tempBoard[j][i];//在转置一次，实现一次上移
        }
    }
}
// 向下移动棋盘上的数字
void moveDown(int board[4][4]) {
    int tempBoard[4][4];
    for (int i = 0; i < 4; ++i) {
        for (int j = 0; j < 4; ++j) {
            tempBoard[3 - j][3 - i] = board[i][j];//与转置类似，只是方向不同
        }
    }
    moveLeft(tempBoard);
    for (int i = 0; i < 4; ++i) {
        for (int j = 0; j < 4; ++j) {
            board[i][j] = tempBoard[3 - j][3 - i];//逆转回来，实现一次下移
        }
    }
}
// 主函数，游戏的入口点
int main() {
    srand(static_cast<unsigned int>(time(0))); // 初始化随机数生成器
    int board[4][4]; // 创建棋盘
    initBoard(board); // 初始化棋盘
    random(board); // 添加初始数字
    random(board); // 添加第二个初始数字
    char move; // 用户的移动指令
    bool gameover = false; // 游戏结束标志
    while (!gameover) { // 游戏主循环
        printBoard(board); // 打印棋盘
        cout << "Enter move (w/a/s/d): ";
        cin >> move;
        switch (move) {
        case 'w':
            moveUp(board);
            random(board);// 添加新数字，在每个正确情况后单独添加，避免错误输入也会生成新数字
            break;
        case 's':
            moveDown(board); 
            random(board);
            break;
        case 'a':
            moveLeft(board);
            random(board);
            break;
        case 'd':
            moveRight(board);
            random(board);
            break;
        default: cout << "Invalid move. Please enter w, a, s, or d." << endl; break;
        }
        if (hasWon(board)) { // 检查是否胜利
            cout << "Congratulations, you've won!" << endl;
            gameover = true;
        }
        else if (!canMove(board)) { // 检查游戏是否结束
            cout << "Game Over!" << endl;
            gameover = true;
        }
    }
    return 0;
}
