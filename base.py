#배경 설정
import os
import pygame
import random

#클래스 잠시 보류
class Jombie(pygame.sprite.Sprite): # 클래스를 안쓰면 안되는 이유는 100개의 보석이 있다고 치면, 그 100개의 보석을 일일히 다 정의할 수 없기 때문. 클래스를 이용해서 찍어내면 훨씬 간단함.
    def __init__(self, image, x, y): #어떤 객체마다 어떤 이미지를 쓰고 어떤 위치에 표시할지 정의하는 것임. !!!!!!!!!!!!!! 
        super().__init__() #상속 받았으니 초기화
        self.image = image
        self.rect = image.get_rect()#정보. xy좌표나 가로 세로 크기가 어떤지 정의한다.
        self.jombie_x_pos = jombie_x_pos
        self.jombie_y_pos = jombie_y_pos

    def move(self, x_pos, y_pos):
        self.x += x_pos
        self.y += y_pos

    
def respon(jombie_x_pos, jombie_y_pos):
        jombie_x_pos = 0
        jombie_y_pos = random.randint(0, 620)
        

def update_score(score): #스코어 계산 함수
    global curr_score #전역 공간에 있는 curr_score을 쓰겠다.
    curr_score += score


def display_score(): #스코어 표출 함수
    txt_curr_score = game_font.render(f"Curr Score: {curr_score:,}", True, BLACK)
    screen.blit(txt_curr_score, (50, 20)) 

    txt_goal_score = game_font.render(f"Goal Score: {goal_score:,}", True, BLACK)
    screen.blit(txt_goal_score, (50, 80)) 

def display_time(time): #타이머 표출 함수
    txt_timer = game_font.render(f"Time : {time}", True, BLACK)
    screen.blit(txt_timer, (1100, 50))

def display_game_over(): #게임 종료 선언 함수
    game_font = pygame.font.SysFont("arialrounded", 60) #큰 폰트
    txt_game_over = game_font.render(game_result, True, BLACK)
    rect_game_over = txt_game_over.get_rect(center=(int(screen_width / 2), int(screen_height / 2)))
    screen.blit(txt_game_over, rect_game_over)#화면 중앙에 게임오버 표시

def update_shot(shot): #스코어 계산 함수
    global curr_shot #전역 공간에 있는 curr_score을 쓰겠다.
    curr_shot -= shot

def display_shot(): #스코어 표출 함수
    txt_curr_shot = game_font.render(f"remaining bullets: {curr_shot:,}", True, BLACK)
    screen.blit(txt_curr_shot, (300, 20)) 

def load_shot(loding): #장전 아이템 함수
    global curr_shot
    curr_shot += loding



total_time = 300 #총 시간
start_ticks = pygame.time.get_ticks() #현재 시간을 받아온다.

# 점수 관련 변수
goal_score = 1000 #목표 점수
curr_score = 0 #현재 점수
curr_shot = 10 #현재 남은 총알 개수

#색깔변수
RED =(255,0,0)
BLACK = (0,0,0)

pygame.init()
screen_width = 1280
screen_height = 720
character_width = 70
character_height = 70

game_font = pygame.font.SysFont("arialrounded", 30)

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("JOMBIE WORLD")

clock = pygame.time.Clock()

#배경 이미지 불러오기
current_path = os.path.dirname(__file__) #현재 파일 위치를 반환
background = pygame.image.load(os.path.join(current_path, "background.png"))

#캐릭터
character = pygame.image.load(os.path.join(current_path, "character.png")).convert_alpha()
character_size = character.get_rect().size
character_width = character_size[0] #캐릭터의 가로 크기
character_height = character_size[1] #캐릭터의 세로 크기
character_x_pos = 50
character_y_pos = 300

#좀비1
jombie = pygame.image.load(os.path.join(current_path, "jombie.png")).convert_alpha()
# jombie = pygame.image.load("C:\\Users\\admin\\Desktop\\Study\\게임개발\\pygame_basic\\my_project\\jombie.png").convert_alpha()
jombie_size = jombie.get_rect().size
jombie_width = jombie_size[0] #캐릭터의 가로 크기
jombie_height = jombie_size[1] #캐릭터의 세로 크기
jombie_x_pos = screen_width
jombie_y_pos = random.randint(0, 620)

