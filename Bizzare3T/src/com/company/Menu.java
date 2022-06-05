package com.company;

import java.util.Scanner;

public class Menu {

    //object defs
    static Scanner in = new Scanner(System.in);
    static Game game = new Game();
    static Player player = new Player();
    static Output output = new Output();

    //variable to work with player's choice
    //1. is starting game
    //2. exiting the game
    static int choice = 0;

    static public void main_menu(){

        //Write things for menu choosing
        output.menu();

        //while (choice != 1 or 2) => player can still choose action
            while((choice < 1) || (choice > 2)){
                choice = in.nextInt();

                //switch case of user choices
                switch(choice){
                    case 1: //start game
                        //entering 1st player's name
                        System.out.println("Player 1 name: ");
                        //setting 1st player's name
                        game.setPlayer1(player.read_name());
                        //entering 2nd player's name
                        System.out.println("Player 2 name: ");
                        //setting 2nd player's name
                        game.setPlayer2(player.read_name());

                        //starting Game.game() method
                        game.game();
                        break;
                    case 2:
                        //entering 1st player's name
                        System.out.println("Player 1 name: ");
                        //setting 1st player's name
                        game.setPlayer1(player.read_name());


                        //starting game with ai
                        game.game_with_ai();
                    case 3: //exit game
                        System.exit(0);
                    default:
                        System.out.println("Wrong choice!");
                        System.out.println("Choose once again.");
                }
            }
    }
}
