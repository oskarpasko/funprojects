#include <iostream>
using namespace std;


class JoyStick
{
private:
	 int x = 0;
	 int y = 0;

public:

	void setBoard(string board[][10])
	{
		board[x][y] = "+";
	}

	void getCords(string board[][10])
	{
		int i, j;
		for (i = 0; i < 10; i++)
		{
			for (j = 0; j < 10; j++)
			{
				if (board[i][j] == "+")
				{
					x = i;
					y = j;
				}
			}
			cout << endl;
		}
	}

	void moveRight(string board[][10])
	{
		if (board[x][y + 1] == "!")
		{
			cout << "Dotarles do celu! Gratulacje!" << endl;
			exit(0);
		}

		if (y+1 < 10) 
		{
			board[x][y] = "-";
			board[x][y + 1] = "+";
		}
	}

	void moveLeft(string board[][10])
	{
		if (board[x][y - 1] == "!")
		{
			cout << "Dotarles do celu! Gratulacje!" << endl;
			exit(0);
		}

		if (y - 1 >= 0)
		{
			board[x][y] = "-";
			board[x][y - 1] = "+";
		}
	}

	void moveDown(string board[][10])
	{
		if (board[x + 1][y] == "!")
		{
			cout << "Dotarles do celu! Gratulacje!" << endl;
			exit(0);
		}

		if (x + 1 < 10)
		{
			board[x][y] = "-";
			board[x + 1][y] = "+";
		}
	}

	void moveUp(string board[][10])
	{
		if (board[x-1][y] == "!")
		{
			cout << "Dotarles do celu! Gratulacje!" << endl;
			exit(0);
		}

		if (x - 1 >= 0)
		{
			board[x][y] = "-";
			board[x - 1][y] = "+";
		}
	}
};

