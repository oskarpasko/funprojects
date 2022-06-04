package com.company;

import java.util.Scanner;

public class Main {


    //function to write TicTacToe's board
    static void game_output(String array[]) {
        System.out.println(" " + array[0] + " " + " | " + " " + array[1] + " " + " | " + " " + array[2]);
        System.out.println("----|-----|----");
        System.out.println(" " + array[3] + " " + " | " + " " + array[4] + " " + " | " + " " + array[5]);
        System.out.println("----|-----|----");
        System.out.println(" " + array[6] + " " + " | " + " " + array[7] + " " + " | " + " " + array[8]);
    }

    public static void main(String[] args) {

        //Welcome player / players.
        System.out.println("Welcome in Bizzare3T!");
        System.out.println("");
        System.out.println("This is our schema.");

        //Write schema for the game.
        System.out.println(" 1 " + " | " + " 2 " + " | " + " 3 ");
        System.out.println("----|-----|----");
        System.out.println(" 4 " + " | " + " 5 " + " | " + " 6 ");
        System.out.println("----|-----|----");
        System.out.println(" 7 " + " | " + " 8 " + " | " + " 9 ");
        System.out.println("\n");

        //Array which is sending to game_output()
        String[] game = {"-", "-", "-",
                "-", "-", "-",
                "-", "-", "-"};

        game_output(game);

        int player_checker = 1;
        int piece = 1;
        Scanner in = new Scanner(System.in);


        //Main game's loop
        while (player_checker < 10) {
            if (player_checker % 2 != 0) {
                //Ask player which cube want to choose
                System.out.println("Player 1, where would You like place Your piece?\n");
                //player's choise
                piece = in.nextInt();

                //Add choice to the game's array
                game[piece - 1] = "X";

                //output game's board
                game_output(game);
            } else {
                //Ask player which cube want to choose
                System.out.println("Player 2, where would You like place Your piece?\n");
                //player's choise
                piece = in.nextInt();

                //Add choice to the game's array
                game[piece - 1] = "O";

                //output game's board
                game_output(game);
            }

            player_checker++;
        }


    }
}
