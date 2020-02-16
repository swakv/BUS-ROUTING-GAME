import pygame
from pygame.locals import *
import time
import threading
from Main import Main
from Mapping import Mapping

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LIGHTGREEN = (76, 153, 0)
DARKGREEN = (0, 102, 0)
YELLOW = (255, 196, 0)
ORANGE = (255, 128, 0)
RED = (255, 0, 0)

MAPRED = Mapping.getMapping('red')
MAPBLUE = Mapping.getMapping('blue')

x_coordb = [755, 700, 670, 625, 685, 740, 780, 840, 785, 670, 595, 560, 505, 400, 320, 245, 230, 200, 180, 300, 380, 400, 300, 318, 420, 510, 580, 700, 800]
y_coordb = [-490, -380, -290, -180, -120, -40, 40, 120, 205, 230, 225, 335, 420, 360, 360, 310, 210, 60, -10, -40, -90, -135, -225, -305, -398, -470, -530, -575, -560]
anglesb = [-45, -20, -20, -42, 55, 10, 40, 20, -55, -90, -55, 0, -55, 230, -45, 180, 190, 180, 120, 120, 120, 230, 230, 135, 125, 125, 125, 105, 45]

angles = [45, 90, 105, 120, 125, 135, 230, 230, 120, 120, 180,185, 190,185, 200,-90, -55, 0, -55, -90, -55, 20, 40, 10, 55, -42, -20, -20, -45]
x_coord = [800,750, 700,640, 520, 345, 325, 420, 360, 260, 220, 260, 265,270, 265,395,505, 590, 595, 670, 785, 880, 805, 765, 685, 685, 710,730, 785]
y_coord = [-560, -570, -575, -540, -490, -335, -245, -135, -70, -20, 20, 185, 250,345, 400, 470, 420, 335, 225, 220, 205, 120, 65, -40, -120, -205, -330, -430, -510]

x_prog = [150, 95, 100, 225, 363, 471, 479, 428, 418, 464, 414, 294,155]
y_prog = [355, 482, 560, 653, 564, 503, 432, 329, 239, 154, 74, 108,220]

x_progb = [721, 719, 771, 851,1030, 982, 1011, 1046, 921, 787, 684, 652]
y_progb = [360, 282, 180, 119,148, 246, 370, 494, 553, 542, 539, 434]


