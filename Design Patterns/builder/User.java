public class User {
    private String name;
    private String password;
    private String city;
    private int age;
    private boolean isAdmin;


    private User(Builder builder) {;
        this.name = builder.name;
        this.password = builder.password;
        this.city = builder.city;
        this.age = builder.age;
        this.isAdmin = builder.isAdmin;
    }
    @Override
    public String toString() {
        return "User{" +
                "name='" + name + '\'' +
                ", password='" + password + '\'' +
                ", city='" + city + '\'' +
                ", age=" + age +
                ", isAdmin=" + isAdmin +
                '}';
    }
    public static class Builder {
        private String name;
        private String password;
        private String city;
        private int age;
        private boolean isAdmin;

        public Builder setName(String name) {
            this.name = name;
            return this;
        }

        public Builder setPassword(String password) {
            this.password = password;
            return this;
        }

        public Builder setCity(String city) {
            this.city = city;
            return this;
        }

        public Builder setAge(int age) {
            this.age = age;
            return this;
        }

        public Builder setAdmin(boolean admin) {
            isAdmin = admin;
            return this;
        }

        public User build() {
            return new User(this);
        }
    }
}
