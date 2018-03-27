import Kboard
import Kpieces
import copy
import BuildFEN
import time
import MiniMax




#ourboard = [[0 for y in range(8)] for x in range(8)]
ourboard = Kboard.Board()
Fenstrings = "rnbqkbnr/2pppppp/p7/1p7/4P3/8/PPPP1PPP/RNBQKBNR b KQkq e3 0 1"
Fenstrings = "r3k2r/pppppppp/2bq1bn1/8/8/N1Bn1BN1/PPPPPPPP/R1Q1K2R w KQkq - 0 1"
Fenstrings = Fenstrings.split()
rankcount = 0
filecount = 0
ilist = [0,1,2,3,4,5,6,7,8]
whitecastle = []
blackcastle = []
enpassant = ""
halfmove = 0
fullmove = 0
#BigList = [BuildFEN.start() for x in range(0,200,1)]
#for x in range(0,100,1):
    #BigList.append(BuildFEN.generate_board())
#XDDD = BuildFEN.generate_board()
##BigList2 = [BuildFEN.start(x) for x in BigList]

tlist = ["n1N4R/3kPBn1/1qp3Qr/1pB1K1P1/PPP1p3/p2p3r/RpPNpPpP/4bb2 w - - 0 1","8/Ppp2Bp1/PB3p2/K2ppk2/bQP1nPn1/PpPRr3/1P1RpNPr/b2N2q1 w - - 0 1","1k1B1b1n/1PrPp1Qp/qrp2pb1/1pn4p/NKR4p/RPPP1B1P/P1p1P3/2N5 w - - 0 1","6N1/1Pn1P1N1/1rq1Qp1P/1PPpppp1/1Rpn3r/kP2bbPR/2B1p1Pp/B3K3 w - - 0 1"]
basicl = ["rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR b KQkq - 0 1"]
tstarttime =time.perf_counter()
for Fenstring in tlist:
    Fenstring = Fenstring.split()
    ourboard = Kboard.Board()
    rankcount = 0
    filecount = 0
    ilist = [0,1,2,3,4,5,6,7,8]
    whitecastle = []
    blackcastle = []
    enpassant = ""
    halfmove = 0
    fullmove = 0
    for letter in Fenstring[0]:
        None 
        if letter in 'p':
            ourboard.board[rankcount][filecount] = Kpieces.Pawn(rankcount,filecount,"Black","Pawn",ourboard)
            filecount += 1
        elif  letter in 'b':
            ourboard.board[rankcount][filecount] = Kpieces.Bishop(rankcount,filecount,"Black","Bishop",ourboard)
            filecount += 1
        elif  letter in 'r':
            ourboard.board[rankcount][filecount] = Kpieces.Rook(rankcount,filecount,"Black","Rook",ourboard)
            filecount += 1
        elif  letter in 'n':
            ourboard.board[rankcount][filecount] = Kpieces.Knight(rankcount,filecount,"Black","Knight",ourboard)
            filecount += 1
        elif  letter in 'q':
            ourboard.board[rankcount][filecount] = Kpieces.Queen(rankcount,filecount,"Black","Queen",ourboard)
            filecount += 1
        elif  letter in 'k':
            ourboard.board[rankcount][filecount] = Kpieces.King(rankcount,filecount,"Black","King",ourboard)
            ourboard.blackking = ourboard.board[rankcount][filecount]
            filecount += 1
        elif letter in 'P':
            ourboard.board[rankcount][filecount] = Kpieces.Pawn(rankcount,filecount,"White","Pawn",ourboard)
            filecount += 1
        elif  letter in 'B':
            ourboard.board[rankcount][filecount] = Kpieces.Bishop(rankcount,filecount,"White","Bishop",ourboard)
            filecount += 1
        elif  letter in 'R':
            ourboard.board[rankcount][filecount] = Kpieces.Rook(rankcount,filecount,"White","Rook",ourboard)
            filecount += 1
        elif  letter in 'N':
            ourboard.board[rankcount][filecount] = Kpieces.Knight(rankcount,filecount,"White","Knight",ourboard)
            filecount += 1
        elif  letter in 'Q':
            ourboard.board[rankcount][filecount] = Kpieces.Queen(rankcount,filecount,"White","Queen",ourboard)
            filecount += 1
        elif  letter in 'K':
            ourboard.board[rankcount][filecount] = Kpieces.King(rankcount,filecount,"White","King",ourboard)
            ourboard.whiteKing = ourboard.board[rankcount][filecount]
            filecount += 1
        elif  letter in '/':
            filecount = 0
            rankcount += 1
        elif int(letter) in ilist:
            filecount += int(letter)
    for letter in Fenstring[1]:
        current_player = letter
        if(letter == 'w'):
            ourboard.currentplayer = "White"
        elif(letter == "b"):
            ourboard.currentplayer = "Black"
    for letter in Fenstring[2]:
        if letter in 'Q':
            whitecastle.append(letter.upper())
            ourboard.whitecastleQ = [True]
            ourboard.board[7][0].moved = ourboard.whitecastleQ
        elif letter in 'K':
            whitecastle.append(letter.upper())
            ourboard.whitecastleK = [True]
            ourboard.board[7][7].moved = ourboard.whitecastleK
        elif letter in 'q':
            blackcastle.append(letter.upper())
            ourboard.blackcastleQ = [True]
            ourboard.board[0][0].moved = ourboard.blackcastleQ
        elif letter in 'k':
            blackcastle.append(letter.upper())
            ourboard.blackcastleK = [True]
            ourboard.board[0][7].moved = ourboard.blackcastleK
    #for letter in Fenstring[3]:
    if Fenstring[3] == '-':
        ourboard.enpassant += letter
    else:
        letter = Fenstring[3]
        enpassant += letter
        ourboard.enpassant += letter
        splitenp = list(letter)
        testl = [(ord(x)-97) for x in ['a',"b","c","d","e","f","g","h"]]
        if(ourboard.currentplayer == "White"):
            trank = 8-int(splitenp[1])+1
            tfile = (ord(splitenp[0])-97)
            ourboard.enpapiece = ourboard.board[trank][tfile]
        if(ourboard.currentplayer == "Black"):
            trank = 8-int(splitenp[1])-1
            tfile = (ord(splitenp[0])-97)
            ourboard.enpapiece = ourboard.board[trank][tfile]
        None
    for letter in Fenstring[4]:
        halfmove = int(letter)
    for letter in Fenstring[5]:
        fullmove = int(letter)

    newboard = copy.deepcopy(ourboard)
    newboard.board[0][0].player = "HIIIIIII"
    newboard.blackcastleQ = "flase"
    ourboard.pretty()
    new_boards = []
    #ourboard.whitecastleQ[0] = "HIIIIIIII"
    starttime =time.perf_counter()

    #minimax(ourboard,1,True)



    #for color in ["White","Black"]:
    for rows in ourboard.board:
        for piece in rows:
            if(isinstance(piece,Kpieces.Kpiece) and (piece.player == ourboard.currentplayer)):
                new_boards.extend( piece.actions())
                None
    None
    startFEN = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
    #endresult = MiniMax()


    endtime = time.perf_counter()
    finish = endtime-starttime
    print(finish)
tendtime = time.perf_counter()
tfinish = tendtime-tstarttime
print(tfinish)
None