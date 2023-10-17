import pygame
import os 
import random 
import sys 




pygame.init()


SCREEN_HEIGHT = 600
SCREEN_WIDHT = 1100 
DEAD = pygame.image.load(os.path.join("element game/dino","DinoDead.png"))
SCREEN = pygame.display.set_mode((SCREEN_WIDHT,SCREEN_HEIGHT))
iconImage = pygame.image.load(os.path.join("element game/dino","dino.png"))
iconWindow = pygame.display.set_icon(iconImage)


#stock image in game 
RUNNING =  [pygame.image.load(os.path.join("element game/dino","DinoRun1.png")),
            pygame.image.load(os.path.join("element game/dino","DinoRun2.png"))]
JUMPING = pygame.image.load(os.path.join("element game/dino","DinoJump.png"))
DUCKING = [pygame.image.load(os.path.join("element game/dino","DinoDuck1.png")),
           pygame.image.load(os.path.join("element game/dino","DinoDuck2.png"))]

#cactus 
SMALL_CACTUS = [pygame.image.load(os.path.join("element game/cactus","SmallCactus1.png")),
                pygame.image.load(os.path.join("element game/cactus","SmallCactus2.png")),
                pygame.image.load(os.path.join("element game/cactus","SmallCactus3.png"))]

LARGE_CACTUS = [pygame.image.load(os.path.join("element game/cactus","LargeCactus1.png")),
                pygame.image.load(os.path.join("element game/cactus","LargeCactus2.png")),
                pygame.image.load(os.path.join("element game/cactus","LargeCactus3.png"))]

#bird image 
BIRD = [pygame.image.load(os.path.join("element game/bird","Bird1.png")),
        pygame.image.load(os.path.join("element game/bird","Bird2.png"))]

#other image 
CLOUD = pygame.image.load(os.path.join("element game/other","Cloud.png"))
GAME_OVER = pygame.image.load(os.path.join("element game/other","GameOver.png"))
RESET = pygame.image.load(os.path.join("element game/other","Reset.png"))
TRACK = pygame.image.load(os.path.join("element game/other","Track.png"))\


#proces 

