




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
        self.currmove = None

    def copy(self):
        tmp = Board()
        tmp.board = "HI"


    def addmove(self,move):
        self.currmove = move
        if len(self.lastmoves) >= 8:
            self.lastmoves.pop(obj = self.lastmoves[0])
            self.lastmoves.extend(move)
        else:
            self.lastmoves.extend(move)

    def stalecheck(self):
        samemoves = 0
        if len(self.lastmoves) >= 8:
            
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
        maxmat = 0
        minmat = 0
        if(color == None):
            color = self.currentplayer
        for row in self.board:
            for piece in row:
                if((color == piece.player) and (isinstance(piece,Kpieces.Kpiece))):
                    maxmat += piece.score
                elif(((color != piece.player) and (isinstance(piece,Kpieces.Kpiece)))):
                    minmat += piece.score
        if(self.stalecheck()):
            return 0
        else:
            return maxmat-minmat



    def movepiece(self,fromrank,fromfile,torank,tofile,special = None):
        ftmp = self.board[fromrank][fromfile]
        ttm = self.board[torank][tofile]
        
        if(special == None):#Move/capture
            self.board[fromrank][fromfile] = Kpieces.Empty()
            self.board[torank][tofile] = ftmp
            ftmp.update(torank,tofile)
            self.pretty()
            self.addmove( (str(str(chr(ord("a")+fromfile))+str(8-fromrank))  , str(str(chr(ord("a")+tofile))+str(8-torank)))   )
        elif(special[0] == 1):#Promotion
            self.board[fromrank][fromfile] = Kpieces.Empty()
            Ptmp = Kpieces.Queen(tofile,torank,ftmp.player,"Queen",self)
            self.board[torank][tofile] = Ptmp
            self.pretty()
            self.addmove( (str(str(chr(ord("a")+fromfile))+str(8-fromrank))  , str(str(chr(ord("a")+tofile))+str(8-torank)))   )
        elif(special[0] == 2):#Enpassant
            self.board[fromrank][fromfile] = Kpieces.Empty()
            self.board[special[1]][special[2]] = Kpieces.Empty() 
            self.board[torank][tofile] = ftmp
            ftmp.update(torank,tofile)
            self.pretty()
            self.addmove( (str(str(chr(ord("a")+fromfile))+str(8-fromrank))  , str(str(chr(ord("a")+tofile))+str(8-torank)))   )
        elif(special[0] == 3):#Castling
            Rooktmp = self.board[special[1]][special[2]]
            self.board[fromrank][fromfile] = Kpieces.Empty()
            self.board[special[1]][special[2]] = Kpieces.Empty()
            self.board[torank][tofile] = ftmp
            ftmp.update(torank,tofile)
            self.board[special[3]][special[4]] = Rooktmp
            Rooktmp.update(special[3],special[4])
            self.pretty()
            self.addmove( (str(str(chr(ord("a")+fromfile))+str(8-fromrank))  , str(str(chr(ord("a")+tofile))+str(8-torank)))   )
        


        if self.currentplayer == "White":
            self.currentplayer = "Black"
        elif self.currentplayer == "Black":
            self.currentplayer = "White"
        None

