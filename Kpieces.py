

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
            if(self.rank == 6):
                #checkforcheck
                if((not isinstance(self.currentboard.checkpos(self.rank-2,self.file),Kpiece)) and (not isinstance(self.currentboard.checkpos(self.rank-1,self.file),Kpiece)) and (self.currentboard.checkpos(self.rank-2,self.file) != None)):
                    possiblemovesforoutput.append("White Pawn from "+self.truefile+str(self.truerank) +" to "+ (self.truefile)+str(self.truerank+2))
                    newenpassant = (self.rank-1,self.file,self.truefile+str(self.truerank+1))
                    None

            if(not isinstance(self.currentboard.checkpos(self.rank-1,self.file),Kpiece)  and (self.currentboard.checkpos(self.rank-1,self.file) != None)):
                possiblemovesforoutput.append("White Pawn from "+self.truefile+str(self.truerank) +" to "+ (self.truefile)+str(self.truerank+1))

            if(isinstance(self.currentboard.checkpos(self.rank-1,self.file-1),Kpiece)  and (self.currentboard.checkpos(self.rank-1,self.file-1) != None)and (self.player != self.currentboard.checkpos(self.rank-1,self.file-1).player)):
                possiblemovesforoutput.append("White Pawn from "+self.truefile+str(self.truerank) +" to "+ chr(ord(self.truefile)-1)+str(self.truerank+1))

            if(isinstance(self.currentboard.checkpos(self.rank-1,self.file+1),Kpiece)  and (self.currentboard.checkpos(self.rank-1,self.file+1) != None)and (self.player != self.currentboard.checkpos(self.rank-1,self.file+1).player)):
                possiblemovesforoutput.append("White Pawn from "+self.truefile+str(self.truerank) +" to "+ chr(ord(self.truefile)+1)+str(self.truerank+1))

        elif(self.player == "Black"):
            if(self.rank == 1):
                #checkforcheck
                if(not isinstance(self.currentboard.checkpos(self.rank+2,self.file),Kpiece)and (not isinstance(self.currentboard.checkpos(self.rank+1,self.file),Kpiece)) and (self.currentboard.checkpos(self.rank+2,self.file) != None)):
                    possiblemovesforoutput.append(str("Black Pawn from "+self.truefile+str(self.truerank) +" to "+ (self.truefile)+str(self.truerank-2)))
                    newenpassant = (self.rank+1,self.file,self.truefile+str(self.truerank-1))
                    None

            if(not isinstance(self.currentboard.checkpos(self.rank+1,self.file),Kpiece)  and (self.currentboard.checkpos(self.rank+1,self.file) != None)):
                possiblemovesforoutput.append("Black Pawn from "+self.truefile+str(self.truerank) +" to "+ (self.truefile)+str(self.truerank-1))

            if(isinstance(self.currentboard.checkpos(self.rank+1,self.file-1),Kpiece)  and (self.currentboard.checkpos(self.rank+1,self.file-1) != None)and (self.player != self.currentboard.checkpos(self.rank+1,self.file-1).player)):
                possiblemovesforoutput.append("Black Pawn from "+self.truefile+str(self.truerank) +" to "+ chr(ord(self.truefile)-1)+str(self.truerank-1))

            if(isinstance(self.currentboard.checkpos(self.rank+1,self.file+1),Kpiece)  and (self.currentboard.checkpos(self.rank+1,self.file+1) != None)and (self.player != self.currentboard.checkpos(self.rank+1,self.file+1).player)):
                possiblemovesforoutput.append("Black Pawn from "+self.truefile+str(self.truerank) +" to "+ chr(ord(self.truefile)+1)+str(self.truerank-1))

        None
        return possiblemovesforoutput









class Bishop(Kpiece):
    def __init__(self,inrank,infile,player,intype,board):
        Kpiece.__init__(self,inrank,infile,player,board)
        self.type = intype
        self.movements = [(1,1),(1,-1),(-1,1),(-1,-1)]


    def actions(self):
        possiblemovesforoutput = []
        possiblemovessimple = []
        newmove = self.movements[:]
        for pair in newmove:
            Brank = pair[0]
            Bfile = pair[1]
            while (not isinstance(self.currentboard.checkpos(self.rank+Brank,self.file+Bfile),Kpiece))  and (self.currentboard.checkpos(self.rank+Brank,self.file+Bfile) != None):
                possiblemovesforoutput.append(  self.player + " "+ self.type +" from " +self.truefile+str(self.truerank)+ " to "+ chr(ord(self.truefile)+Bfile)+str(self.truerank-Brank)  )
                Brank += pair[0]
                Bfile += pair[1]

            else:
                if ((isinstance(self.currentboard.checkpos(self.rank+Brank,self.file+Bfile),Kpiece))  and (self.currentboard.checkpos(self.rank+Brank,self.file+Bfile) != None) and (self.player != self.currentboard.checkpos(self.rank+Brank,self.file+Bfile).player)):
                    possiblemovesforoutput.append(  self.player + " "+ self.type +" from " +self.truefile+str(self.truerank)+ " to "+ chr(ord(self.truefile)+Bfile)+str(self.truerank-Brank)  )
                    None
                None




