class Entity:
    def __init__(self, health, speed, position, **kwargs):
        super().__init__(**kwargs)
        self.health = health
        self.speed = speed
        self.position = position

    def move(self):
        self.position += self.speed

class Attacker:
    def __init__(self, damage, **kwargs):
        super().__init__(**kwargs)
        self.damage = damage

    def attack(self):
        self.health -= self.damage

class Player(Entity, Attacker):
    def __init__(self, health, speed, position, damage):
        super().__init__(
            health=health,
            speed=speed,
            position=position,
            damage=damage               
        )

player1 = Player(health=100, speed = 10, position=0, damage=20)

player1.move()
player1.attack()

print(player1.health, player1.position)