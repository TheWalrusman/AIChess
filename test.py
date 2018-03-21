import Kboard
import Kpieces




#ourboard = [[0 for y in range(8)] for x in range(8)]
ourboard = Kboard.Board()
Fenstring = "rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq e3 0 1"
Fenstring = Fenstring.split()
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
        filecount += 1
    elif  letter in '/':
        filecount = 0
        rankcount += 1
    elif int(letter) in ilist:
        filecount += int(letter)
for letter in Fenstring[1]:
    current_player = letter
for letter in Fenstring[2]:
    if letter in 'Q':
        whitecastle.append(letter.upper())
        ourboard.whitecastleQ = "Q"
    elif letter in 'K':
        whitecastle.append(letter.upper())
        ourboard.whitecastleK = "K"
    elif letter in 'q':
        blackcastle.append(letter.upper())
        ourboard.blackcastleQ = "Q"
    elif letter in 'k':
        blackcastle.append(letter.upper())
        ourboard.blackcastleK = "K"
for letter in Fenstring[3]:
    enpassant += letter
    ourboard.enpassant += letter
for letter in Fenstring[4]:
    halfmove = int(letter)
for letter in Fenstring[5]:
    fullmove = int(letter)




None