from Graphics import *

# author: Bras Ramos 2020


# global variables
play_board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
points_Circle = 0
points_Crosses = 0


# program starts running here
def main():
    win = GraphWin("Tic-Tac-Toe", 300, 400)
    make_gui(win)
    menu_mouseClick = win.getMouse()

    while True:
        if enterWasClicked(menu_mouseClick):
            win.close()
            enter_win = GraphWin("In-Game", 500, 550)
            makeEnterWind(enter_win)
            break

        elif optionsWasClicked(menu_mouseClick):
            win.close()
            makeOptionsWind()
            break

        else:
            win.close()
            break


# draws main menu GUI on a new window
def make_gui(win):
    """
    """
    # 'ENTER' button
    """
        Draws ENTER button with colour and outline.
    """
    rect_1 = Rectangle(Point(5, 5), Point(295, 120))
    rect_1.setFill("white")
    rect_1.setOutline("black")
    rect_1.setWidth(1.5)
    rect_1.draw(win)

    """
        Draws text inside the ENTER button.
    """
    text_1 = Text(Point(145, 63), "New Game")
    text_1.draw(win)

    # 'OPTIONS' button
    '''
        Draws OPTIONS button with colour and outline.
    '''
    rect_2 = Rectangle(Point(5, 125), Point(295, 245))
    rect_2.setFill("white")
    rect_2.setOutline("black")
    rect_2.setWidth(1.5)
    rect_2.draw(win)

    '''
        Draws text inside the OPTIONS button.
    '''
    text_2 = Text(Point(145, 185), "Options")
    text_2.draw(win)

    # 'EXIT' button
    '''
        Draws EXIT button with colour and outline.
    '''
    rect_3 = Rectangle(Point(5, 250), Point(295, 370))
    rect_3.setFill("white")
    rect_3.setOutline("black")
    rect_3.setWidth(1.5)
    rect_3.draw(win)

    '''
        Draws text inside the EXIT button.
    '''
    text_3 = Text(Point(145, 307), "Exit")
    text_3.draw(win)

    '''
        Draws "Made by: Bras Ramos 2020" on the bottom of window
    '''
    text_4 = Text(Point(105, 385), "Made by: Bras Ramos 2020")
    text_4.draw(win)


# returns True if ENTER button was clicked
def enterWasClicked(mouse):
    xClick = mouse.getX()
    YClick = mouse.getY()
    if 5 < xClick < 295 and 5 < YClick < 120:
        return True


# returns True if OPTIONS button was clicked
def optionsWasClicked(win):
    xClick = win.getX()
    YClick = win.getY()
    if 5 < xClick < 295 and 125 < YClick < 245:
        return True


# resets play board
def resetPlayBoard(enter_win):
    for i in range(3):
        for ii in range(3):
            play_board[i][ii] = 0
    drawEnterWind(enter_win)


# draws ENTER graphics
def drawEnterWind(enter_win):
    clearboard = Rectangle(Point(0, 0), Point(499, 549))
    clearboard.setFill(color_rgb(233, 233, 233))
    clearboard.draw(enter_win)

    scoreCircle = Text(Point(230, 525), str(points_Circle))
    scoreCircle.setTextColor(color_rgb(135, 252, 255))
    scoreCircle.setSize(25)
    scoreCircle.draw(enter_win)
    print("run")

    scoreCross = Text(Point(270, 525), str(points_Crosses))
    scoreCross.setTextColor(color_rgb(167, 135, 255))
    scoreCross.setSize(25)
    scoreCross.draw(enter_win)

    restartButton = Rectangle(Point(425, 510), Point(495, 545))
    restartButton.setFill("white")
    restartButton.draw(enter_win)

    restartText = Text(Point(460, 527), "Restart")
    restartText.setFill("black")
    restartText.draw(enter_win)

    scoreHifen = Text(Point(250, 523), '-')
    scoreHifen.setTextColor("black")
    scoreHifen.setSize(25)
    scoreHifen.draw(enter_win)

    line_1 = Line(Point(166.6, 15), Point(166.6, 485))
    line_1.setWidth(5)
    line_1.draw(enter_win)

    line_2 = Line(Point(333, 15), Point(333, 485))
    line_2.setWidth(5)
    line_2.draw(enter_win)

    line_3 = Line(Point(15, 166.6), Point(485, 166.6))
    line_3.setWidth(5)
    line_3.draw(enter_win)

    line_4 = Line(Point(15, 333), Point(485, 333))
    line_4.setWidth(5)
    line_4.draw(enter_win)


