public class VideoGame {
    // Fields to store video game information
    private String title;
    private String genre;
    private int releaseYear;
    private double price;

    // Constructor to initialize the VideoGame object
    public VideoGame(String title, String genre, int releaseYear, double price) {
        // Using setter methods to ensure proper formatting and validation
        setTitle(title);
        setGenre(genre);
        setReleaseYear(releaseYear);
        setPrice(price);
    }

    // Getter method for the title
    public String getTitle() {
        return title;
    }

    // Setter method for the title
    public void setTitle(String title) {
        this.title = title;
    }

    // Getter method for the genre
    public String getGenre() {
        return genre;
    }

    // Setter method for the genre
    public void setGenre(String genre) {
        this.genre = genre;
    }

    // Getter method for the release year
    public int getReleaseYear() {
        return releaseYear;
    }

    // Setter method for the release year with validation
    public void setReleaseYear(int releaseYear) {
        if (releaseYear >= 0) {
            this.releaseYear = releaseYear;
        } else {
            // Throw an exception for negative release years
            throw new IllegalArgumentException("Release year cannot be negative.");
        }
    }

    // Getter method for the price
    public double getPrice() {
        return price;
    }

    // Setter method for the price with validation
    public void setPrice(double price) {
        if (price >= 0) {
            this.price = price;
        } else {
            // Throw an exception for negative prices
            throw new IllegalArgumentException("Price cannot be negative.");
        }
    }

    // String representation of the VideoGame object
    public String toString() {
        // Create a formatted string with video game information
        return "Title: " + title + "\nGenre: " + genre + "\nRelease Year: " + releaseYear;
    }
}
