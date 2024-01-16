#include <iostream>
using namespace std;

class Device
{
protected:
	// sk�adowe z koordynatami joysticka
	int x;
	int y;

	// sk�adowa z wielko�ci� planszy jak� obs�uguje joystick
	string goodBye = "Dziekujemy za skorzystanie z naszego programu!" ;
};

class JoyStick : Device
{
public:
	/*
	
	W aplikacji u�ywany jest konstruktor z parametrami,
	dlatego pozosta�e konstruktory s� zakomentowane
	
	*/

	//konstruktor domy�lny
	/*JoyStick()
	{
		this->x = 0;
		this->y = 0;
	}*/

	// konstruktor z parametrami
	JoyStick(int xx, int yy)
	{
		this->x = xx;
		this->y = yy;
	}

	//konstruktor kopiuj�cy
	/*JoyStick(JoyStick& copyx, JoyStick& copyy, JoyStick& copys)
	{
		this->x = copyx.x;
		this->y = copyy.y;
	}*/

	// destruktor
	~JoyStick()
	{
		cout << this->goodBye;
	}

	// metoda ustawiaj�ca nasz joystick na wybranych koordynatach
	void setBoard(string board[][10])
	{
		board[x][y] = "+";
	}

	// metoda pobieraj�ca nasz� aktualn� pozycj�
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
		}
	}

	//metody poruszaj�ce si� odpowiednio:
	// w prawo
	// w lewo
	// w d�
	// w g�r�
	void moveRight(string board[][10])
	{
		if (board[x][y + 1] == "!")
		{
			board[x][y] = "-";
			board[x][y + 1] = "+";
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
			board[x][y] = "-";
			board[x][y - 1] = "+";
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
			board[x][y] = "-";
			board[x + 1][y] = "+";
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
			board[x][y] = "-";
			board[x - 1][y] = "+";
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

