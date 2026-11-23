import collections

class TokenClub:
    """
    Simulates the Token Club's token management system.
    Users can buy tokens and use them for various services.
    """
    def __init__(self):
        self.users = collections.defaultdict(lambda: {'tokens': 0})
        self.services = {
            "standard_drink": 5,
            "premium_drink": 10,
            "vip_lounge_access": 20,
            "special_event_ticket": 30
        }
        print("Token Club system initialized.")
        print(f"Available services and their token costs: {self.services}\n")

    def register_user(self, username):
        """Registers a new user in the club."""
        if username in self.users:
            print(f"User '{username}' already registered.")
            return False
        self.users[username] = {'tokens': 0}
        print(f"User '{username}' registered successfully.")
        return True

    def buy_tokens(self, username, amount):
        """Allows a user to buy a specified amount of tokens."""
        if username not in self.users:
            print(f"Error: User '{username}' not found. Please register first.")
            return False
        if amount <= 0:
            print("Error: Token amount must be positive.")
            return False

        self.users[username]['tokens'] += amount
        print(f"User '{username}' bought {amount} tokens. Current balance: {self.users[username]['tokens']}")
        return True

    def use_tokens_for_service(self, username, service_name):
        """
        Allows a user to use tokens for a specific service.
        This is the core concept from the article: tokens grant access/services.
        """
        if username not in self.users:
            print(f"Error: User '{username}' not found. Please register first.")
            return False
        if service_name not in self.services:
            print(f"Error: Service '{service_name}' not found.")
            return False

        cost = self.services[service_name]
        current_tokens = self.users[username]['tokens']

        if current_tokens >= cost:
            self.users[username]['tokens'] -= cost
            print(f"User '{username}' successfully used {cost} tokens for '{service_name}'.")
            print(f"Remaining tokens for '{username}': {self.users[username]['tokens']}")
            return True
        else:
            print(f"User '{username}' has insufficient tokens for '{service_name}'.")
            print(f"Needed: {cost}, Available: {current_tokens}")
            return False

    def get_user_tokens(self, username):
        """Returns the current token balance for a user."""
        if username not in self.users:
            return None
        return self.users[username]['tokens']

# --- Demonstration ---
if __name__ == "__main__":
    club = TokenClub()

    print("\n--- Scenario 1: New User Experience ---")
    club.register_user("Alice")
    club.buy_tokens("Alice", 25)
    club.use_tokens_for_service("Alice", "standard_drink")
    club.use_tokens_for_service("Alice", "vip_lounge_access") # Alice has 20 tokens left, VIP costs 20.
    club.use_tokens_for_service("Alice", "premium_drink") # Alice has 0 tokens left, premium costs 10.

    print(f"\nAlice's final tokens: {club.get_user_tokens('Alice')}")

    print("\n--- Scenario 2: Another User ---")
    club.register_user("Bob")
    club.buy_tokens("Bob", 15)
    club.use_tokens_for_service("Bob", "premium_drink")
    club.use_tokens_for_service("Bob", "standard_drink") # Bob has 5 tokens left, standard costs 5.
    club.use_tokens_for_service("Bob", "standard_drink") # Bob has 0 tokens left.

    print(f"\nBob's final tokens: {club.get_user_tokens('Bob')}")

    print("\n--- Scenario 3: Error Cases ---")
    club.use_tokens_for_service("Charlie", "standard_drink") # Charlie not registered
    club.register_user("Charlie")
    club.buy_tokens("Charlie", -10) # Invalid token amount
    club.buy_tokens("Charlie", 10)
    club.use_tokens_for_service("Charlie", "non_existent_service") # Invalid service

    print(f"\nCharlie's final tokens: {club.get_user_tokens('Charlie')}")