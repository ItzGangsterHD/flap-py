import pygame
import random
import base64
import sys
from io import BytesIO
from PIL import Image
pygame.init()

HEIGHT = 480
WIDTH = 288
FPS = 60

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Flappy Bird')

bg = pygame.transform.scale2x(pygame.image.load(BytesIO(base64.b64decode(b'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'))))
flap1 = pygame.transform.scale2x(pygame.image.load(BytesIO(base64.b64decode(b'iVBORw0KGgoAAAANSUhEUgAAABEAAAAMCAMAAACz+6aNAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAYUExURVI4RvlzJ/r6+vk6HNflzfe2Q9AwFQAAAPbQHQwAAAAIdFJOU/////////8A3oO9WQAAAAlwSFlzAAAOwwAADsMBx2+oZAAAAFRJREFUGFdtjlsOACEIA4u6cP8bbx9+OgmJHRsFY2ByTK4qrJWgqdqbIooDZppDIYWB8stYXSOsDLOuDhU+Q+k/uqFzOmo0SYfG78h0KtpHWyWQmR8ZGAKS7yayMAAAAABJRU5ErkJggg=='))))
flap2 = pygame.transform.scale2x(pygame.image.load(BytesIO(base64.b64decode(b'iVBORw0KGgoAAAANSUhEUgAAABEAAAAMCAMAAACz+6aNAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAYUExURVI4RvlzJ/r6+vk6HNflzfe2Q9AwFQAAAPbQHQwAAAAIdFJOU/////////8A3oO9WQAAAAlwSFlzAAAOwwAADsMBx2+oZAAAAFNJREFUGFdVzUEOwCAMA0EHKPn/j2tveqmlSHgIQk1E5ji9qrTWlEzV3oYhj9wtxxBSK/0vyUcI7xdELLk6Fj0Ec+6Vzwl/XTI7iLeGWEFiFKf7BRiXAqXMebNcAAAAAElFTkSuQmCC'))))
flap3 = pygame.transform.scale2x(pygame.image.load(BytesIO(base64.b64decode(b'iVBORw0KGgoAAAANSUhEUgAAABEAAAAMCAMAAACz+6aNAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAYUExURVI4RvlzJ/r6+vk6HNflzfe2Q9AwFQAAAPbQHQwAAAAIdFJOU/////////8A3oO9WQAAAAlwSFlzAAAOwwAADsMBx2+oZAAAAFRJREFUGFdlj1EOwDAIQrE6vf+NJ9B9jaQJPtFYjATJ1nVE4BwXfBGZC4yggVxSC4jg3o98yISmNCdxT5XBI/GGbXQ31t/MsBZSxPeYOSKiwfuHmRcTeQKoJnJ7FAAAAABJRU5ErkJggg=='))))
grass = pygame.transform.scale2x(pygame.image.load(BytesIO(base64.b64decode(b'iVBORw0KGgoAAAANSUhEUgAAAKgAAAA4BAMAAACbA67EAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAVUExURVQ4R+T6kXW9Op7kYVZ+KdanVN7XmMkDGZ0AAAAJcEhZcwAADsMAAA7DAcdvqGQAAABYSURBVFjD7c4xEcAwEANBUTAFhYGfQiiYwvOHEIN4TZq7QuWOFGkFku2qmt2LPlV7dhU4agWOXnT+qBU4agWOWm8gnUDqQKCgoKCgoKCgoKCgoKCg/6LdH2Dse9me8c/qAAAAAElFTkSuQmCC'))))
pipedown = pygame.transform.scale2x(pygame.image.load(BytesIO(base64.b64decode(b'iVBORw0KGgoAAAANSUhEUgAAABoAAACgCAMAAAAlxYzvAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAFcUExURVQ4R8Hcd8rjfdPqg9nyid/2juT6kd/4jtjyidPrg7bUcKzKaKPCYJi5WI6wUYSnS3qeQ3GXPGmPNmGJMVuDLVZ+KdLrg9/4j9LrhMnjfbbUb6PDYZi5WYOnS3qfQnGWO2iPNmKIMVuDLNLqg8nlfcHdd6LCYHCWPGKJMVuELdnyiMHddrfUcI6vUcnlfsHcdqLCYXGXO2ePNmGIMeH2juH4jtPrhIOnSXqfRHGWPMnjfoOlSXCXPFuELIWpS5a3V6XEY7TSbsTged31i8PgebXSbqTEY5W2VnabQF6GL4aoS5a2VrXTb931jNHqg8PeeaTEYpW3V3eaQGqPNqXEYtHqgrTTboWoS1+GL4apS7TTb8TeeXaaQGmPN9LqgnebQJW2V9z1i9zzi8PgesTgel+HL93zi16HL5a2V9Hrg2qPN7TSb5a3VtLrgpW3VrXSb8PeesTeeld/KQAAAL1g/WAAAAB0dFJOU/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////8A9nTFawAAAAlwSFlzAAAOwwAADsMBx2+oZAAABA1JREFUWEftVWtz20QUTVrHiePWCS64LSQprQKU8n6F8tLLehhJkVaOIiHLteUkGJcUY5r/P8PZlWLvelpm+MLwwf6SmZy5e88999yjtX/6rd+4Wdmobm7VKjdvrG/Xb91u7Oy+0bzzJqDa1mZ1Y+nfb+EHqLW1Ub1buXd//e36O3uN/YMH7z58VEL3ULVZkQ7f266/v9fYOfig+fjDEqKdNp5Ihx99XL+198nOwYPm4+uqFiVRqX362Xb989uN/d0vvvzqulet8nX1mydHh5TGXuPbp98taEiMYe170ADD/V1A172OKncx1dH9gvwPT39s3vmphOifV/0Avf539ZoyAFdrsqJqutSutiXDtGy50/x5Djmu6lHo2A80EjrdkwUkK5FmnB5X274eq3bSbf4yh9KQ9LLiQc1y0/6zRVXiktgYADoNPBLKQ65XGkae4dOqTItsuctVyTkxMwYZXhQmfa5Kti0zk0bVM1/3LNvhH0xsq3cOaNQKNFWRu8JcxNP9ER688FTX6XPkUaUFjHxgRq7A0LGJFhQ0TFVB1a8cZMV05JGPKjsVeimWR6GxpMdLkBxGpt6iD+o94qbD5m8LCPLSuejIVpgIS7EjMBwzhsR1OtxSUleNAzryQPfAsMPN5YRRbFCGku5RGifcyKjST5nypioaAGqwucbSeazmSefZokqeEFOHGiPQgG1Eb4DGc8pQN6NQVKOU9xiQlTuCbaijAIFGD72GHENHgQ9pLx8GcLFlTihbjQ2mIcgrwr5kGwwHVMMAPpSHPMOQQKhCDaLIfQ5ybLWUN4thNl7DhD7IGOIcQINXPsRSYOwzpkbS+Z3rNSnlhUVhbEFexbosjJ1p6iQRzDaJegG1qE8vBavkeuVg2GLeMNUXwlwOLkVntrmISS4sJYXnC3kN3BeU52mAIaCxH/SsPOXVSCaRGTw/owzNaOL0TxaeT0OVGaD9R+BFU7lzslhKagMqekFe4WDhXvgQDE+zP5EAS+GALVPlZ/CGoEYyId4Mqxz5mYlzELYMNf6CAeDDWHVlvleSq5cXrfkq+ZGhBnJjTA1wSRApHA3MxTwP5enIwsFOIRTzPNwLzws0iFfmBg6W7evlnEbEUrTdMmLyAme+1AsPnkmzS/iwK9xXaWyfHhFsw0GI5bKXZk1LGi8LaBpp1GxjyYijXBgZjjLL+/IQy7w3YJt4RjUcFKtcyg3WC+6Fo4Y8lEdxGV809Hjb4L48+mC7lXlqKAiVKEhRVgVviGFeCAVvDBB6Ink5VL0ZI2+YqBIMoODDwb4pmUmmiZBsU5w5tejgHB+OZW94FzQqpXPNUoSlYJUx+xK1gphMRA1X97VSY5U2q7T5t2nz/z+9VTiswmEVDnPovwmHtau/AaUwnAA13H1XAAAAAElFTkSuQmCC'))))
pipeup = pygame.transform.scale2x(pygame.image.load(BytesIO(base64.b64decode(b'iVBORw0KGgoAAAANSUhEUgAAABoAAACgCAMAAAAlxYzvAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAFcUExURVQ4R4WoS5W3VqTEYrTTbsPeedHqg931i+T6kdLqgsPgerXTb6XEYpW3V4WpS3aaQGmPNl6GL1Z+KZa3V8PgedHqgsTeebXSbneaQGqPNl+GL6XEY8PeetLqg3ebQJW2V8Tgedz1i6TEY7TSbtLrg4aoS5W2VoapS3abQJa2V5a2Vt3zi1d/Kdzzi7TSb2mPN5a3VsTgesTeerXSb9Lrgl6HL9Hrg1+HL7TTb2qPN931jNPrhNnyid/4j9/4jtjyicnjfcHcd7bUcKzKaKPCYJi5WI6wUYOlSXqfRHCXPGGJMVuELN/2jtPrg8njfrbUb4OnS3qeQ3GWPFuELeH2juH4jtnyiMnlfZi5WYOnSVuDLcnlfsHcdqLCYXGXO2ePNmGIMdPqg8HddrfUcI6vUYSnS3qfQnGWO2KJMVuDLNLrhMHdd6LCYHCWPKPDYWiPNmKIMcrjfXGXPAAAAE+V2F0AAAB0dFJOU/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////8A9nTFawAAAAlwSFlzAAAOwwAADsMBx2+oZAAABBZJREFUWEftVWtz2kYUReiB8K5kWskIV5YFEhIgYifuI6U2wbHdOo+aNukjdt9NWztp+kzz/2d67iLMrjPJp37pDPuJmcPde/bcc48qLypaVTdMq2bX6iuMO+5q4403cQC8qLgeZ34d0Foz0Ktaa/2tBeSEbCMCFPmB7mibUpUWc9aOOrjQZ0mstWTI01OzK6oYqpRejs42COo2Wei4clUWc6MtqtoBz3ur6xLkcMMkGlab6bG72VgwzGLdoAs7dZPxqtuXoQEPfEG+yZKi15IudKs8ba/V7GHkG1wl7xYhE70iM02qJcNrM2gQGj4xtMDQUXr1nNBoQt6taGNb99zW9QU0EwpVXd/Qb/RkDd1Yn/diiZP1AV27ZBgabVzYgRpJrgglegk1zIAPMgUq9KAZDalqm5S/voC0ONze6Q5JDYM76pPjMH2bNIxMIywUb2gDzKvesTtWM0iuGKDQWduiCzcCGECGspwbPnljrfmODrNJNHp5GAg1yBue4g28K6An196djXL9vUtIwyjNm1tEnp68uv7+AvIgFC4cWuYoiRXbQA02M4Cf8lwRCrYBDTCMdgw4SvHGf63G/4DhMhxkeZfhoNBYhsMCWqqhqqEbPtHomoY+UNc8DtkOqjrRSpp4irGXabNMm2XaXEKv2a8e1DC7BPlBeMPdlH044CPTAmSZMLaY1xzSvGSbDACGaThQ1CDbkNnIvTyHbaReDk9NrN5WZGLKWv8D6cKcGNKFZqoXmUIjB0NMuRyl7EPsl9gUGADyurIaLl2IUQpjF8q73Lw0NuQNPeyX1MsLMWVcaPmMg0ZjMZSex9Nyv0YhDCDlRpYnYFizd8m9MZSXGGJe5k0iT0vUU3w4AEPheVJDGYqWJ8Lzw2jFQK++vF9FKS+RV+Wl3CCGpAYiRU62HqpMisp6m4UeRimTx1CEvGYA5fuyUHhyU9gGoUfKS5DDgzK+RnqBNV8IlXkJm5FvG0RDZli+q0O7fBVCigpHwYdettqQPF/KSww5RilXia0UxmZhgSpJqDwZrdCTu2aKKSvK5wlyo2NvwaJJjilLEDZlZmwYQA1zuJeJLxE8D2O35LQp8JES3xTaFIVhz9FHIr6wlYhlORxIXn9tlzbFCHNklDQUxDKtw66FdXAyJcy9MC0jhWwjD4V+vHwAvO6U/3rpANob37In+3u3Dw6PPvzo+M7de437H5dQtD+xT8bTTw4+JejBw88a9z8voen4C/vLR3unVHV2/NVdQF+XUHd8Yk/G02++PTz6jqq+/+HHOfQY0Mmj6PSnn1H1y/nFk8bTX0voGXpNxtHpb4dHv58dn1/80Xg679XdP7FvjZ/dBo0/z44fXDz56+951VQwfPx8Rv784T8LGgfPqdtkf3oFBvSKU6n8C0nsuQ72wU8CAAAAAElFTkSuQmCC'))))

