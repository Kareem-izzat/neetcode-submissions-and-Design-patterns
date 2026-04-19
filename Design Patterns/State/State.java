interface State {
    void insertMoney(VendingMachine vm);
    void selectItem(VendingMachine vm);
}
class VendingMachine{
    private State state;
    public VendingMachine(){
        this.state = new NoMoneyState();
    }
    public void setState(State state){
        this.state = state;
    }
    public void insertMoney(){
        state.insertMoney(this);
    }
    public void selectItem() {
        state.selectItem(this);
    }

}
class NoMoneyState implements State {
    @Override
    public void insertMoney(VendingMachine vm) {
        System.out.println("Money inserted.");
        vm.setState(new HasMoneyState());
    }
    @Override
    public void selectItem(VendingMachine vm) {
        System.out.println("Please insert money first.");
    }
}
class HasMoneyState implements State {
    @Override
    public void insertMoney(VendingMachine vm) {
        System.out.println("Money already inserted.");
    }
    @Override
    public void selectItem(VendingMachine vm) {
        System.out.println("Item dispensed. Thank you!");
        vm.setState(new NoMoneyState());
    }
}
class Main5 {
    public static void main(String[] args) {
        VendingMachine vm = new VendingMachine();
        vm.selectItem();
        vm.insertMoney();
        vm.insertMoney();
        vm.selectItem();
        vm.selectItem();
    }
}