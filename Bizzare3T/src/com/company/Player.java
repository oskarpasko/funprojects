package com.company;

import java.util.Scanner;

public class Player {

    //variable for player's name
    static String name;
    //just scanner
    static Scanner in = new Scanner(System.in);

    //method which write from user his/her name
    public static String read_name(){
        name = in.nextLine();

        return name;
    }

}
