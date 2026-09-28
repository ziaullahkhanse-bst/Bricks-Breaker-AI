import pygame

pygame.init()

white=(230,255,230)
darkblue=(20,60,30)
lightblue=(100,200,100)
red=(200,50,50)
buttonColor=(60,120,60)

bricks1=[pygame.Rect(10+i*100,60,80,30) for i in range(6)]
bricks2=[pygame.Rect(10+i*100,100,80,30) for i in range(6)]
bricks3=[pygame.Rect(10+i*100,140,80,30) for i in range(6)]



def draw_brick(bricks):
    for i in bricks:
        pygame.draw.rect(screen,red,i)

score=0

velocity=[1,1]
size=(600,600)

screen=pygame.display.set_mode(size)

pygame.display.set_caption("Bricks Breaker AI")
paddle=pygame.Rect(100,550,200,10)

ball=pygame.Rect(50,250,10,10)

autoPlay = False

btnAuto = pygame.Rect(10, 580, 90, 30)
btnManual = pygame.Rect(110, 580, 90, 30)

gameContinue=True

while gameContinue:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            gameContinue=False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if btnAuto.collidepoint(event.pos):
                autoPlay = True
            if btnManual.collidepoint(event.pos):
                autoPlay = False

    # smooth arrow key movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        if paddle.x > 0:
            paddle.x = paddle.x - 7
    if keys[pygame.K_RIGHT]:
        if paddle.x < 400:
            paddle.x = paddle.x + 7

    # dynamic difficulty
    speed = 1 + (score // 5)

    screen.fill(darkblue)

    pygame.draw.rect(screen,lightblue,paddle)
    font=pygame.font.Font(None,34)
    text=font.render("Score "+str(score),1,white)
    screen.blit(text, (20,10))

    draw_brick(bricks1)
    draw_brick(bricks2)
    draw_brick(bricks3)

    # predictive paddle
    if autoPlay:
        if velocity[1] > 0:
            time_to_reach = (paddle.y - ball.y) / velocity[1]
            future_x = ball.x + velocity[0] * time_to_reach
            while future_x < 0 or future_x > 600:
                if future_x < 0:
                    future_x = -future_x
                if future_x > 600:
                    future_x = 1200 - future_x

            if paddle.x + 100 < future_x:
                paddle.x += 5
            if paddle.x + 100 > future_x:
                paddle.x -= 5
        else:
            if paddle.x + 100 < ball.x:
                paddle.x += 3
            if paddle.x + 100 > ball.x:
                paddle.x -= 3

    if paddle.x < 0:
        paddle.x = 0
    if paddle.x > 400:
        paddle.x = 400

    ball.x = ball.x + velocity[0] * speed
    ball.y = ball.y + velocity[1] * speed

    if ball.x > 590 or ball.x < 0:
        velocity[0] = - velocity[0]

    if ball.y <= 3:
        velocity[1] = - velocity[1]

    pygame.draw.rect(screen,white,ball)

    if ball.colliderect(paddle):
        velocity[1] = - velocity[1]

    for i in bricks1:
        if i.collidepoint(ball.x,ball.y):
            bricks1.remove(i)
            velocity[0]=-velocity[0]
            velocity[1]=-velocity[1]
            score=score+1

    for i in bricks2:
        if i.collidepoint(ball.x,ball.y):
            bricks2.remove(i)
            velocity[0]=-velocity[0]
            velocity[1]=-velocity[1]
            score=score+1

    for i in bricks3:
        if i.collidepoint(ball.x,ball.y):
            bricks3.remove(i)
            velocity[0]=-velocity[0]
            velocity[1]=-velocity[1]
            score=score+1

    pygame.draw.rect(screen, buttonColor, btnAuto)
    pygame.draw.rect(screen, buttonColor, btnManual)
    smallFont = pygame.font.Font(None, 24)
    screen.blit(smallFont.render("AutoPlay", 1, white), (20, 588))
    screen.blit(smallFont.render("Manual", 1, white), (125, 588))

    if ball.y>=590:
        font = pygame.font.Font(None, 74)
        text = font.render("Gameover", 1, red)
        screen.blit(text,(150,350))

        pygame.display.flip()

        pygame.time.wait(2000)

        break

    if score==18:
        font=pygame.font.Font(None,74)
        text=font.render("Won!",1,red)
        screen.blit(text,(150,350))
        pygame.display.flip()

        pygame.time.wait(3000)
        break

    pygame.time.wait(1)
    pygame.display.flip()

pygame.quit()