"""
Random Module
random.seed()
random.sample()

https://www.w3schools.com/python/module_random.asp
https://www.w3schools.com/python/ref_random_seed.asp
https://www.w3schools.com/python/ref_random_sample.asp

Mini Project: Turn-Based Battle Randomizer

Scenario:
Build a tiny turn-based battle simulator that randomly determines
turn order, actions, damage, and loot.

players = ["Alice", "Bob", "Charlie"]
actions = ["Attack", "Defend", "Heal"]
items = ["Potion", "Sword", "Shield", "Gold"]

1. TURN ORDER
   Use shuffle() to randomize the players' turn order.

2. RANDOM ACTION
   Use choice() to give the current player a random action.

3. RANDOM DAMAGE
   Use randint() or randrange() to generate the action's damage value.

4. RANDOM LOOT
   Use sample() to give the winner 2 unique items.

5. RANDOM EFFECT
   Use uniform() to generate a random multiplier between 0.5 and 1.5.

6. REPRODUCIBLE TESTING
   Use seed() so running the battle with the same seed produces
   exactly the same results.

7. EVENT GENERATOR
   Combine the random operations into one function that generates
   a complete random battle event.

Goal:
Run the battle once normally, then run it twice with the same seed
and verify that both test runs produce the same sequence.
"""

import random

players: list[str] = ["Alice", "Bob", "Charlie"]
actions: list[str] = ["Attack", "Defend", "Heal"]
items: list[str] = ["Potion", "Sword", "Shield", "Gold"]


def init_scenario():
    try:
        seed_int: int = int(input("enter seed int: "))
        random.seed(seed_int)
        shuffle_turnorder()
        random_player_action()
        set_random_reward()

        init_scenario()

    except KeyboardInterrupt:
        print("exit.")


def set_random_reward():
    reward: list[str] = random.sample(items, k=2)
    print(f"loot has been found: {reward}")
    random_xp_gain: float = random.uniform(5, 20)
    print(f"the group awarded {random_xp_gain} XP.")


def random_player_action():
    for player in players:
        rnd_action: str = random.choice(actions)
        rnd_number: int = random.randint(10, 20)

        if rnd_action == "Attack":
            print(f"{player} deals {rnd_number} damage.")
        elif rnd_action == "Defend":
            print(f"{player} avoids {rnd_number} damage.")
        elif rnd_action == "Heal":
            print(f"{player} heals {rnd_number} hitpoints.")


def shuffle_turnorder():
    random.shuffle(players)
    print(players)


def main():
    init_scenario()


if __name__ == "__main__":
    main()