# takes ENTER input and translates to graphics
def makeEnterWind(enter_win):
    global points_Crosses
    global points_Circle

    drawEnterWind(enter_win)

    counter = 1

    while counter <= 10:
        enter_mouseClick = enter_win.getMouse()

        if onFirstSquare(enter_mouseClick) and available(0, 0):
            if isEven(counter):
                cross = Line(Point(40, 40), Point(122.5, 122.5))
                cross_1 = Line(Point(40, 122.5), Point(122.5, 40))
                cross.setOutline(color_rgb(167, 135, 255))
                cross_1.setOutline(color_rgb(167, 135, 255))
                cross.setWidth(3)
                cross_1.setWidth(3)
                cross.draw(enter_win)
                cross_1.draw(enter_win)
                counter += 1
                addPlay(0, 0, 1)
            else:
                circle = Circle(Point(81.25, 81.25), 50)
                circle.setOutline(color_rgb(135, 252, 255))
                circle.setWidth(3)
                circle.draw(enter_win)
                counter += 1
                addPlay(0, 0, 2)

        elif onSecondSquare(enter_mouseClick) and available(0, 1):
            if isEven(counter):
                cross = Line(Point(210.7, 40), Point(293.2, 122.5))
                cross_1 = Line(Point(210, 122.5), Point(293.2, 40))
                cross.setOutline(color_rgb(167, 135, 255))
                cross_1.setOutline(color_rgb(167, 135, 255))
                cross.setWidth(3)
                cross_1.setWidth(3)
                cross.draw(enter_win)
                cross_1.draw(enter_win)
                counter += 1
                addPlay(0, 1, 1)

            else:
                circle = Circle(Point(250, 81.25), 50)
                circle.setOutline(color_rgb(135, 252, 255))
                circle.setWidth(3)
                circle.draw(enter_win)
                counter += 1
                addPlay(0, 1, 2)


        elif onThirdSquare(enter_mouseClick) and available(0, 2):
            if isEven(counter):
                cross = Line(Point(381.4, 40), Point(463.9, 122.5))
                cross_1 = Line(Point(381.4, 122.5), Point(463.9, 40))
                cross.setOutline(color_rgb(167, 135, 255))
                cross_1.setOutline(color_rgb(167, 135, 255))
                cross.setWidth(3)
                cross_1.setWidth(3)
                cross.draw(enter_win)
                cross_1.draw(enter_win)
                counter += 1
                addPlay(0, 2, 1)

            else:
                circle = Circle(Point(418.75, 81.25), 50)
                circle.setOutline(color_rgb(135, 252, 255))
                circle.setWidth(3)
                circle.draw(enter_win)
                counter += 1
                addPlay(0, 2, 2)


        elif onFourthSquare(enter_mouseClick) and available(1, 0):
            if isEven(counter):
                cross = Line(Point(40, 210.7), Point(122.5, 293.2))
                cross_1 = Line(Point(40, 293.2), Point(122.5, 210.7))
                cross.setOutline(color_rgb(167, 135, 255))
                cross_1.setOutline(color_rgb(167, 135, 255))
                cross.setWidth(3)
                cross_1.setWidth(3)
                cross.draw(enter_win)
                cross_1.draw(enter_win)
                counter += 1
                addPlay(1, 0, 1)

            else:
                circle = Circle(Point(81.25, 250), 50)
                circle.setOutline(color_rgb(135, 252, 255))
                circle.setWidth(3)
                circle.draw(enter_win)
                counter += 1
                addPlay(1, 0, 2)


        elif onFifthSquare(enter_mouseClick) and available(1, 1):
            if isEven(counter):
                cross = Line(Point(210.7, 210.7), Point(293.2, 293.2))
                cross_1 = Line(Point(210.7, 293.2), Point(293.2, 210.7))
                cross.setOutline(color_rgb(167, 135, 255))
                cross_1.setOutline(color_rgb(167, 135, 255))
                cross.setWidth(3)
                cross_1.setWidth(3)
                cross.draw(enter_win)
                cross_1.draw(enter_win)
                counter += 1
                addPlay(1, 1, 1)

            else:
                circle = Circle(Point(250, 250), 50)
                circle.setOutline(color_rgb(135, 252, 255))
                circle.setWidth(3)
                circle.draw(enter_win)
                counter += 1
                addPlay(1, 1, 2)


        elif onSixthSquare(enter_mouseClick) and available(1, 2):
            if isEven(counter):
                cross = Line(Point(381.4, 210.7), Point(463.9, 293.2))
                cross_1 = Line(Point(381.4, 293.2), Point(463.9, 210.7))
                cross.setOutline(color_rgb(167, 135, 255))
                cross_1.setOutline(color_rgb(167, 135, 255))
                cross.setWidth(3)
                cross_1.setWidth(3)
                cross.draw(enter_win)
                cross_1.draw(enter_win)
                counter += 1
                addPlay(1, 2, 1)

            else:
                circle = Circle(Point(418.72, 250), 50)
                circle.setOutline(color_rgb(135, 252, 255))
                circle.setWidth(3)
                circle.draw(enter_win)
                counter += 1
                addPlay(1, 2, 2)


        elif onSeventhSquare(enter_mouseClick) and available(2, 0):
            if isEven(counter):
                cross = Line(Point(40, 381.4), Point(122.5, 463.9))
                cross_1 = Line(Point(40, 463.9), Point(122.5, 381.4))
                cross.setOutline(color_rgb(167, 135, 255))
                cross_1.setOutline(color_rgb(167, 135, 255))
                cross.setWidth(3)
                cross_1.setWidth(3)
                cross.draw(enter_win)
                cross_1.draw(enter_win)
                counter += 1
                addPlay(2, 0, 1)

            else:
                circle = Circle(Point(81.25, 418.72), 50)
                circle.setOutline(color_rgb(135, 252, 255))
                circle.setWidth(3)
                circle.draw(enter_win)
                counter += 1
                addPlay(2, 0, 2)


        elif onEigthSquare(enter_mouseClick) and available(2, 1):
            if isEven(counter):
                cross = Line(Point(210.7, 381.4), Point(293.2, 463.9))
                cross_1 = Line(Point(210.7, 463.9), Point(293.2, 381.4))
                cross.setOutline(color_rgb(167, 135, 255))
                cross_1.setOutline(color_rgb(167, 135, 255))
                cross.setWidth(3)
                cross_1.setWidth(3)
                cross.draw(enter_win)
                cross_1.draw(enter_win)
                counter += 1
                addPlay(2, 1, 1)

            else:
                circle = Circle(Point(250, 418.72), 50)
                circle.setOutline(color_rgb(135, 252, 255))
                circle.setWidth(3)
                circle.draw(enter_win)
                counter += 1
                addPlay(2, 1, 2)


        elif onNinethSquare(enter_mouseClick) and available(2, 2):
            if isEven(counter):
                cross = Line(Point(381.4, 381.4), Point(463.9, 463.9))
                cross_1 = Line(Point(381.4, 463.9), Point(463.9, 381.4))
                cross.setOutline(color_rgb(167, 135, 255))
                cross_1.setOutline(color_rgb(167, 135, 255))
                cross.setWidth(3)
                cross_1.setWidth(3)
                cross.draw(enter_win)
                cross_1.draw(enter_win)
                counter += 1
                addPlay(2, 2, 1)

            else:
                circle = Circle(Point(418.72, 418.72), 50)
                circle.setOutline(color_rgb(135, 252, 255))
                circle.setWidth(3)
                circle.draw(enter_win)
                counter += 1
                addPlay(2, 2, 2)

        elif onRestartButton(enter_mouseClick):
            points_Crosses = 0
            points_Circle = 0
            drawEnterWind(enter_win)

        else:
            print("Choose a valid square.")

        if isWin():
            # print("Winner - " + getWinner())
            wonAlert = Rectangle(Point(130, 230), Point(370, 270))
            wonAlert.setFill("white")
            wonAlert.draw(enter_win)

            if getWinner() == "crosses":
                pointAddedCrosses = Text(Point(250, 250), "+1 Point for Crosses")
                pointAddedCrosses.setTextColor(color_rgb(167, 135, 255))
                pointAddedCrosses.draw(enter_win)
                points_Crosses += 1
            elif getWinner() == "circles":
                pointAddedCircles = Text(Point(250, 250), "+1 Point for Circles")
                pointAddedCircles.setTextColor(color_rgb(135, 252, 255))
                pointAddedCircles.draw(enter_win)
                points_Circle += 1

            time.sleep(2.5)
            resetPlayBoard(enter_win)
            makeEnterWind(enter_win)


        elif (counter == 10) and (isWin() == False):
            tieAlert = Rectangle(Point(130, 230), Point(370, 270))
            tieAlert.setFill("white")
            tieAlert.draw(enter_win)

            tieAlertText = Text(Point(250, 250), "Tied, no Points awarded")
            tieAlertText.setTextColor("red")
            tieAlertText.draw(enter_win)

            time.sleep(2.5)
            resetPlayBoard(enter_win)
            makeEnterWind(enter_win)


