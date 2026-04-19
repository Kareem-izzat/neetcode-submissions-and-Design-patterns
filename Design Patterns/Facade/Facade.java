public class DVDPlayer{
    public void on() {
        System.out.println("DVD Player ON");
    }

    public void play(String movie) {
        System.out.println("Playing movie: " + movie);
    }

    public void off() {
        System.out.println("DVD Player OFF");
    }
}
class Projector {
    public void on() {
        System.out.println("Projector ON");
    }

    public void setInput(String input) {
        System.out.println("Projector input set to " + input);
    }

    public void off() {
        System.out.println("Projector OFF");
    }
}
class SoundSystem {
    public void on() {
        System.out.println("Sound System ON");
    }

    public void setVolume(int level) {
        System.out.println("Volume set to " + level);
    }

    public void off() {
        System.out.println("Sound System OFF");
    }
}

class Lights {
    public void dim() {
        System.out.println("Lights dimmed");
    }

    public void on() {
        System.out.println("Lights ON");
    }
}

class HomeTheaterFacade{
    private DVDPlayer dvd;
    private Projector projector;
    private SoundSystem sound;
    private Lights lights;

    public HomeTheaterFacade() {
        this.dvd = new DVDPlayer();
        this.projector = new Projector();
        this.sound = new SoundSystem();
        this.lights = new Lights();
    }
    public void watchMovie(String movie) {
        System.out.println("\n=== Starting Movie ===");
        lights.dim();
        projector.on();
        projector.setInput("DVD");
        sound.on();
        sound.setVolume(10);
        dvd.on();
        dvd.play(movie);
    }
    public void endMovie() {
        System.out.println("\n=== Ending Movie ===");
        dvd.off();
        sound.off();
        projector.off();
        lights.on();
    }
}
class Main2 {
    public static void main(String[] args) {

        HomeTheaterFacade theater = new HomeTheaterFacade();

        // User only interacts with the facade
        theater.watchMovie("Inception");

        // Simulate time passing...
        System.out.println("\n...Watching movie...\n");

        theater.endMovie();
    }
}