package com.company;

import java.util.Scanner;

public class Setting {

    //devs objects
    static Output output = new Output();
    static Scanner in = new Scanner(System.in);


    //pieces to choose in menu
    static public String[][] piece = {{"-", "-", "-", "-", "-", "-", "-", "-", "-"},
                                       {"1", "2", "3", "4", "5", "6", "7", "8", "9"},
                                       {" ", " ", " ", " ", " ", " ", " ", " ", " "},
                                       {"/", "/", "/", "/", "/", "/", "/", "/", "/"},
                                       {"T", "i", "c", "T", "a", "c", "T", "o", "e"}};

    //default tab with pices
    static String pieces[] = {"-", "-", "-", "-", "-", "-", "-", "-", "-"};


    //method which set chose pieces
    static public String[] game_pieces(){

        int chosed_patter = choose_pieces();

        for(int i = 0;i < 9;i++){
            pieces[i] = piece[chosed_patter - 1][i];
        }

        return pieces;
    }


    //method which write from user which pieces he/she have chose
    static public int choose_pieces(){
        //outputs welcome texts from Output class
        output.welcome();

        System.out.println("Which one pattern of pieces You would like to choose?");

        //helping var
        int i = 1;

        //loop which writes pieces to choose
        for(String[] pie: piece) {
            System.out.print(i+". ");
            for(String n: pie) {
                System.out.print(n + " ");
            }
            System.out.println();
            i++;
        }

        //user choice
        int choose = in.nextInt();

        return choose;
    }

}
