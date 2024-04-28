from pygame import*

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (wight, height))  # вместе 55,55 - параметры
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


ball = GameSprite('ball.png', 225,225,4,50,50)



window = display.set_mode((500, 500))
col1 = (0,0, 255)
mw.fill(col1)
cloock = time.Clock()

run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    if not finish:
        ball.reset()
    display.update()
    cloock/tick(40)
