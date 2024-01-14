import pygame

pygame.init()

#Tạo một màn hình hiển thị trò chơi với kích thước chiều rộng là 400 và chiều cao là 300
dis = pygame.display.set_mode((400,300))

#Cho phép thực hiện cập nhật một số thành phần của màn hình
pygame.display.update()

pygame.display.set_caption('Snake game')

#Tạo màu cho con rắn
blue=(0,0,255)
red=(255,0,0)

game_end=False

while not game_end:
    for event in pygame.event.get():
        #Phát hiện thao tác thoát khỏi trò chơi của người dùng
        if event.type==pygame.QUIT:
            game_end=True

    #Thực hiện vẽ một ô hình vuông màu xanh nước biển(đại diện cho đầu con rắn) lên trên màn hình với vị trí
    #trên màn hình máy tính (x, y) là (200, 150) và có chiều rộng, chiều cao là 10
    pygame.draw.rect(dis,blue,[200,150,10,10])

pygame.quit()

quit()


