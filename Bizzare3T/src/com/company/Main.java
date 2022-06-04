package com.company;

import java.util.Scanner;

public class Main {

    static Output output = new Output();
    static Game game = new Game();

    public static void main(String[] args) {

        //outputs welcome texts
        output.welcome();

        game.game();
    }
}
