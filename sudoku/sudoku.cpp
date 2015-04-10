#include <vector>
#include <iostream>

const int dim = 9;

class Point {
    private:
    	int x, y;
    public:
    	Point();
        Point(int x, int y) {this->x = x; this->y = y;}
};

class Solution {
    private:
        std::vector<std::vector<char> > m;
        std::vector<Point> moves;
        int freecount;
    public:
        void solveSudoku(std::vector<std::vector<char> > &board);
        bool backtrack();
};

void Solution::solveSudoku(std::vector<std::vector<char> > &board) {
	this->m = board;
}

int main() {
    char input_board[dim][dim] = {
        {'5', '3', '-', '-', '7', '-', '-', '-', '-'},
        {'6', '-', '-', '1', '9', '5', '-', '-', '-'},
        {'-', '9', '8', '-', '-', '-', '-', '6', '-'},
        {'8', '-', '-', '-', '6', '-', '-', '-', '3'},
        {'4', '-', '-', '8', '-', '3', '-', '-', '1'},
        {'7', '-', '-', '-', '2', '-', '-', '-', '6'},
        {'-', '6', '-', '-', '-', '-', '2', '8', '-'},
        {'-', '-', '-', '4', '1', '9', '-', '-', '5'},
        {'-', '-', '-', '-', '8', '-', '-', '7', '9'},
    };
    std::vector<std::vector<char> > b (dim);
    for (int i = 0; i < dim; i++) {
        b[i].assign(input_board[i], input_board[i]+dim);
    }
    Solution s;
    s.solveSudoku(b);
    return 0;
}
