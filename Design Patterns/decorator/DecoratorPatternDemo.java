public class DecoratorPatternDemo {
    interface Coffee{
        String getDescription();
        double getCost();
    }
    static class SimpleCoffee implements Coffee{
        @Override
        public String getDescription() {
            return "Simple Coffee";
        }

        @Override
        public double getCost() {
            return 2.0;
        }
    }
    static abstract class CoffeeDecorator implements Coffee{
        protected Coffee coffee;
        public CoffeeDecorator(Coffee coffee) {
            this.coffee = coffee;
        }
        @Override
        public String getDescription() {
            return coffee.getDescription();
        }
        @Override
        public double getCost() {
            return coffee.getCost();
        }
    }
    static class MilkDecorator extends CoffeeDecorator{
        public MilkDecorator(Coffee coffee) {
            super(coffee);
        }
        @Override
        public String getDescription() {
            return super.getDescription() + ", Milk";
        }
        @Override
        public double getCost() {
            return super.getCost() + 0.5;
        }
    }
    static class SugarDecorator extends CoffeeDecorator{
        public SugarDecorator(Coffee coffee) {
            super(coffee);
        }
        @Override
        public String getDescription() {
            return super.getDescription() + ", Sugar";

        }
        @Override
        public double getCost() {
            return super.getCost() + 0.2;
        }
        }
    static class WhippedCreamDecorator extends CoffeeDecorator {
        public WhippedCreamDecorator(Coffee coffee) {
            super(coffee);
        }

        @Override
        public String getDescription() {
            return coffee.getDescription() + ", Whipped Cream";
        }

        @Override
        public double getCost() {
            return coffee.getCost() + 3.0;
        }
    }
    public static void main(String[] args) {
        Coffee coffee = new SimpleCoffee();
        coffee = new MilkDecorator(coffee);
        coffee = new SugarDecorator(coffee);
        coffee = new WhippedCreamDecorator(coffee);
        System.out.println("Order: " + coffee.getDescription());
        System.out.println("Total cost: $" + coffee.getCost());

    }
}
