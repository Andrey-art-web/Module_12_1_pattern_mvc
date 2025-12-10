# ========== Model ==========
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Pizza(Product):
    def __init__(self, name, price, dough, sauce, toppings):
        super().__init__(name, price)
        self.dough = dough
        self.sauce = sauce
        self.toppings = toppings

    def get_info(self):
        return (f"Пицца: {self.name}\n"
                f"Цена: {self.price}\n"
                f"Тесто: {self.dough}\n"
                f"Соус: {self.sauce}\n"
                f"Топпинги: {', '.join(self.toppings)}")


class PizzaFromMenu(Pizza):
    def __init__(self, name, price, dough, sauce, toppings, category):
        super().__init__(name, price, dough, sauce, toppings)
        self.category = category  # например, "классическая", "острая"


class OwnPizza(Pizza):
    def __init__(self, name, price, dough, sauce, toppings, customer_name):
        super().__init__(name, price, dough, sauce, toppings)
        self.customer_name = customer_name


# ========== Controller ==========
class PizzaController:
    def __init__(self):
        self.menu_pizzas = []
        self.custom_pizzas = []

    def add_menu_pizza(self, pizza):
        self.menu_pizzas.append(pizza)

    def add_custom_pizza(self, pizza):
        self.custom_pizzas.append(pizza)

    def get_menu_pizzas(self):
        return self.menu_pizzas

    def get_custom_pizzas(self):
        return self.custom_pizzas

    def get_total_price(self):
        total = sum(p.price for p in self.menu_pizzas + self.custom_pizzas)
        return total


# ========== View ==========
class PizzaView:
    @staticmethod
    def show_pizza_list(pizzas, title):
        print(f"\n=== {title} ===")
        for pizza in pizzas:
            print(pizza.get_info())
            print("-" * 30)

    @staticmethod
    def show_total(total):
        print(f"\nОбщая стоимость заказа: {total} руб.")


# ========== Usage ==========
if __name__ == "__main__":
    # 1. Создаем модели
    margherita = PizzaFromMenu(
        name="Маргарита",
        price=500,
        dough="тонкое",
        sauce="томатный",
        toppings=["сыр Моцарелла", "базилик"],
        category="классическая"
    )

    pepperoni = PizzaFromMenu(
        name="Пепперони",
        price=600,
        dough="толстое",
        sauce="острый томатный",
        toppings=["пепперони", "сыр"],
        category="острая"
    )

    my_pizza = OwnPizza(
        name="Моя особенная",
        price=700,
        dough="сырный борт",
        sauce="сливочный",
        toppings=["грибы", "курица", "перец"],
        customer_name="Алексей"
    )

    # 2. Контроллер
    controller = PizzaController()
    controller.add_menu_pizza(margherita)
    controller.add_menu_pizza(pepperoni)
    controller.add_custom_pizza(my_pizza)

    # 3. Представление
    view = PizzaView()
    view.show_pizza_list(controller.get_menu_pizzas(), "Пиццы из меню")
    view.show_pizza_list(controller.get_custom_pizzas(), "Собственные пиццы")
    view.show_total(controller.get_total_price())