class Dinosaur : 


    X_POS_DINO = 100
    Y_POST_DINO = 310
    Y_post_DUCK = 340
    JUMP_VALUE = 9

    def __init__(self) -> None:


        #image
        self.duck_img = DUCKING
        self.Jump_img = JUMPING 
        self.run_img = RUNNING 
        self.dead_img = DEAD

        #position start
        self.dino_duck = False 
        self.dino_jump = False 
        self.dino_run = True
        self.dino_dead = False
        self.dino_jumpSuper = False 
        self.step_index = 0
        
        self.jump_vel = self.JUMP_VALUE
        self.image = self.run_img[0]
        self.dino_reck = self.image.get_rect()
        self.dino_reck.x = self.X_POS_DINO
        self.dino_reck.y = self.Y_POST_DINO
   

       
    def update(self, userInput): 
       

        if self.dino_duck: 
            self.duck()
        if self.dino_run: 
            self.run()
        if self.dino_jump: 
            self.jump()

        if self.step_index >= 10: 
            self.step_index = 0 


        if userInput[pygame.K_UP] and not self.dino_jump: 
            self.dino_jump = True 
            self.dino_run = False 
            self.dino_duck = False 
        elif userInput[pygame.K_DOWN] and not self.dino_jump: 
            self.dino_jump = False
            self.dino_run = False 
            self.dino_duck = True 
        elif not (self.dino_jump or userInput[pygame.K_DOWN]): 
            self.dino_jump = False 
            self.dino_run = True 
            self.dino_duck = False 
        
   
            
    def dead(self) : 
        self.image = self.dead_img 
        self.dino_rect = self.image.get_rect()
        self.dino_reck.x = self.X_POS_DINO
        self.dino_reck.y = self.Y_post_DUCK


    def run(self): 
        self.image = self.run_img[self.step_index // 5 ]
        self.dino_reck = self.image.get_rect()
        self.dino_reck.x = self.X_POS_DINO
        self.dino_reck.y = self.Y_POST_DINO
        self.step_index +=1
      

       
    def jump(self): 
        
        self.image = self.Jump_img
        if self.dino_jump : 
            self.dino_reck.y  -= self.jump_vel * 4 
            self.jump_vel -= 1
        if self.jump_vel < - self.JUMP_VALUE:
            self.dino_jump = False
            self.jump_vel = self.JUMP_VALUE


    
    def duck(self): 
        self.image = self.duck_img[self.step_index // 5 ]
        self.dino_reck = self.image.get_rect()
        self.dino_reck.x = self.X_POS_DINO
        self.dino_reck.y = self.Y_post_DUCK
        self.step_index +=1


    
    def draw(self,SCREEN): 
        SCREEN.blit(self.image,(self.dino_reck.x, self.dino_reck.y))

class Cloud : 
    def __init__(self) -> None:
        self.image = CLOUD
        self.x = SCREEN_WIDHT + random.randint(800,1000)
        self.y = random.randint(50,100)
        self.widht = self.image.get_width()
    def update(self): 
        self.x -= game_speed 
        if self.x <- self.widht : 
            self.x = SCREEN_WIDHT + random.randint(2500,3000)
            self.y = random.randint(50,100)

    def draw(self,SCREEN) : 
        SCREEN.blit(self.image,(self.x,self.y))

    
class Obstacle : 

     def __init__(self,image,type) -> None:
        
         self.image =  image 
         self.type = type 
         self.rect = self.image[self.type].get_rect()
         self.rect.x = SCREEN_WIDHT + 5
        
     def update (self) : 
         
        
         self.rect.x -= game_speed
         
         if self.rect.x < -self.rect.width  :
             obstacle.pop()

     def draw(self,SCEREEN) : 
        
         SCREEN.blit(self.image[self.type],self.rect)
     
class SmallCactus(Obstacle) : 
    def __init__(self,image) -> None:
        self.type = random.randint(0,2)
        super().__init__(image,self.type)
        self.rect.y = 325 


class LargeCactus(Obstacle) : 
    def __init__(self,image) -> None:
        self.type = random.randint(0,2)
        super().__init__(image,self.type)
        self.rect.y = 300

class Bird(Obstacle) : 
    def __init__(self,image) -> None:
        self.type = 0
        super().__init__(image,self.type) 
        self.rect.y = random.choice([250,330,220])
        self.index = 0 
    def draw(self, SCEREEN):
        if self.index >= 9 : 
            self.index = 0 
        SCREEN.blit(self.image[self.index//5],self.rect)


        self.index +=1         


class rintangn2 : 
    
    def __init__(self,image,type) -> None:
         self.image = image 
         self.type = type 
       
         self.rect = self.image[self.type].get_rect()

         if count == 1  :           
            self.rect.x = 550+ SCREEN_WIDHT + 5
         elif count >  1 : 
             self.rect.x = SCREEN_WIDHT
        

    def update(self) : 
         self.rect.x -= game_speed  
         if self.rect.x < -self.rect.width : 
            obstacle_2.pop() 
         
        
    def draw(self,SCREEN) : 
        SCREEN.blit(self.image[self.type],self.rect)
        
        
     
class SmallCactu(rintangn2) : 
    def __init__(self,image) -> None:
        self.type = random.randint(0,2)
        super().__init__(image,self.type)
        self.rect.y = 325 


class LargeCactu(rintangn2) : 
    def __init__(self,image) -> None:
        self.type = random.randint(0,2)
        super().__init__(image,self.type)
        self.rect.y = 300

class Bir(rintangn2) : 
    def __init__(self,image) -> None:
        self.type = 0
        super().__init__(image,self.type) 
        self.rect.y = random.choice([250,320,220])
        self.index = 0 
    def draw(self, SCEREEN):
        if self.index >= 9 : 
            self.index = 0 
        SCREEN.blit(self.image[self.index//5],self.rect)


        self.index +=1     

    
def main(): 

    global point,game_speed,font,x_post_bg,y_post_bg,obstacle,death_count,obstacle_2,count
    run = True 
    clock = pygame.time.Clock()
    player = Dinosaur()
    point = 0 
    game_speed = 14
    x_post_bg = 0  # seting tampat backgroud berada di posisi x 
    y_post_bg = 380 #seting tempat background berada di posisi y 
    obstacle = []
    obstacle_2 = []
    font = pygame.font.Font("freesansbold.ttf",20)
    font2 = pygame.font.Font("freesansbold.ttf",70)
    cloud = Cloud()
    death_count = 0 
    count = 0 
   
  

    def background() : 
        global x_post_bg,y_post_bg,game_speed,death_count
        bg_widht = TRACK.get_width()
        SCREEN.blit(TRACK,(x_post_bg,y_post_bg))
        SCREEN.blit(TRACK,(bg_widht + x_post_bg,y_post_bg))
        if x_post_bg <= -bg_widht : 
            SCREEN.blit(TRACK,(bg_widht + x_post_bg,y_post_bg))
            x_post_bg = 0 
        x_post_bg -=game_speed


    #tempat ngatur teks yang ada saat game berjalan 
    def score() : 
        global point,game_speed
        point += 1 

        if point % 100 == 0 : 
            game_speed += 1
        if point <= 400 : 
            text = font.render(f"Score : {str(point)}",True,(0,0,0))
            text2 = font2.render("Let's Gooo",True,(0,0,0))
           
        elif  point >= 400 : 
            text = font.render(f"Score : {str(point)}",True,(225,225,225))
            text2 = font2.render("Let's Gooo",True,(225,225,225))
        
        text2_rect = text2.get_rect()
        text2_rect.center = (550,520)
        textRect = text.get_rect()
        textRect.center = (1000,40)
        SCREEN.blit(text2,text2_rect)
        SCREEN.blit(text,textRect)

    while  run : 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT : 
                run = False 
                sys.exit()
        if point >400 : 
            SCREEN.fill((0,0,0))
        else : 
            SCREEN.fill((192,192,192))
        UserInput = pygame.key.get_pressed()

        player.update(UserInput)
        player.draw(SCREEN)
        score()
        background()
        cloud.draw(SCREEN)
      
        cloud.update()



        
        if len(obstacle) == 0  : 
            if random.randint(0,2) == 0 : 
                obstacle.append(SmallCactus(SMALL_CACTUS))
            elif random.randint(0,2) == 1 : 
                obstacle.append(LargeCactus(LARGE_CACTUS))
            elif random.randint(0,2) == 2 : 
                obstacle.append(Bird(BIRD)) 
            count +=1

        if len(obstacle_2) == 0 : 
            if random.randint(0,2) == 0 : 
                obstacle_2.append(SmallCactu(SMALL_CACTUS))
                
            elif random.randint(0,2) == 1 : 
                obstacle_2.append(LargeCactu(LARGE_CACTUS))
            elif random.randint(0,2) == 2 : 
                obstacle_2.append(Bir(BIRD)) 
            count +=1
            


        
   
        for rintangan in obstacle : 
            rintangan.update()
            rintangan.draw(SCREEN)
            if player.dino_reck.colliderect(rintangan.rect) :             
                pygame.time.delay(1000)
                death_count +=1
                menu(death_count)
                sys.exit()

        for rintanga in obstacle_2 : 
            rintanga.update()
            rintanga.draw(SCREEN)
            if player.dino_reck.colliderect(rintanga.rect) :             
                pygame.time.delay(1000)
                death_count +=1
           
                menu(death_count)
                sys.exit()



        clock.tick(30)
        pygame.display.update()


def menu (death_count) : 
    global point 
    run = True 
    while run : 
        SCREEN.fill((225,225,225))
        font = pygame.font.Font("freesansbold.ttf",30)
        if death_count == 0 : 
            text = font.render("Press any key to play",True,(0,0,0))
        elif death_count >= 0 :
            text = font.render("Press any key to Restart",True,(0,0,0))
            score = font.render(f"Score : {point}",True,(0,0,0))
            scoreRect = score.get_rect()
            scoreRect.center = (SCREEN_WIDHT //2, SCREEN_HEIGHT //2 +50)
            SCREEN.blit(score,scoreRect)
        textRect = text.get_rect()
        textRect.center = (SCREEN_WIDHT//2,SCREEN_HEIGHT/2 )
        SCREEN.blit(text,textRect)
        SCREEN.blit(RUNNING[0],(SCREEN_WIDHT//2,SCREEN_HEIGHT//2 -140))
        pygame.display.update()

        for even in pygame.event.get() : 
            if even.type == pygame.QUIT : 
                run = False 
                sys.exit()
            if even.type == pygame.KEYDOWN : 

                main()
               

menu(0)

# if len(obstacle) == 0  : 

        #     if point <= 300 :
        #         obstacle.append(SmallCactus(SMALL_CACTUS))
        #     if point >= 300 and point <= 500 : 
        #         if random.randint(0,1) == 0 : 
        #             obstacle.append(SmallCactus(SMALL_CACTUS))
        #         elif random.randint(0,1) == 1 : 
        #             obstacle.append(LargeCactus(LARGE_CACTUS)) 
        #     if point >= 500 : 
        #         if random.randint(0,2) == 0 : 
        #             obstacle.append(SmallCactu(SMALL_CACTUS))   
        #         elif random.randint(0,2) == 1 : 
        #             obstacle.append(LargeCactu(LARGE_CACTUS))
        #         elif random.randint(0,2) == 2 : 
        #             obstacle.append(Bir(BIRD)) 
        #     count +=1

        # if len(obstacle_2) == 0 : 
        #     if point <= 300 :
        #         obstacle_2.append(SmallCactus(SMALL_CACTUS))
        #     if point >= 300 and point <= 500 : 
        #         if random.randint(0,1) == 0 : 
        #             obstacle_2.append(SmallCactus(SMALL_CACTUS))
        #         elif random.randint(0,1) == 1 : 
        #             obstacle_2.append(LargeCactus(LARGE_CACTUS)) 
        #     if point >= 500 : 
        #         if random.randint(0,2) == 0 : 
        #             obstacle_2.append(SmallCactu(SMALL_CACTUS))   
        #         elif random.randint(0,2) == 1 : 
        #             obstacle_2.append(LargeCactu(LARGE_CACTUS))
        #         elif random.randint(0,2) == 2 : 
        #             obstacle_2.append(Bir(BIRD))        
        #     count +=1 