# draws OPTIONS graphics
def makeOptionsWind():
    options_win = GraphWin("In-Settings", 300, 300)

    options_win.getMouse()
    options_win.close()


# returns True if position in board is empty
def available(column, row):
    return play_board[column][row] == 0


# checks if there is a win, in that case returns True
def isWin():
    if (isHorizontalWin() or isVerticalWin() or isDiagonalWin()):
        return True
    else:
        return False


# checks if its an horizontal win
def isHorizontalWin():
    isWin = False

    for i in range(3):
        if play_board[i][0] == play_board[i][1] and play_board[i][1] == play_board[i][2] and play_board[i][0] != 0:
            isWin = True

    return isWin


# checks if its a vertical win
def isVerticalWin():
    isWin = False

    for i in range(3):
        if play_board[0][i] == play_board[1][i] and play_board[1][i] == play_board[2][i] and play_board[0][i] != 0:
            isWin = True

    return isWin


# checks if its a diagonal win
def isDiagonalWin():
    isWin = False

    if (play_board[0][0] != 0 and play_board[0][0] == play_board[1][1] and play_board[1][1] == play_board[2][2]) \
            or (
            play_board[2][0] != 0 and play_board[2][0] == play_board[1][1] and play_board[1][1] == play_board[0][2]):
        isWin = True

    return isWin


