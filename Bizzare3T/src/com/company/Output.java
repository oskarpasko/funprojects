package com.company;

public class Output {


    //function to write TicTacToe's board
    public static void game_output(String array[]) {
        System.out.println("  " + array[0] + " " + " | " + " " + array[1] + " " + " | " + " " + array[2]);
        System.out.println("-----|-----|-----");
        System.out.println("  " + array[3] + " " + " | " + " " + array[4] + " " + " | " + " " + array[5]);
        System.out.println("-----|-----|-----");
        System.out.println("  " + array[6] + " " + " | " + " " + array[7] + " " + " | " + " " + array[8]);
    }

    //output for welcome players
    public static void welcome() {
        //Welcome player / players.
        System.out.println("Welcome in Bizzare3T!");
        System.out.println("");
        System.out.println("This is our schema.");

        //Write schema for the game.
        System.out.println("  1 " + " | " + " 2 " + " | " + " 3 ");
        System.out.println("-----|-----|-----");
        System.out.println("  4 " + " | " + " 5 " + " | " + " 6 ");
        System.out.println("-----|-----|-----");
        System.out.println("  7 " + " | " + " 8 " + " | " + " 9 ");
        System.out.println("\n");
    }

    //output for choose menu in main_menu
    public static void menu(){
        System.out.println("Choose action");
        System.out.println("1. Player vs Player");
        System.out.println("2. Player vs AI");
        System.out.println("3. Exit");
    }
}
