import random
import time

class Character:
    def __init__(self, name, health, max_health, attack_power, attacks, icon=''):
        self.name = name
        self.max_health = max_health
        self.health = health
        self.attack_power = attack_power
        self.attacks = attacks
        self.icon = icon
        self.is_alive = True

    def input_attack(self):
        while(True):
            attack_names = list(self.attacks)
            attack_choice = input(f"\tHow will you attack your foe?\n\n{self.list_attacks()}\n\n\t>>> ").lower()
            if attack_choice.isnumeric() and int(attack_choice) in range(len(self.attacks)):
                print(f"\t{self.name.upper()} uses {attack_names[int(attack_choice)].upper()}")
                print(f"\t{self.attacks[attack_names[int(attack_choice)]]}")
                break
            elif (attack_choice in attack_names):
                print(f"\t{self.name.upper()} uses {attack_choice.upper()}")
                print(f"\t{self.attacks[attack_choice]}")
                break
            else:
                print("\tHuh? Try entering the number or name of attack.\n")
        time.sleep(1)
        return self.generate_attack_damage()

    def random_attack(self):
        random_attack_choice = random.randrange(0,len(self.attacks))
        attack_name_key_list = list(self.attacks)
        random_attack_name = attack_name_key_list[random_attack_choice]
        print(f"\t{self.name.upper()} uses {random_attack_name.upper()}!")
        print(f"\t{self.attacks[random_attack_name]}")
        time.sleep(1)
        return self.generate_attack_damage()

    def take_damage(self, damage):
        if (damage >= self.health):
            self.health = 0
            self.is_alive = False
        else:
            self.health -= damage
        print(f"\n\t{self.name.upper()} takes {damage}hp of damage!\tHealth Remaining: ({self.health}/{self.max_health})\n")
        time.sleep(1)

    def reset_health(self):
        self.health = self.max_health
        self.is_alive = True

    def generate_attack_damage(self):
        d20_roll = random.random()
        return int(self.attack_power * d20_roll)

    def list_attacks(self):
        attack_list_str = ''
        attack_names = list(self.attacks)
        for i, attack_name in enumerate(attack_names):
            attack_list_str += f"\t[{i}]\t{attack_name.title()}\n"
        return attack_list_str

