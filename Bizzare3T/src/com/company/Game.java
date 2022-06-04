package com.company;

import java.util.Scanner;

public class Game {

    //create objects of outputs and Scanner
    static Output output = new Output();
    static Scanner in = new Scanner(System.in);

    //Array which is sending to game_output()
    static String[] game = {"-", "-", "-",
            "-", "-", "-",
            "-", "-", "-"};

    //Variables definitions
    static int player_checker = 1;
    static int piece = 1;

    public static void game(){
        //Outputs default board
        output.game_output(game);

        //Main game's loop
            while (player_checker < 10) {
            if (player_checker % 2 != 0) {

                player1(); //function for player1

            } else {

                player2(); //function for player 2

            }

            player_checker++;
        }
    }

    public static void player1(){
        //Ask player which cube want to choose
        System.out.println("Player 1, where would You like place Your piece?\n");

        //player's choise
        piece = in.nextInt();

        //Add choice to the game's array
        game[piece - 1] = "X";

        //output game's board
        output.game_output(game);
    }

    public static void player2(){
        //Ask player which cube want to choose
        System.out.println("Player 2, where would You like place Your piece?\n");
        //player's choise
        piece = in.nextInt();

        //Add choice to the game's array
        game[piece - 1] = "O";

        //output game's board
        output.game_output(game);
    }
}
