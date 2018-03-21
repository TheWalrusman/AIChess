

import Kboard


class Kpiece:
    def __init__(self,inrank,infile,player,board):
        self.rank = inrank
        self.truerank = 8-inrank
        self.file = infile
        self.truefile = chr(ord('a')+infile)
        self.player = player
        self.currentboard = board
    





class Pawn(Kpiece):
    def __init__(self,inrank,infile,player,intype,board):
        Kpiece.__init__(self,inrank,infile,player,board)
        self.type = intype



    def actions(self):
        possiblemovesforoutput = []
        possiblemovessimple = []
        if(self.player == "White"):
            if(self.rank == 1):
                #checkforcheck
                if(type(self.currentboard.checkpos(self.rank,self.file+2)) != Kpiece):
                    possiblemovesforoutput.append("White Pawn from "+self.truefile+self.truerank +"to "+ chr(self.truefile)+(self.truerank+2))
            if(type(self.currentboard.checkpos(self.rank,self.file+2)) == Kpiece):
                possiblemovesforoutput.append("White Pawn from "+self.truefile+self.truerank +"to "+ chr(self.truefile)+(self.truerank+2))









class Bishop(Kpiece):
    def __init__(self,inrank,infile,player,intype,board):
        Kpiece.__init__(self,inrank,infile,player,board)
        self.type = intype

class Rook(Kpiece):
    def __init__(self,inrank,infile,player,intype,board):
        Kpiece.__init__(self,inrank,infile,player,board)
        self.type = intype

class Knight(Kpiece):
    def __init__(self,inrank,infile,player,intype,board):
        Kpiece.__init__(self,inrank,infile,player,board)
        self.type = intype
class Queen(Kpiece):
    def __init__(self,inrank,infile,player,intype,board):
        Kpiece.__init__(self,inrank,infile,player,board)
        self.type = intype

class King(Kpiece):
    def __init__(self,inrank,infile,player,intype,board):
        Kpiece.__init__(self,inrank,infile,player,board)
        self.type = intype