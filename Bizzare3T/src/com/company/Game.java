package com.company;

import java.util.Scanner;

public class Game {

    //create objects of outputs and Scanner
    static Output output = new Output();
    static Setting setting = new Setting();
    static Scanner in = new Scanner(System.in);

    //Array from setting, which player is setting
    static String[] game = setting.game_pieces();

    //Variables definitions
    static int player_checker = 1;
    static int piece = 1;
    static boolean choice_check = false;
    static String player1, player2;

    //setters
    public static void setPlayer1(String player1) {
        Game.player1 = player1;
    }
    public static void setPlayer2(String player2) {
        Game.player2 = player2;
    }

    public static void game() {
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

    public static void player1() {
        choice_check = false;

        while (choice_check == false) {
            //Ask player which cube want to choose
            System.out.println(player1 + ", where would You like place Your piece?\n");

            //player's choice
            piece = in.nextInt();

            //checker if cube where user want to place piece is free
            if ((game[piece - 1] != "X") || (game[piece - 1] != "O")) {
                //Add choice to the game's array
                game[piece - 1] = "X";
                choice_check = true;

                //checker if player've won
                if (win_checker() == true){
                    System.out.println(player1 +" have won!");
                    System.exit(0);
                }
            } else System.out.println("You cannot add piece here!");
        }
        //output game's board
        output.game_output(game);
    }

    public static void player2() {
        choice_check = false;

        while (choice_check == false) {
            //Ask player which cube want to choose
            System.out.println(player2 + ", where would You like place Your piece?\n");

            //player's choice
            piece = in.nextInt();

            //checker if cube where user want to place piece is free
            if ((game[piece - 1] != "X") || (game[piece - 1] != "O")) {
                //Add choice to the game's array
                game[piece - 1] = "O";
                choice_check = true;

                //checker if player've won
                if (win_checker() == true){
                    System.out.println(player2 +" have won!");
                    System.exit(0);
                }
            } else System.out.println("You cannot add piece here!");
        }
        //output game's board
        output.game_output(game);
    }


    //method to check if player win in his/her turn
    public static boolean win_checker() {
        if ((game[0] == game[1] && game[1] == game[2] && ((game[0] == "X" && game[1] == "X" && game[2] == "X") || (game[0] == "O" && game[1] == "O" && game[2] == "O"))) ||
                (game[3] == game[4] && game[4] == game[5] && ((game[3] == "X" && game[4] == "X" && game[5] == "X") || (game[3] == "O" && game[4] == "O" && game[5] == "O"))) ||
                (game[6] == game[7] && game[7] == game[8] && ((game[6] == "X" && game[7] == "X" && game[8] == "X") || (game[6] == "O" && game[7] == "O" && game[8] == "O"))) ||
                (game[0] == game[3] && game[3] == game[6] && ((game[0] == "X" && game[3] == "X" && game[6] == "X") || (game[0] == "O" && game[3] == "O" && game[6] == "O"))) ||
                (game[1] == game[4] && game[4] == game[7] && ((game[1] == "X" && game[4] == "X" && game[7] == "X") || (game[1] == "O" && game[4] == "O" && game[7] == "O"))) ||
                (game[2] == game[5] && game[5] == game[8] && ((game[2] == "X" && game[5] == "X" && game[8] == "X") || (game[2] == "O" && game[5] == "O" && game[8] == "O"))) ||
                (game[0] == game[4] && game[4] == game[8] && ((game[0] == "X" && game[4] == "X" && game[8] == "X") || (game[0] == "O" && game[4] == "O" && game[8] == "O"))) ||
                (game[2] == game[4] && game[4] == game[6] && ((game[2] == "X" && game[4] == "X" && game[6] == "X") || (game[2] == "O" && game[4] == "O" && game[6] == "O")))) {
            output.game_output(game);
            return true;
        }
        return false;
    }
}
