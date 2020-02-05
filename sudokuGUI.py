import pygame
from solver import sudokuSolver

pygame.init()
winsize = 90
winmultiplier = 5
height = winsize * winmultiplier
winoffset = (int(height/3))
width = winsize * winmultiplier + winoffset
squaresize = int(height / 3)
cellsize = int(squaresize / 3)
win = pygame.display.set_mode((width,height))

WHITE = (255,255,255)
BLACK = (0,0,0)
LIGHTGRAY = (200,200,200)

numberfont = pygame.font.SysFont('arial', 20)
instructionfont = pygame.font.SysFont('arial', 20)

solverX = clearerX = int(height + winoffset / 3 / 2)
solverY = int(height / 2)
clearerY = solverY + 2 * cellsize
solveButton = pygame.draw.rect(win, LIGHTGRAY, (solverX, solverY, 2 * cellsize, int(winoffset / 3)))
clearButton = pygame.draw.rect(win, LIGHTGRAY, (solverX, solverY + 2 * cellsize, 2 * cellsize, int(winoffset / 3)))
pygame.display.set_caption("Sudoku Solver")
arr = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0]]



def drawWindow():

    pygame.draw.rect(win, LIGHTGRAY, (solverX, solverY, 2 * cellsize, int(winoffset / 3)))
    pygame.draw.rect(win, LIGHTGRAY, (clearerX, clearerY, 2 * cellsize, int(winoffset / 3)))

    solverButtonX = int((solverX + solverX + 2 * cellsize) / 2)
    solverButtonY = int((solverY + solverY + winoffset / 3) / 2)

    solverText = instructionfont.render("Solve",1,BLACK)
    solverRect = solverText.get_rect()
    solverRect.center = (solverButtonX,solverButtonY)
    win.blit(solverText,solverRect)

    clearerButtonX = int((clearerX + clearerX + 2 * cellsize) / 2)
    clearerButtonY = int((clearerY + clearerY + winoffset / 3) / 2)

    clearerText = instructionfont.render("Clear", 1, BLACK)
    clearerRect = clearerText.get_rect()
    clearerRect.center = (clearerButtonX, clearerButtonY)
    win.blit(clearerText, clearerRect)

    for i in range(0,height,cellsize):
        pygame.draw.line(win,LIGHTGRAY,(i,0),(i,height))
        pygame.draw.line(win,LIGHTGRAY,(0,i),(height,i))
    for j in range(0,width,squaresize):
        pygame.draw.line(win,BLACK,(j,0),(j,height))
        pygame.draw.line(win,BLACK,(0,j),(height,j))

def clearBoard(arr):
    for row in range(len(arr)):
        for col in range(len(arr[0])):
            arr[row][col] = 0

def populateCells(arr):
    celloffset = int(cellsize / 2)
    for row in range(len(arr)):
        for col in range(len(arr[0])):
            if arr[row][col] > 0:
                cell = numberfont.render(str(arr[row][col]),1, BLACK)
                cellRect = cell.get_rect()
                cellRect.center = (celloffset + col * celloffset * 2,celloffset + row * celloffset * 2)
                win.blit(cell, cellRect)

def showselectednumber(value):
    instructions = instructionfont.render('Input Number:',1,BLACK)
    instructionsRect = instructions.get_rect()
    instructionsRect.center = (int(height + winoffset / 2), cellsize)
    win.blit(instructions, instructionsRect)
    if value > 0:
        numbertext = numberfont.render(str(value),1,BLACK)
    else:
        numbertext = numberfont.render('DELETE', 1, BLACK)
    numberRect = numbertext.get_rect()
    numberRect.center = (int(height + winoffset / 2), cellsize * 2)
    win.blit(numbertext,numberRect)

def main():
    run = True
    value = 0

    while run:
        win.fill(WHITE)
        drawWindow()
        populateCells(arr)
        showselectednumber(value)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_0:
                    value = 0
                if event.key == pygame.K_1:
                    value = 1
                if event.key == pygame.K_2:
                    value = 2
                if event.key == pygame.K_3:
                    value = 3
                if event.key == pygame.K_4:
                    value = 4
                if event.key == pygame.K_5:
                    value = 5
                if event.key == pygame.K_6:
                    value = 6
                if event.key == pygame.K_7:
                    value = 7
                if event.key == pygame.K_8:
                    value = 8
                if event.key == pygame.K_9:
                    value = 9
                if event.key == pygame.K_s:
                    sudokuSolver(arr)

            if event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
                y = int(position[0] // (height / 9))
                x = int(position[1] // (height / 9))
                if x < 9 and y < 9:
                    arr[x][y] = value
                elif solveButton.collidepoint(position[0],position[1]):
                    sudokuSolver(arr)
                elif clearButton.collidepoint(position[0],position[1]):
                    clearBoard(arr)

            if event.type == pygame.QUIT:
                run = False
        pygame.display.update()

main()
pygame.quit()

