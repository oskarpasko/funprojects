package com.company;

import java.util.Scanner;

public class Setting {

    static Output output = new Output();
    static Scanner in = new Scanner(System.in);

    static public String[][] piece = {{"-", "-", "-", "-", "-", "-", "-", "-", "-"},
                                       {"1", "2", "3", "4", "5", "6", "7", "8", "9"},
                                       {" ", " ", " ", " ", " ", " ", " ", " ", " "},
                                       {"/", "/", "/", "/", "/", "/", "/", "/", "/"},
                                       {"T", "i", "c", "T", "a", "c", "T", "o", "e"}};

    static String pieces[] = {"-", "-", "-", "-", "-", "-", "-", "-", "-"};

    static public String[] game_pieces(){

        int chosed_patter = choose_pieces();

        for(int i = 0;i < 9;i++){
            pieces[i] = piece[chosed_patter - 1][i];
        }

        return pieces;
    }

    static public int choose_pieces(){
        //outputs welcome texts
        output.welcome();

        System.out.println("Which one pattern of pieces You would like to choose?");

        int i = 1;

        for(String[] pie: piece) {
            System.out.print(i+". ");
            for(String n: pie) {
                System.out.print(n + " ");
            }
            System.out.println();
            i++;
        }

        int choose = in.nextInt();

        return choose;
    }

}