class Rook(Kpiece):
    def __init__(self,inrank,infile,player,intype,board):
        Kpiece.__init__(self,inrank,infile,player,board)
        self.type = intype
        self.movements = [(1,0),(-1,0),(0,1),(0,-1)]

    def actions(self):
        possiblemovesforoutput = []
        possiblemovessimple = []
        newmove = self.movements[:]
        for pair in newmove:
            Brank = pair[0]
            Bfile = pair[1]
            while (not isinstance(self.currentboard.checkpos(self.rank+Brank,self.file+Bfile),Kpiece))  and (self.currentboard.checkpos(self.rank+Brank,self.file+Bfile) != None):
                possiblemovesforoutput.append(  self.player + " "+ self.type +" from " +self.truefile+str(self.truerank)+ " to "+ chr(ord(self.truefile)+Bfile)+str(self.truerank-Brank)  )
                Brank += pair[0]
                Bfile += pair[1]

            else:
                if ((isinstance(self.currentboard.checkpos(self.rank+Brank,self.file+Bfile),Kpiece))  and (self.currentboard.checkpos(self.rank+Brank,self.file+Bfile) != None) and (self.player != self.currentboard.checkpos(self.rank+Brank,self.file+Bfile).player)):
                    possiblemovesforoutput.append(  self.player + " "+ self.type +" from " +self.truefile+str(self.truerank)+ " to "+ chr(ord(self.truefile)+Bfile)+str(self.truerank-Brank)  )
                    None
                None

class Knight(Kpiece):
    def __init__(self,inrank,infile,player,intype,board):
        Kpiece.__init__(self,inrank,infile,player,board)
        self.type = intype
        self.movements = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(-1,2),(1,-2),(-1,-2)]

    def actions(self):
        possiblemovesforoutput = []
        possiblemovessimple = []
        newmove = self.movements[:]
        for pair in newmove:
            Brank = pair[0]
            Bfile = pair[1]
            if (not isinstance(self.currentboard.checkpos(self.rank+Brank,self.file+Bfile),Kpiece))  and (self.currentboard.checkpos(self.rank+Brank,self.file+Bfile) != None):
                possiblemovesforoutput.append(  self.player + " "+ self.type +" from " +self.truefile+str(self.truerank)+ " to "+ chr(ord(self.truefile)+Bfile)+str(self.truerank-Brank)  )
                None

            else:
                if ((isinstance(self.currentboard.checkpos(self.rank+Brank,self.file+Bfile),Kpiece))  and (self.currentboard.checkpos(self.rank+Brank,self.file+Bfile) != None) and (self.player != self.currentboard.checkpos(self.rank+Brank,self.file+Bfile).player)):
                    possiblemovesforoutput.append(  self.player + " "+ self.type +" from " +self.truefile+str(self.truerank)+ " to "+ chr(ord(self.truefile)+Bfile)+str(self.truerank-Brank)  )
                    None
                None


class Queen(Kpiece):
    def __init__(self,inrank,infile,player,intype,board):
        Kpiece.__init__(self,inrank,infile,player,board)
        self.type = intype
        self.movements = [(1,1),(1,-1),(-1,1),(-1,-1),(1,0),(-1,0),(0,1),(0,-1)]

    def actions(self):
        possiblemovesforoutput = []
        possiblemovessimple = []
        newmove = self.movements[:]
        for pair in newmove:
            Brank = pair[0]
            Bfile = pair[1]
            while (not isinstance(self.currentboard.checkpos(self.rank+Brank,self.file+Bfile),Kpiece))  and (self.currentboard.checkpos(self.rank+Brank,self.file+Bfile) != None):
                possiblemovesforoutput.append(  self.player + " "+ self.type +" from " +self.truefile+str(self.truerank)+ " to "+ chr(ord(self.truefile)+Bfile)+str(self.truerank-Brank)  )
                Brank += pair[0]
                Bfile += pair[1]

            else:
                if ((isinstance(self.currentboard.checkpos(self.rank+Brank,self.file+Bfile),Kpiece))  and (self.currentboard.checkpos(self.rank+Brank,self.file+Bfile) != None) and (self.player != self.currentboard.checkpos(self.rank+Brank,self.file+Bfile).player)):
                    possiblemovesforoutput.append(  self.player + " "+ self.type +" from " +self.truefile+str(self.truerank)+ " to "+ chr(ord(self.truefile)+Bfile)+str(self.truerank-Brank)  )
                    None
                None



class King(Kpiece):
    def __init__(self,inrank,infile,player,intype,board):
        Kpiece.__init__(self,inrank,infile,player,board)
        self.type = intype
        self.movements = [(1,1),(1,-1),(-1,1),(-1,-1),(1,0),(-1,0),(0,1),(0,-1)]


    def actions(self):
        possiblemovesforoutput = []
        possiblemovessimple = []
        newmove = self.movements[:]
        for pair in newmove:
            Brank = pair[0]
            Bfile = pair[1]
            if (not isinstance(self.currentboard.checkpos(self.rank+Brank,self.file+Bfile),Kpiece))  and (self.currentboard.checkpos(self.rank+Brank,self.file+Bfile) != None):
                possiblemovesforoutput.append(  self.player + " "+ self.type +" from " +self.truefile+str(self.truerank)+ " to "+ chr(ord(self.truefile)+Bfile)+str(self.truerank-Brank)  )
                None

            else:
                if ((isinstance(self.currentboard.checkpos(self.rank+Brank,self.file+Bfile),Kpiece))  and (self.currentboard.checkpos(self.rank+Brank,self.file+Bfile) != None) and (self.player != self.currentboard.checkpos(self.rank+Brank,self.file+Bfile).player)):
                    possiblemovesforoutput.append(  self.player + " "+ self.type +" from " +self.truefile+str(self.truerank)+ " to "+ chr(ord(self.truefile)+Bfile)+str(self.truerank-Brank)  )
                    None
                None