# returns which side won
def getWinner():
    for i in range(3):
        if play_board[i][0] == play_board[i][1] and play_board[i][1] == play_board[i][2] and play_board[i][0] != 0:
            winner = play_board[i][0]
            return winTranslate(winner)

    for i in range(3):
        if play_board[0][i] == play_board[1][i] and play_board[1][i] == play_board[2][i] and play_board[0][i] != 0:
            winner = play_board[0][i]
            return winTranslate(winner)

    if (play_board[0][0] == play_board[1][1] and play_board[1][1] == play_board[2][2]) or (
            play_board[2][0] == play_board[1][1] and play_board[1][1] == play_board[0][2]):
        winner = play_board[1][1]
        return winTranslate(winner)


# translates win position to winning person
def winTranslate(win):
    x = "crosses"
    o = "circles"

    if win == 1:
        return x
    elif win == 2:
        return o


# adds play to board
def addPlay(column, row, type):
    play_board[column][row] = type


# tells if given number is even
def isEven(number):
    x = number % 2
    even = False
    if x == 0:
        even = True
    return even


# returns True if click was on First square
def onFirstSquare(mouse):
    x = mouse.getX()
    y = mouse.getY()

    if 0 < x < 166 and 0 < y < 166:
        return True
    else:
        return False


# returns True if click was on Second square
def onSecondSquare(mouse):
    x = mouse.getX()
    y = mouse.getY()

    if 166 < x < 332 and 0 < y < 166:
        return True
    else:
        return False


# returns True if click was on Third square
def onThirdSquare(mouse):
    x = mouse.getX()
    y = mouse.getY()

    if 332 < x < 500 and 0 < y < 166:
        return True
    else:
        return False


# returns True if click was on Fourth square
def onFourthSquare(mouse):
    x = mouse.getX()
    y = mouse.getY()

    if 0 < x < 166 and 166 < y < 332:
        return True
    else:
        return False


# returns True if click was on Fifth square
def onFifthSquare(mouse):
    x = mouse.getX()
    y = mouse.getY()

    if 166 < x < 332 and 166 < y < 332:
        return True
    else:
        return False


# returns True if click was on Sixth square
def onSixthSquare(mouse):
    x = mouse.getX()
    y = mouse.getY()

    if 332 < x < 500 and 166 < y < 332:
        return True
    else:
        return False


# returns True if click was on Seventh square
def onSeventhSquare(mouse):
    x = mouse.getX()
    y = mouse.getY()

    if 0 < x < 166 and 332 < y < 500:
        return True
    else:
        return False


# returns True if click was on Eigth square
def onEigthSquare(mouse):
    x = mouse.getX()
    y = mouse.getY()

    if 166 < x < 332 and 332 < y < 500:
        return True
    else:
        return False


# returns True if click was on Nineth square
def onNinethSquare(mouse):
    x = mouse.getX()
    y = mouse.getY()

    if 332 < x < 500 and 332 < y < 500:
        return True
    else:
        return False


# returns True if click was on Restart Button
def onRestartButton(mouse):
    x = mouse.getX()
    y = mouse.getY()

    if 425 < x < 495 and 510 < y < 545:
        return True
    else:
        return False


main()
