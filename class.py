class Smartphone:
    def __init__(self, brand, model, price):
        """Initialize the Smartphone object."""
        self.brand = brand
        self.model = model
        self.price = price

    def display_info(self):
        """Displays smartphone details."""
        return f"{self.brand} {self.model}, priced at ${self.price}"

    def make_call(self, number):
        """Simulates making a call."""
        return f"Dialing {number} from {self.model}..."

# Inheritance: GamingSmartphone class extends Smartphone
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, price, gpu, refresh_rate):
        """Initialize with additional gaming-specific attributes."""
        super().__init__(brand, model, price)
        self.gpu = gpu
        self.refresh_rate = refresh_rate

    def display_info(self):
        """Override to include gaming features."""
        base_info = super().display_info()
        return f"{base_info}, with {self.gpu} GPU and {self.refresh_rate}Hz refresh rate."

    def play_game(self, game):
        """Simulates playing a game."""
        return f"Launching {game} on {self.model} with {self.gpu} GPU."

# Create objects and demonstrate polymorphism
if __name__ == "__main__":
    # Base class object
    phone = Smartphone("Apple", "iPhone 14", 999)
    print(phone.display_info())
    print(phone.make_call("123-456-7890"))

    # Derived class object
    gaming_phone = GamingSmartphone("Asus", "ROG Phone 6", 1199, "Adreno 730", 144)
    print(gaming_phone.display_info())
    print(gaming_phone.play_game("Genshin Impact"))

