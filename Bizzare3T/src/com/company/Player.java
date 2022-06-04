package com.company;

import java.util.Scanner;

public class Player {

    static String name;
    static Scanner in = new Scanner(System.in);

    public static String read_name(){
        name = in.nextLine();

        return name;
    }

}