#좀비2
jombie2 = pygame.image.load(os.path.join(current_path, "jombie.png")).convert_alpha()
# jombie = pygame.image.load("C:\\Users\\admin\\Desktop\\Study\\게임개발\\pygame_basic\\my_project\\jombie.png").convert_alpha()
jombie2_size = jombie2.get_rect().size
jombie2_width = jombie2_size[0] #캐릭터의 가로 크기
jombie2_height = jombie2_size[1] #캐릭터의 세로 크기
jombie2_x_pos = screen_width
jombie2_y_pos = random.randint(0, 620)

#좀비3
jombie3 = pygame.image.load(os.path.join(current_path, "jombie.png")).convert_alpha()
# jombie = pygame.image.load("C:\\Users\\admin\\Desktop\\Study\\게임개발\\pygame_basic\\my_project\\jombie.png").convert_alpha()
jombie3_size = jombie3.get_rect().size
jombie3_width = jombie3_size[0] #캐릭터의 가로 크기
jombie3_height = jombie3_size[1] #캐릭터의 세로 크기
jombie3_x_pos = screen_width
jombie3_y_pos = random.randint(0, 620)

#좀비3
jombie4 = pygame.image.load(os.path.join(current_path, "jombie.png")).convert_alpha()
# jombie = pygame.image.load("C:\\Users\\admin\\Desktop\\Study\\게임개발\\pygame_basic\\my_project\\jombie.png").convert_alpha()
jombie4_size = jombie4.get_rect().size
jombie4_width = jombie4_size[0] #캐릭터의 가로 크기
jombie4_height = jombie4_size[1] #캐릭터의 세로 크기
jombie4_x_pos = screen_width
jombie4_y_pos = random.randint(0, 620)

#총알
bullet = pygame.image.load(os.path.join(current_path, "bullet.png")).convert_alpha()
bullet_size = bullet.get_rect().size
bullet_width = bullet_size[0] #캐릭터의 가로 크기
bullet_height = bullet_size[1] #캐릭터의 세로 크기
bullet_x_pos = character_x_pos + character_width - bullet_width*2
bullet_y_pos = character_y_pos + bullet_height*2 - 15

#장전 아이템 
load_item = pygame.image.load(os.path.join(current_path, "load.png")).convert_alpha()
load_item_size = load_item.get_rect().size
bullet_width = load_item_size[0] #캐릭터의 가로 크기
load_item_height = load_item_size[1] #캐릭터의 세로 크기
load_item_x_pos = random.randint(0, 1100)
load_item_y_pos = random.randint(0, 620)

#여러발 발사 가능하게
bullets = []
shot = 1

#좀비 리스트
jombies = []
jombie_score = 10


#이동 관련 함수
character_speed = 0.5
bullet_speed = 20
jombie_speed = 5
jombie2_speed = 2
jombie3_speed = 7
jombie4_speed = 0.5
to_x = 0
to_y = 0
running = True

#사라질 무기, 좀비 저장 변수
bullets_to_remove = -1
jombies_to_remove = -1

