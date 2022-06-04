package com.company;

public class Main {

    static void game_output(String array []){
        System.out.println(" " + array[0] + " " + " | " + " " + array[1] + " " + " | " + " " + array[2]);
        System.out.println("----|-----|----");
        System.out.println(" " + array[3] + " " + " | " + " " + array[4] + " " + " | " + " " + array[5]);
        System.out.println("----|-----|----");
        System.out.println(" " + array[6] + " " + " | " + " " + array[7] + " " + " | " + " " + array[8]);
    }

    public static void main(String[] args) {


        System.out.println("Welcome in Bizzare3T!");
        System.out.println("");
        System.out.println("This is our schema.");

        System.out.println(" 1 " + " | " + " 2 " + " | " + " 3 ");
        System.out.println("----|-----|----");
        System.out.println(" 4 " + " | " + " 5 " + " | " + " 6 ");
        System.out.println("----|-----|----");
        System.out.println(" 7 " + " | " + " 8 " + " | " + " 9 ");
        System.out.println("\n");

        boolean endgame = false;
        //String[][] game = new String[3][3];

        String[][] test = {{"X", "X", "X"}, {"O", "X", "O"}, {"X", "O", "O"}};

        String[] game_work = {test[0][0], test[0][1], test[0][2],
                          test[1][0], test[1][1], test[1][2],
                          test[2][0], test[2][1], test[2][2]};

        game_output(game_work);


    }
}
