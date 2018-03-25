




import Kpieces
import copy
class Board:
    def __init__(self):
        self.board = [[Kpieces.Empty() for y in range(8)] for x in range(8)]
        self.blackcastleQ = [False]
        self.blackcastleK = [False]
        self.whitecastleQ = [False]
        self.whitecastleK = [False]
        self.enpassant = ""
        self.prettyenpassant = ""
        self.currentplayer = ""
        self.prettyboard = None
        self.blackking = None
        self.whiteKing = None
        self.enpapiece = None


    def checkpos(self,inrank,infile):
        if((infile <0) or (infile >7) or (inrank <0) or (inrank >7)):
            return None
        return self.board[inrank][infile]

    def pretty(self):
        self.prettyboard = [[y.rep if y.player=="White" else y.rep.lower() for y in x] for x in self.board]
    
    def currentmat(self,color=None):#material cost of all pieces of curent player
        mat = 0
        for row in self.board:
            for piece in row:
                if(self.currentplayer == piece.player):
                    mat += piece.score
        return mat



    def movepiece(self,fromrank,fromfile,torank,tofile,special = None):
        ftmp = self.board[fromrank][fromfile]
        ttm = self.board[torank][tofile]
        NewBoard = copy.deepcopy(self)
        if(special == None):#Move/capture
            NewBoard[fromrank][fromfile] = Kpieces.Empty()
            NewBoard[torank][tofile] = ftmp
            ftmp.update(torank,tofile)
        elif(special[0] == 1):#Promotion
            NewBoard[fromrank][fromfile] = Kpieces.Empty()
            Ptmp = Kpieces.Queen(tofile,torank,ftmp.player,"Queen",NewBoard)
            NewBoard[torank][tofile] = Ptmp
        elif(special[0] == 2):#Enpassant
            NewBoard[fromrank][fromfile] = Kpieces.Empty()
            NewBoard[special[1]][special[2]] = Kpieces.Empty()
            NewBoard[torank][tofile] = ftmp
            ftmp.update(torank,tofile)
        elif(special[0] == 3):#Castling
            Rooktmp = self.board[special[1]][special[2]]
            NewBoard[fromrank][fromfile] = Kpieces.Empty()
            NewBoard[specia[1]][special[2]] = Kpieces.Empty()
            NewBoard[torank][tofile] = ftmp
            ftmp.update(torank,tofile)
            NewBoard[special[3]][special[4]] = Rooktmp
            Rooktmp.update(special[3],special[4])
        return NewBoard



        None

