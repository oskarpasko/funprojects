#include <iostream>
#include <stdio.h>
#include <conio.h>
#include "JoyStick.h"

using namespace std;

void arrayOutput(string array[][10])
{
	int i, j;
	for (i = 0; i < 10; i++)
	{
		for (j = 0; j < 10; j++)
		{
			cout << " " << array[i][j];
		}
		cout << endl;
	}
}

int main()
{
    string arr[10][10] = {
        {"-", "-", "-", "-", "-", "-", "-", "-", "-", "-"},
		{"-", "-", "-", "-", "-", "-", "-", "-", "-", "-"},
		{"-", "-", "-", "-", "-", "-", "-", "-", "-", "-"},
		{"-", "-", "-", "-", "-", "-", "-", "-", "-", "-"},
		{"-", "-", "-", "-", "-", "-", "-", "-", "-", "-"},
		{"-", "-", "-", "-", "-", "-", "-", "-", "-", "-"},
		{"-", "-", "-", "-", "-", "-", "-", "-", "-", "-"},
		{"-", "-", "-", "-", "-", "-", "-", "-", "-", "-"},
		{"-", "-", "-", "-", "-", "-", "-", "-", "-", "-"},
		{"-", "-", "-", "-", "-", "-", "-", "-", "-", "!"},
            };

	JoyStick js;

	js.setBoard(arr);

	while (true)
	{
		arrayOutput(arr);

		char choice = _getch();

		switch (choice)
		{
		case 'w':
			js.getCords(arr);
			js.moveUp(arr);
			break;
		case 'd':
			js.getCords(arr);
			js.moveRight(arr);
			break;
		case 's':
			js.getCords(arr);
			js.moveDown(arr);
			break;
		case 'a':
			js.getCords(arr);
			js.moveLeft(arr);
			break;
		case 'q':
			exit(0);
		}
	}
}
