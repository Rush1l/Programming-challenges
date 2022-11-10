public class Lesson2 {
    public static void main(String[] args) {
        for_loop_yes();
        Print_cars();
    }

    public static void for_loop_yes() {
        for (int i = 0; i < 5; i++) {
            System.out.println("Yes");
        }
    }
    public static void Print_cars() {
        String[] cars = {"Volvo", "BMW", "Ford", "Mazda"};
        for (int i = 0; i < cars.length; i++) {
            System.out.println(cars[i]);
        }
    }
    public static void Get_day() {
        int day = 4;

    }


}
