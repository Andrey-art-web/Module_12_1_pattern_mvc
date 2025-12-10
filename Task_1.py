# Product
class Shoe:
    def __init__(self):
        self.shoe_type = None
        self.category = None
        self.color = None
        self.price = None
        self.manufacturer = None
        self.size = None

    def __str__(self):
        return (f"{self.shoe_type} {self.category}, "
                f"Цвет: {self.color}, "
                f"Цена: {self.price}, "
                f"Производитель: {self.manufacturer}, "
                f"Размер: {self.size}")

# Builder
class ShoeBuilder:
    def __init__(self):
        self.shoe = Shoe()

    def set_type(self, shoe_type):
        self.shoe.shoe_type = shoe_type
        return self

    def set_category(self, category):
        self.shoe.category = category
        return self

    def set_color(self, color):
        self.shoe.color = color
        return self

    def set_price(self, price):
        self.shoe.price = price
        return self

    def set_manufacturer(self, manufacturer):
        self.shoe.manufacturer = manufacturer
        return self

    def set_size(self, size):
        self.shoe.size = size
        return self

    def build(self):
        return self.shoe

# Director (опционально)
class ShoeDirector:
    @staticmethod
    def create_men_boots():
        return (ShoeBuilder()
                .set_type("мужская")
                .set_category("ботинки")
                .set_color("черный")
                .set_price(8000)
                .set_manufacturer("Timberland")
                .set_size(42)
                .build())

    @staticmethod
    def create_women_sneakers():
        return (ShoeBuilder()
                .set_type("женская")
                .set_category("кроссовки")
                .set_color("белый")
                .set_price(6000)
                .set_manufacturer("Nike")
                .set_size(38)
                .build())

# Использование
if __name__ == "__main__":
    # Готовая обувь
    boot = ShoeDirector.create_men_boots()
    sneaker = ShoeDirector.create_women_sneakers()

    print(boot)
    print(sneaker)

    # Своя сборка
    custom_shoe = (ShoeBuilder()
                   .set_type("мужская")
                   .set_category("сандалии")
                   .set_color("коричневый")
                   .set_price(3000)
                   .set_manufacturer("Adidas")
                   .set_size(41)
                   .build())
    print(custom_shoe)