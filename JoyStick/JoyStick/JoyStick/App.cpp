#include <iostream>
#include <stdio.h>
#include <conio.h>
#include <cstdlib>
#include <ctime>

#include "JoyStick.h"

using namespace std;

// funkcja wypisuj¹ca ca³¹ tablice
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
	cout << endl;
}

// funkcja losuj¹ca liczbê z przedzia³o [0, 10]
int randomNumber()
{
	return rand() % 10;
}

void game()
{

}

void welcome()
{
	cout << "Witamy w symulatorze JoySticka."
		"Twoim zadaniem jest dojsc do wykrzyknika na planszy."
		" JoyStickiem poruszasz sie za pomoca przyciskow W (gora), A (lewo), S (dol), D (prawo)."
		" Jesli chcesz zaczac wcisnij przycisk '1'. Powodzenia!" << endl;
}

int main()
{
	welcome();

	while (true)
	{
		int check;
		cin >> check;
		if (check == 1) break;
	}

	system("CLS");

	srand(time(NULL));

	// konstruktor naszego joystick
	// przypisanie losowych koordynatów X oraz Y
	JoyStick* js = new JoyStick(randomNumber(), randomNumber());

	// zmienna z surow¹ tablic¹
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

	// ustawienie w wylosowanych koordynatach joysticka
	js->setBoard(arr);

	// pêtla poruszaj¹ca siê po planszy
	while (true)
	{
		// wypisanie planszy
		arrayOutput(arr);

		// pobranie od u¿ytkownika wciœniêtego klawisza
		char choice = _getch();

		switch (choice)
		{
		case 'w': // poruszeniesiê w górê planszy
			js->getCords(arr);
			js->moveUp(arr);
			break;
		case 'd': // poruszenie siê w praw¹ stronê planszy
			js->getCords(arr);
			js->moveRight(arr);
			break;
		case 's': // poruszenie siê w dó³ planszy
			js->getCords(arr);
			js->moveDown(arr);
			break;
		case 'a': // poruszenie siê w lew¹ stronê planszy
			js->getCords(arr);
			js->moveLeft(arr);
			break;
		case 'q':
			// wywo³anie destruktora
			delete js;
			exit(0);
		}
		system("CLS");
	}
}
