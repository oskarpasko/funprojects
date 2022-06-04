package com.company;

import java.util.Scanner;

public class Main {

    static Output output = new Output();

    public static void main(String[] args) {

        //outputs welcome texts
        output.welcome();

        //Array which is sending to game_output()
        String[] game = {"-", "-", "-",
                "-", "-", "-",
                "-", "-", "-"};

        //Outputs default board
        output.game_output(game);


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
                output.game_output(game);
            } else {
                //Ask player which cube want to choose
                System.out.println("Player 2, where would You like place Your piece?\n");
                //player's choise
                piece = in.nextInt();

                //Add choice to the game's array
                game[piece - 1] = "O";

                //output game's board
                output.game_output(game);
            }

            player_checker++;
        }


    }
}