while running:
    dt = clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:#캐릭터를 왼쪽으로
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:#캐릭터를 오른쪽으로
                to_x += character_speed
            elif event.key == pygame.K_UP:#캐릭터를 위로
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:#캐릭터를 아래로
                to_y += character_speed

            elif event.key == pygame.K_SPACE: #스페이스바를 누르면 총알 발사
                if curr_shot > 0:
                    bullet_x_pos = character_x_pos + character_width - bullet_width*2 #무기 위치 정의
                    bullet_y_pos = character_y_pos + bullet_height*2 - 15
                    bullets.append([bullet_x_pos, bullet_y_pos])
                    update_shot(shot)
                else:
                    pass

            for i in range(len(bullets)):
                b = bullets[i]
                bullet_x_pos += bullet_speed    
                

        if event.type == pygame.KEYUP: #방향키에 손을 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                to_y = 0
            
    character_x_pos += to_x * dt #보정 #캐릭터의 x축을 to_x 로 입력받아서 움직이게 함
    character_y_pos += to_y * dt #보정 #캐릭터의 y축을 to_y 로 입력받아서 움직이게 함  

    # print(character_x_pos, character_y_pos, bullet_x_pos, bullet_y_pos)
    
    #가로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    #세로 경계값 처리
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    #좀비 이동시키는 코드
    jombie_x_pos -= jombie_speed
    jombie2_x_pos -= jombie2_speed
    jombie3_x_pos -= jombie3_speed

    if jombie_x_pos < 0:
        jombie_x_pos = screen_width
        jombie_y_pos = random.randint(0, 620)
    if jombie2_x_pos < 0:
        jombie2_x_pos = screen_width
        jombie2_y_pos = random.randint(0, 620)
    if jombie3_x_pos < 0:
        jombie3_x_pos = screen_width
        jombie3_y_pos = random.randint(0, 620)
    
    if bullets_to_remove > -1:
        del bullets[bullets_to_remove]
        bullets_to_remove = -1

    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    jombie_rect = jombie.get_rect()
    jombie_rect.left = jombie_x_pos
    jombie_rect.top = jombie_y_pos
    jombie2_rect = jombie2.get_rect()
    jombie2_rect.left = jombie2_x_pos
    jombie2_rect.top = jombie2_y_pos
    jombie3_rect = jombie3.get_rect()
    jombie3_rect.left = jombie3_x_pos
    jombie3_rect.top = jombie3_y_pos

    bullet_rect = bullet.get_rect()
    bullet_rect.left = bullet_x_pos
    bullet_rect.top = bullet_y_pos

    load_item_rect = load_item.get_rect()
    load_item_rect.left = load_item_x_pos
    load_item_rect.top = load_item_y_pos

    #좀비 사람 충돌처리
    if character_rect.colliderect(jombie_rect):
    # if pygame.sprite.collide_mask(character, jombie): #실제 이미지 충돌처리
        print("GAME OVER")
        running = False
    if character_rect.colliderect(jombie2_rect):
    # if pygame.sprite.collide_mask(character, jombie): #실제 이미지 충돌처리
        print("GAME OVER")
        running = False
    if character_rect.colliderect(jombie3_rect):
    # if pygame.sprite.collide_mask(character, jombie): #실제 이미지 충돌처리
        print("GAME OVER")
        running = False
        
    
    if bullet_rect.colliderect(jombie_rect):
        jombie_x_pos = screen_width
        jombie_y_pos = random.randint(0, 620)
        print("kill")
        update_score(jombie_score)
        
    if bullet_rect.colliderect(jombie2_rect):
    # if pygame.sprite.collide_mask(bullet, jombie): #실제 이미지 충돌처리
        jombie2_x_pos = screen_width
        jombie2_y_pos = random.randint(0, 620)
        print("kill")
        update_score(jombie_score)
        
    if bullet_rect.colliderect(jombie3_rect):
    # if pygame.sprite.collide_mask(bullet, jombie): #실제 이미지 충돌처리
        jombie3_x_pos = screen_width
        jombie3_y_pos = random.randint(0, 620)
        print("kill")
        update_score(jombie_score)
        

    if character_rect.colliderect(load_item_rect):
        load_shot(random.choice([1, 2, 3]))
        load_item_x_pos = random.randint(0, 1100)
        load_item_y_pos = random.randint(0, 620)
        

    #무기 위치 조정 
    bullets = [ [b[0] + bullet_speed, b[1]] for b in bullets]    

    #천장에 닿은 무기 없애기
    bullets = [ [b[0], b[1]] for b in bullets if b[0] < 1280]

    

    screen.blit(background, (0, 0))
    for bullet_x_pos, bullet_y_pos in bullets:
        screen.blit(bullet, (bullet_x_pos, bullet_y_pos))

    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(jombie, (jombie_x_pos, jombie_y_pos))
    screen.blit(jombie2, (jombie2_x_pos, jombie2_y_pos))
    screen.blit(jombie3, (jombie3_x_pos, jombie3_y_pos))
    screen.blit(load_item, (load_item_x_pos, load_item_y_pos))
#점수정보를 보여주는 함수
    display_score()

#남은 총알 수를 보여주는 함수
    display_shot()

#시간 계산 
    elapsed_time = (pygame.time.get_ticks() -start_ticks) / 1000 #ms -> s
    display_time(total_time - int(elapsed_time)) #시간 표시

    if total_time - int(elapsed_time) <= 0:
        running = False
        if curr_score >= goal_score:
            game_result = "Mission complete"
        else:
            game_result = "Game Over"
        #게임 종료 메시지  표시
        display_game_over()

    pygame.display.update()
pygame.time.delay(2000) #2초 정도 대기 후 종료
pygame.quit()

#좀비를 30마리 잡으면 다음 스테이지.
#좀비를 여러마리 단체로 나오게 함.
#총알이 좀비를 맞으면 사라짐.
#아이템이 랜덤으로 나오게 함.
#점수가 200 단위로 넘으면 시간 추가.