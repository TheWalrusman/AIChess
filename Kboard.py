




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
        self.lastmoves = []

    def stalecheck(self,mset):
        if len(self.lastmoves == 8):
            self.lastmoves.pop(obj = self.lastmoves[0])
            self.lastmoves.append(mset)
        else:
            self.lastmoves.append(mset)
        if len(self.lastmoves) >= 8:
            samemoves = 0
            for x in range(0,4,1):
                if(self.lastmoves[x] == self.lastmoves[x+4]):
                    samemoves += 1
        if samemoves == 4:
            return True
        else:
            return False


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
        
        if(special == None):#Move/capture
            self.board[fromrank][fromfile] = Kpieces.Empty()
            self.board[torank][tofile] = ftmp
            ftmp.update(torank,tofile)
        elif(special[0] == 1):#Promotion
            self.board[fromrank][fromfile] = Kpieces.Empty()
            Ptmp = Kpieces.Queen(tofile,torank,ftmp.player,"Queen",self)
            self.board[torank][tofile] = Ptmp
        elif(special[0] == 2):#Enpassant
            self.board[fromrank][fromfile] = Kpieces.Empty()
            self.board[special[1]][special[2]] = Kpieces.Empty() 
            self.board[torank][tofile] = ftmp
            ftmp.update(torank,tofile)
        elif(special[0] == 3):#Castling
            Rooktmp = self.board[special[1]][special[2]]
            self.board[fromrank][fromfile] = Kpieces.Empty()
            self.board[special[1]][special[2]] = Kpieces.Empty()
            self.board[torank][tofile] = ftmp
            ftmp.update(torank,tofile)
            self.board[special[3]][special[4]] = Rooktmp
            Rooktmp.update(special[3],special[4])
        



        None