class Pipes:
    pipes = set()

    def __init__(self, pipeup, pipedown):
        self.pipeup = pipeup
        self.pipedown = pipedown
        self.left = 320
        self.topup = random.randint(-270, -90)
        self.topdown = self.topup + 400
        self.vel = 5
        
    def move(self):
        win.blit(self.pipeup, (self.left, self.topup))
        win.blit(self.pipedown, (self.left, self.topdown))
        self.left -= self.vel

    def checkcollision(self, bird):
        global state
        uprect = pygame.Rect((self.left, self.topup), self.pipeup.get_size())
        downrect = pygame.Rect((self.left, self.topdown), self.pipedown.get_size())
        if uprect.colliderect(bird.rect) or downrect.colliderect(bird.rect) or bird.top >= 370:
            Bird.state = 0
        if bird.left == self.left + 45:
            Bird.score += 1

class Bird:
    frames = 0
    score = 0
    state = 1

    def __init__(self, flap1, flap2, flap3):
        self.flap1 = flap1
        self.flap2 = flap2
        self.flap3 = flap3
        self.vert = 0
        self.left = 30
        self.top = 200
        self.rect = None

    def animation(self):
        if Bird.frames < 10:
            win.blit(self.flap1, (self.left, self.top))
            Bird.frames += 1
        elif Bird.frames < 20:
            win.blit(self.flap2, (self.left, self.top))
            Bird.frames += 1
        elif Bird.frames < 30:
            win.blit(self.flap3, (self.left, self.top))
            Bird.frames += 1
        else:
            win.blit(self.flap1, (self.left, self.top))
            Bird.frames = 0
        
        self.rect = pygame.Rect((self.left, self.top), self.flap2.get_size())
        self.top -= self.vert
        self.vert -= 0.5