class frontEnd:

    def __init__(self):
                
        pygame.init()
        #FONT AND TEXT FOR WELCOME SCREEN
        self.font = pygame.font.SysFont("comicsansms", 22)
        self.text = self.font.render("Click to Start", True, (230, 179, 14))
        # Set the height and width of the screen
        self.w, self.h = 1200, 750
        self.screen = pygame.display.set_mode([self.w,self.h])
        pygame.display.set_caption("Game Screen")
        # load logo
        self.loadLogo()
        # load Red Map
        self.loadRedMap()
        # load blue Map
        self.loadBlueMap()
        # load bus image
        self.loadBus()
        self.backEnd = Main()
        # Loop until the user clicks the close button.
        self.done = False
        self.page = 1
        # load + image
        self.loadAdd()
        self.totalCost = 0

    def loadLogo(self):
        #SETTING FOR LOGO 
        self.logo = pygame.image.load('logo.png')
        self.logo.convert()
        self.rectLogo = self.logo.get_rect()
        self.rectLogo.center = self.w//2, (self.h-50)//2

    def loadAdd(self):
        #SETTING FOR ADD
        self.add = pygame.image.load('plus.png')
        self.add.convert()
        self.rectAdd = self.add.get_rect()
        self.rectAdd.center = (self.w-195)//2, (self.h+530)//2
        self.rectAdd2 = self.add.get_rect()
        self.rectAdd2.center = (self.w+945)//2, (self.h+530)//2

    def loadRedMap(self):
        #SETTING FOR RED MAP
        self.redMap = pygame.image.load('red1.png')
        self.redMap.convert()
        self.rectRed = self.redMap.get_rect()
        self.rectRed.center = (self.w-575)//2, (self.h)//2

    def loadBlueMap(self):
        #SETTING FOR BLUE MAP
        self.blueMap = pygame.image.load('blue1.png')
        self.blueMap.convert()
        self.rectBlue = self.blueMap.get_rect()
        self.rectBlue.center = (self.w+575)//2, (self.h)//2

    def loadBus(self):
        #SETTING FOR BUS

        #SPAWN THE BUS EVERY TIME AT
        # x = w + 800
        # y = h - 560
        # speed = 50
        # angle = 45

        self.busImg = pygame.image.load('bussmol.png')
        self.busImg.convert()
        self.busRect = self.busImg.get_rect()
        self.speed = 50
        self.transparent = (0, 0, 0, 0)

    def move_bus(self,image, speed, x, y, angle):

        def rot_center(image, angle):
            center = image.get_rect().center
            rotated_image = pygame.transform.rotate(image, angle)
            new_rect = rotated_image.get_rect(center = center)
            return rotated_image, new_rect

        image, n = rot_center(image, angle)

        x += speed
        y += speed

        rect3 = self.busImg.get_rect()
        rect3.center = x//2, y//2

        self.screen.blit(image, rect3)

        return image

    def pageLoop(self):
        # -------- Page Loop -----------
        i = 0
        initHandle = True
        while not self.done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        self.done = True
                elif initHandle:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.page += 1
                        if self.page == 3:
                            initHandle = False
                else:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        x, y = event.pos
                        if ((x <= 524) and (x >= 477)) and ( (y <= 660) and ( y>= 615) ) :
                            self.backEnd.addBus('red')
                        elif ((x <= 1095) and (x >= 1048)) and ( (y <= 660) and ( y>= 615) ):
                            self.backEnd.addBus('blue')
                        elif x <= (self.w)//2+70 and x >= self.w//2-70 and y >= (self.h+710)//2-25 and y <= (self.h+710)//2+25:
                            self.renderPage4()
                            self.page = 4
                            print(self.totalCost)
        
            # Set the screen background
            self.screen.fill(BLACK)
            
            if self.page == 1:
                # page 1
                self.renderPage1()

            elif self.page == 2:
                # page 2
                self.renderPage2()
            
            elif self.page == 3:
                # page 3
                self.renderPage3(i)
                i+=1
                

    def renderPage1(self):
        # page 1
        self.screen.fill(BLACK)

        #replace img,rect with logo,rectLogo appropriately
        self.screen.blit(self.logo, self.rectLogo)
        self.screen.blit(self.text,(615 - self.text.get_width() // 2, 410 - self.text.get_height() // 2))
        pygame.display.update()

    def renderPage2(self):
        # page 2
        self.text = self.font.render("WELCOME TO BUSy", True, WHITE)
        self.screen.blit(self.text, [500, 260])
        self.text = self.font.render("An app which helps you save the environment by reducing fuel", True, WHITE)
        self.screen.blit(self.text, [270, 300])
        self.text = self.font.render("used along with time and energy!", True, WHITE)
        self.screen.blit(self.text, [400, 330])
        pygame.display.update()

    def drawFullBar(self,xCoord,yCoord,fractionFull):
        if fractionFull>0.8:
            Color = RED
        elif fractionFull>0.6:
            Color = ORANGE
        elif fractionFull>0.4:
            Color = YELLOW
        elif fractionFull>0.2:
            Color = LIGHTGREEN
        else:
            Color = DARKGREEN

        pygame.draw.rect(self.screen, Color, (xCoord,yCoord,50,15), 2)
        pygame.draw.rect(self.screen, Color, (xCoord,yCoord,int(50*fractionFull),15))

    def drawBusBlue(self,i):
        self.move_bus(self.busImg,self.speed,self.w+x_coordb[i],self.h+y_coordb[i], anglesb[i]+180)

    def drawBusRed(self,i):
        self.move_bus(self.busImg,self.speed,30 + x_coord[i],self.h+y_coord[i], angles[i])

    def renderPage3(self,i):
        self.screen.fill(BLACK)
        # img1/img2 replace by red/blue
        self.screen.blit(self.redMap, self.rectRed)
        self.screen.blit(self.blueMap, self.rectBlue)
        self.screen.blit(self.add,self.rectAdd)
        self.screen.blit(self.add,self.rectAdd2)
        pygame.draw.rect(self.screen, (255,255,255), ((self.w)//2-70, (self.h +710)//2-25,140,50))
        self.fin = self.font.render("FINISH!", True, (0, 0, 0))

        self.rectAddfin = self.fin.get_rect()
        self.rectAddfin.center = (self.w)//2, (self.h + 710 )//2

        self.screen.blit(self.fin, self.rectAddfin)

        busStopsRed = self.backEnd.getBusStops('red')

        for x,stop in enumerate(busStopsRed):
            self.drawFullBar(x_prog[x],y_prog[x],stop.currentCapacity/stop.maxCapacity)

        busStopsBlue = self.backEnd.getBusStops('blue')
        for x,stop in enumerate(busStopsBlue):
            self.drawFullBar(x_progb[x],y_progb[x],stop.currentCapacity/stop.maxCapacity)

        busesred = self.backEnd.getActiveBuses('red')

        for bus in busesred:
            i = MAPRED[bus.currentLocation]
            self.drawBusRed(i)

        busesblue = self.backEnd.getActiveBuses('blue')

        for bus in busesblue:
            i = MAPBLUE[bus.currentLocation]
            self.drawBusBlue(i)
        # add for loop to render the buses
        # add for loop to render the fullness bars
        # for x in range(len(x_progb)):
            

        # for x in range(len(x_prog)):
        #     self.drawFullBar(x_prog[x],y_prog[x],0.75)
        self.totalCost += self.backEnd.step()

        self.text = self.font.render("Total Cost:  "+str(self.totalCost), True, (230, 179, 14))

        self.rectAddf = self.text.get_rect()
        self.rectAddf.center = (self.w)//2, (self.h -710 )//2

        self.screen.blit(self.text, self.rectAddf)



        # self.drawFullBar(851,119,0.75)
        pygame.time.wait(500)
        pygame.display.update()


    def renderPage4(self):
        self.screen.fill(BLACK)
        
        self.text = self.font.render("THANK YOU!", True, (255, 255, 255))
        self.rectAddt = self.text.get_rect()
        self.rectAddt.center = (self.w)//2, (self.h)//2

        self.screen.blit(self.text, self.rectAddt)

        self.textc = self.font.render("Total Cost:  "+str(self.totalCost), True, (255, 255, 255))
        self.rectAddc = self.textc.get_rect()
        self.rectAddc.center = (self.w)//2, (self.h - 100)//2

        self.screen.blit(self.textc, self.rectAddc)

        pygame.display.update()
        

        
if __name__ == "__main__":
    a= frontEnd()
    a.pageLoop()
 
