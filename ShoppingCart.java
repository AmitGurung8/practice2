import java.util.ArrayList;
import java.util.List;

class ShoppingCart {
    // List to store VideoGame objects in the shopping cart
    private List<VideoGame> cartItems;

    // Constructor to initialize the shopping cart
    public ShoppingCart() {
        cartItems = new ArrayList<>();
    }

    // Method to add a VideoGame object to the shopping cart
    public void addToCart(VideoGame game) {
        cartItems.add(game);
    }

    // Method to calculate the total value of items in the shopping cart
    public double calculateTotalValue() {
        double totalValue = 0.0d;
        for (VideoGame game : cartItems) {
            totalValue += game.getPrice();
        }
        return totalValue;
    }

    // Getter method for cart items
    public List<VideoGame> getCartItems() {
        return cartItems;
    }
}