def draw(bird, text, state):
    win.blit(bg, (0, 0))

    if not Pipes.pipes:
        Pipes.pipes.add(Pipes(pipeup, pipedown))
    else:
        for i in Pipes.pipes.copy():
            i.move()
            i.checkcollision(bird)
            if i.left < -40:
                Pipes.pipes.remove(i)
            if i.left == 50:
                Pipes.pipes.add(Pipes(pipeup, pipedown))

    bird.animation()
    win.blit(grass, (0, 395))
    win.blit(text, (0, 0))
    pygame.display.update()

def drawfail(failtext1, failtext2):
    win.blit(bg, (0, 0))
    win.blit(failtext1, (20, 200))
    win.blit(failtext2, (20, 230))

    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True
    
    font = pygame.font.Font(None, 25)
    failtext2 = font.render(f'SPACE or LEFT CLICK to restart', True, (255, 255, 255))

    state = 1
    bird = Bird(flap1, flap2, flap3)
    while run:
        scoretext = font.render(f'Score: {Bird.score}', True, (255, 255, 255))
        failtext = font.render(f'Gameover! Your score is {Bird.score}', True, (255, 255, 255))
        if Bird.state:
            draw(bird, scoretext, state)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE) or\
                   (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                    bird.vert = 7
        else:
            drawfail(failtext, failtext2)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE) or\
                   (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                    Bird.score = 0
                    Bird.state = 1
                    bird.left = 30
                    bird.top = 200
                    bird.vert = 1
                    Pipes.pipes = set()

        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
