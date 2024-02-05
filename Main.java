import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // Create a list of video games
        List<VideoGame> videoGames = new ArrayList<>();

        // Prompt the user to input video game information
        Scanner scanner = new Scanner(System.in);

        for (int i = 1; i <= 3; i++) {
            System.out.println("Enter details for Video Game " + i + ":");
            System.out.print("Title: ");
            String title = scanner.nextLine();
            System.out.print("Genre: ");
            String genre = scanner.nextLine();
            System.out.print("Release Year: ");
            int releaseYear = scanner.nextInt();
            System.out.print("Price: $");
            double price = scanner.nextDouble();
            scanner.nextLine(); // Consume the newline character

            VideoGame game = new VideoGame(title, genre, releaseYear, price);
            videoGames.add(game);
        }

        // Print the information of each VideoGame object
        for (VideoGame game : videoGames) {
            System.out.println("\nVideo Game Information:\n" + game.toString());
        }

        // Create a shopping cart
        ShoppingCart shoppingCart = new ShoppingCart();

        // Add video games to the shopping cart
        for (VideoGame game : videoGames) {
            shoppingCart.addToCart(game);
        }

        // Calculate and print the total value of items in the shopping cart
        System.out.println("\nTotal Value of Items in the Shopping Cart: $" + shoppingCart.calculateTotalValue());

        // Print names, genres, release years, and prices of items in the shopping cart
        System.out.println("\nDetails of Items in the Shopping Cart:");
        List<VideoGame> cartItems = shoppingCart.getCartItems();
        for (VideoGame game : cartItems) {
            System.out.println(game.toString() + "\nPrice: $" + game.getPrice() + "\n");
        }
    }
}