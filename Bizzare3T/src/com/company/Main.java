package com.company;

public class Main {

    static Output output = new Output();
    static Game game = new Game();
    static Player player = new Player();

    public static void main(String[] args){

        //outputs welcome texts
        output.welcome();

        System.out.println("Player 1 name: ");
        game.setPlayer1(player.read_name());
        System.out.println("Player 2 name: ");
        game.setPlayer2(player.read_name());

        game.game();
    }
}
