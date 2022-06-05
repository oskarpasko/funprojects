package com.company;

import java.io.IOException;
import java.util.Scanner;

public class Main {

    static Output output = new Output();
    static Game game = new Game();
    static Player player = new Player();
    static Scanner in = new Scanner(System.in);

    //variable to work with player's choice
    //1. is starting game
    //2. exiting the game
    static int choice = 0;


    public static void main(String[] args) {



        output.menu();

        //while (choice != 1 or 2) => player can still choose action
        while((choice < 1) || (choice > 2)){
            choice = in.nextInt();

            switch(choice){
                case 1: //start game
                    System.out.println("Player 1 name: ");
                    game.setPlayer1(player.read_name());
                    System.out.println("Player 2 name: ");
                    game.setPlayer2(player.read_name());
                    game.game();
                    break;
                case 2: //exit game
                    System.exit(0);
                default:
                    System.out.println("Wrong choice!");
                    System.out.println("Choose once again.");
            }
        }
    }
}
