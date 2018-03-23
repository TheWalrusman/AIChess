

import Kboard
import random



class Empty:
    def __init__(self):
        self.rank = None
        self.truerank = None
        self.file = None
        self.truefile = None
        self.player = None
        self.currentboard = None
        self.rep = "0"
        None

class Kpiece:
    def __init__(self,inrank,infile,player,board):
        self.rank = inrank
        self.truerank = 8-inrank
        self.file = infile
        self.truefile = chr(ord('a')+infile)
        self.player = player
        self.currentboard = board
        self.capablePs=(Pawn,Knight,Bishop,Rook,Queen)
        


    def checkcheck(self,torank,tofile):
        savedpiece = self.currentboard.board[torank][tofile]
        self.currentboard.board[torank][tofile] = self
        oldrank = self.rank
        oldfile = self.file
        self.rank = torank
        self.file = tofile
        self.currentboard.board[self.rank][self.file] = Empty()
        self.currentboard.pretty()
        #pmoves = [(-1,-1),(-1,1)]
        nmoves = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(-1,2),(1,-2),(-1,-2)]#knight Moves
        qbmoves = [(1,1),(1,-1),(-1,1),(-1,-1)]#queen and bishop
        qrmoves = [(1,0),(-1,0),(0,1),(0,-1)]#queen and rook
        if(self.currentboard.currentplayer == "White"):
            King = self.currentboard.whiteKing
            playerside = 1
            pmoves = [(-1,-1),(-1,1)]
            None
        if(self.currentboard.currentplayer == "Black"):
            King = self.currentboard.blackking
            playerside = -1
            pmoves = [(1,1),(1,-1)]
            None

        #not isinstance(self.currentboard.checkpos(self.rank+Brank,self.file+Bfile),Kpiece))

        for p in pmoves:
            None
            if(isinstance(self.currentboard.checkpos(King.rank+(p[0]),King.file+(p[1])),Pawn)) and (self.currentboard.board[King.rank+(p[0])][King.file+(p[1])].player not in [self.player,None]):
                self.currentboard.pretty()
                self.currentboard.board[torank][tofile] = savedpiece
                self.currentboard.board[self.rank][self.file] = self
                self.rank = oldrank
                self.file = oldfile
                self.currentboard.pretty()
                return True
        for n in nmoves:
            None
            if( (isinstance(self.currentboard.checkpos(King.rank+n[0],King.file+n[1]),Knight))  and (self.currentboard.board[King.rank+n[0]][King.file+n[1]].player not in [self.player,None])  ):
                self.currentboard.pretty()
                self.currentboard.board[torank][tofile] = savedpiece
                self.currentboard.board[self.rank][self.file] = self
                self.rank = oldrank
                self.file = oldfile
                self.currentboard.pretty()
                return True
        for qb in qbmoves:
            None
            incrank = qb[0]
            incfile = qb[1]
            while( (not isinstance(self.currentboard.checkpos(King.rank+incrank,King.file+incfile),Kpiece)) and (self.currentboard.checkpos(King.rank+incrank,King.file+incfile) != None) ):
                incrank += qb[0]
                incfile += qb[1]
            else:
                if(  (isinstance(self.currentboard.checkpos(King.rank+incrank,King.file+incfile),(Queen,Bishop))) and  (self.currentboard.checkpos(King.rank+incrank,King.file+incfile) != None) and (self.currentboard.board[King.rank+incrank][King.file+incfile].player not in [self.player,None])  ):
                    self.currentboard.pretty()
                    self.currentboard.board[torank][tofile] = savedpiece
                    self.currentboard.board[self.rank][self.file] = self
                    self.rank = oldrank
                    self.file = oldfile
                    self.currentboard.pretty()
                    return True
        for qr in qrmoves:
            None
            incrank = qr[0]
            incfile = qr[1]
            while( (not isinstance(self.currentboard.checkpos(King.rank+incrank,King.file+incfile),Kpiece)) and (self.currentboard.checkpos(King.rank+incrank,King.file+incfile) != None) ):
                incrank += qr[0]
                incfile += qr[1]
            else:
                if(  (isinstance(self.currentboard.checkpos(King.rank+incrank,King.file+incfile),(Queen,Rook))) and  (self.currentboard.checkpos(King.rank+incrank,King.file+incfile) != None) and (self.currentboard.board[King.rank+incrank][King.file+incfile].player not in [self.player,None])  ):
                    self.currentboard.pretty()
                    self.currentboard.board[torank][tofile] = savedpiece
                    self.currentboard.board[self.rank][self.file] = self
                    self.rank = oldrank
                    self.file = oldfile
                    self.currentboard.pretty()
                    return True
        self.currentboard.pretty()
        self.currentboard.board[torank][tofile] = savedpiece
        self.currentboard.board[self.rank][self.file] = self
        self.rank = oldrank
        self.file = oldfile
        self.currentboard.pretty()
        return False
        #def undo(self,Old,New,board):
            #board.board[Old.rank][Old.file] = New
            #board.board[New.rank][New.file] = New


        None

    def movep(self,fromrank,fromfile,torank,tofile,special=None):
        if(special == None ):
            None
            self.currentboard.board[torank][tofile] = self
            self.currentboard.board[fromrank][fromfile] = Empty()
        elif(special == 1):#empassant capture
            None
            self.currentboard.board[torank][tofile] = self
            self.currentboard.board[fromrank][fromfile] = Empty()


        None


class Pawn(Kpiece):
    def __init__(self,inrank,infile,player,intype,board):
        Kpiece.__init__(self,inrank,infile,player,board)
        self.type = intype
        self.possiblepromotes = ["Queen","Knight","Rook","Bishop",]
        self.rep = "P"
        self.score = 1
        

    def checkpromote(self,rank,file):
        if (self.currentboard.currentplayer == "White") and (rank == 0):
            return True
        elif(self.currentboard.currentplayer == "Black") and (rank == 7):
            return True
        else:
            return False


    def actions(self):
        possiblemovesforoutput = []
        possiblemovessimple = []
        if(self.player == "White"):
            if(self.rank == 6):
                #checkforcheck
                if((not isinstance(self.currentboard.checkpos(self.rank-2,self.file),Kpiece)) and (not isinstance(self.currentboard.checkpos(self.rank-1,self.file),Kpiece)) and (self.currentboard.checkpos(self.rank-2,self.file) != None)     and not (self.checkcheck(self.rank-2,self.file)) ):
                    possiblemovesforoutput.append("White Pawn from "+self.truefile+str(self.truerank) +" to "+ (self.truefile)+str(self.truerank+2))
                    if((isinstance(self.currentboard.checkpos(self.rank-2,self.file+1),Kpiece)) and (self.checkcheck(self.rank-2,self.file+1)) or (isinstance(self.currentboard.checkpos(self.rank-2,self.file-1),Kpiece))):
                        newenpassant = (self.rank-1,self.file)
                        nicenewenpassant = (self.truefile+str(self.truerank+1))
                        self.currentboard.enpapiece = self
                    None

            if(not isinstance(self.currentboard.checkpos(self.rank-1,self.file),Kpiece) and (self.currentboard.checkpos(self.rank-1,self.file) != None)   and not(self.checkcheck(self.rank-1,self.file)) ):
                if(self.checkpromote(self.rank-1,self.file)):
                    possiblemovesforoutput.append("White Pawn from "+self.truefile+str(self.truerank) +" to "+ (self.truefile)+str(self.truerank+1)+" With Promotion: "+str(random.choice(self.possiblepromotes)))
                else:
                    possiblemovesforoutput.append("White Pawn from "+self.truefile+str(self.truerank) +" to "+ (self.truefile)+str(self.truerank+1))

            if((isinstance(self.currentboard.checkpos(self.rank-1,self.file-1),Kpiece))  and (self.currentboard.checkpos(self.rank-1,self.file-1) != None)and (self.player != self.currentboard.checkpos(self.rank-1,self.file-1).player)   and not (self.checkcheck(self.rank-1,self.file-1)) ):
                if(self.checkpromote(self.rank-1,self.file-1)):
                    possiblemovesforoutput.append("White Pawn from "+self.truefile+str(self.truerank) +" to "+ chr(ord(self.truefile)-1)+str(self.truerank+1)+" With Promotion: "+str(random.choice(self.possiblepromotes)))
                else:
                    possiblemovesforoutput.append("White Pawn from "+self.truefile+str(self.truerank) +" to "+ chr(ord(self.truefile)-1)+str(self.truerank+1))

            if((isinstance(self.currentboard.checkpos(self.rank-1,self.file+1),Kpiece))  and (self.currentboard.checkpos(self.rank-1,self.file+1) != None)and (self.player != self.currentboard.checkpos(self.rank-1,self.file+1).player)   and not (self.checkcheck(self.rank-1,self.file+1)) ):
                if(self.checkpromote(self.rank-1,self.file+1)):
                    possiblemovesforoutput.append("White Pawn from "+self.truefile+str(self.truerank) +" to "+ chr(ord(self.truefile)+1)+str(self.truerank+1)+" With Promotion: "+str(random.choice(self.possiblepromotes)))
                else:
                    possiblemovesforoutput.append("White Pawn from "+self.truefile+str(self.truerank) +" to "+ chr(ord(self.truefile)+1)+str(self.truerank+1))

            if(((self.currentboard.enpassant ==(chr(ord(self.truefile)+1)+str(self.truerank+1))))  and (self.currentboard.checkpos(self.rank-1,self.file+1) != None)and (self.player != self.currentboard.checkpos(self.rank-1,self.file+1).player) and (self.currentboard.enpapiece.player != self.player)   and not (self.checkcheck(self.rank-1,self.file+1)) ):
                possiblemovesforoutput.append("White Pawn from "+self.truefile+str(self.truerank) +" to "+ chr(ord(self.truefile)+1)+str(self.truerank+1)+"ENPASSANT AT: "+self.currentboard.enpassant)
                None
            if((self.currentboard.enpassant ==(chr(ord(self.truefile)-1)+str(self.truerank+1))))  and (self.currentboard.checkpos(self.rank-1,self.file-1) != None)and (self.player != self.currentboard.checkpos(self.rank-1,self.file-1).player) and (self.currentboard.enpapiece.player != self.player)   and not (self.checkcheck(self.rank-1,self.file-1)):
                possiblemovesforoutput.append("White Pawn from "+self.truefile+str(self.truerank) +" to "+ chr(ord(self.truefile)-1)+str(self.truerank+1)+"ENPASSANT AT: "+self.currentboard.enpassant)
                None

        elif(self.player == "Black"):
            if(self.rank == 1):
                #checkforcheck
                if(not isinstance(self.currentboard.checkpos(self.rank+2,self.file),Kpiece)and (not isinstance(self.currentboard.checkpos(self.rank+1,self.file),Kpiece)) and (self.currentboard.checkpos(self.rank+2,self.file) != None) and not(self.checkcheck(self.rank+2,self.file))):
                    possiblemovesforoutput.append(str("Black Pawn from "+self.truefile+str(self.truerank) +" to "+ (self.truefile)+str(self.truerank-2)))
                    if((isinstance(self.currentboard.checkpos(self.rank+2,self.file+1),Kpiece)) and (self.checkcheck(self.rank-2,self.file+1)) or (isinstance(self.currentboard.checkpos(self.rank+2,self.file-1),Kpiece))):
                        newenpassant = (self.rank+1,self.file)
                        nicenewenpassant = (self.truefile+str(self.truerank-1))
                        self.currentboard.enpapiece = self
                    None

            if(not isinstance(self.currentboard.checkpos(self.rank+1,self.file),Kpiece)  and (self.currentboard.checkpos(self.rank+1,self.file) != None)and not(self.checkcheck(self.rank+1,self.file))):
                if(self.checkpromote(self.rank+1,self.file)):
                    possiblemovesforoutput.append("Black Pawn from "+self.truefile+str(self.truerank) +" to "+ (self.truefile)+str(self.truerank-1)+" With Promotion: "+str(random.choice(self.possiblepromotes)))
                else:
                    possiblemovesforoutput.append("Black Pawn from "+self.truefile+str(self.truerank) +" to "+ (self.truefile)+str(self.truerank-1))

            if((isinstance(self.currentboard.checkpos(self.rank+1,self.file-1),Kpiece))  and (self.currentboard.checkpos(self.rank+1,self.file-1) != None)and (self.player != self.currentboard.checkpos(self.rank+1,self.file-1).player)and not(self.checkcheck(self.rank+1,self.file-1))):
                if(self.checkpromote(self.rank+1,self.file-1)):
                    possiblemovesforoutput.append("Black Pawn from "+self.truefile+str(self.truerank) +" to "+ chr(ord(self.truefile)-1)+str(self.truerank-1)+" With Promotion: "+str(random.choice(self.possiblepromotes)))
                else:
                    possiblemovesforoutput.append("Black Pawn from "+self.truefile+str(self.truerank) +" to "+ chr(ord(self.truefile)-1)+str(self.truerank-1))

            if((isinstance(self.currentboard.checkpos(self.rank+1,self.file+1),Kpiece))  and (self.currentboard.checkpos(self.rank+1,self.file+1) != None)and (self.player != self.currentboard.checkpos(self.rank+1,self.file+1).player)and not(self.checkcheck(self.rank+1,self.file+1))):
                if(self.checkpromote(self.rank+1,self.file+1)):
                    possiblemovesforoutput.append("Black Pawn from "+self.truefile+str(self.truerank) +" to "+ chr(ord(self.truefile)+1)+str(self.truerank-1)+" With Promotion: "+str(random.choice(self.possiblepromotes)))
                else:
                    possiblemovesforoutput.append("Black Pawn from "+self.truefile+str(self.truerank) +" to "+ chr(ord(self.truefile)+1)+str(self.truerank-1))

            if((self.currentboard.enpassant ==(chr(ord(self.truefile)+1)+str(self.truerank-1)))  and (self.currentboard.checkpos(self.rank+1,self.file+1) != None)and (self.player != self.currentboard.checkpos(self.rank+1,self.file+1).player) and (self.currentboard.enpapiece.player != self.player)and not(self.checkcheck(self.rank+1,self.file+1))):
                possiblemovesforoutput.append("Black Pawn from "+self.truefile+str(self.truerank) +" to "+ chr(ord(self.truefile)+1)+str(self.truerank-1)+"ENPASSANT AT: "+self.currentboard.enpassant)
                None
            if((self.currentboard.enpassant ==(chr(ord(self.truefile)-1)+str(self.truerank-1))))  and (self.currentboard.checkpos(self.rank+1,self.file-1) != None)and (self.player != self.currentboard.checkpos(self.rank+1,self.file-1).player) and (self.currentboard.enpapiece.player != self.player)and not(self.checkcheck(self.rank+1,self.file-1)):
                possiblemovesforoutput.append("Black Pawn from "+self.truefile+str(self.truerank) +" to "+ chr(ord(self.truefile)-1)+str(self.truerank-1)+"ENPASSANT AT: "+self.currentboard.enpassant)
                None


        None
    
        return possiblemovesforoutput









class Bishop(Kpiece):
    def __init__(self,inrank,infile,player,intype,board):
        Kpiece.__init__(self,inrank,infile,player,board)
        self.type = intype
        self.movements = [(1,1),(1,-1),(-1,1),(-1,-1)]
        self.rep = "B"
        self.score = 3


    def actions(self):
        possiblemovesforoutput = []
        possiblemovessimple = []
        newmove = self.movements[:]
        for pair in newmove:
            Brank = pair[0]
            Bfile = pair[1]
            while (not isinstance(self.currentboard.checkpos(self.rank+Brank,self.file+Bfile),Kpiece))  and (self.currentboard.checkpos(self.rank+Brank,self.file+Bfile) != None) and not(self.checkcheck(self.rank+Brank,self.file+Bfile)):
                possiblemovesforoutput.append(  self.player + " "+ self.type +" from " +self.truefile+str(self.truerank)+ " to "+ chr(ord(self.truefile)+Bfile)+str(self.truerank-Brank)  )
                Brank += pair[0]
                Bfile += pair[1]

            else:
                if ((isinstance(self.currentboard.checkpos(self.rank+Brank,self.file+Bfile),Kpiece))  and (self.currentboard.checkpos(self.rank+Brank,self.file+Bfile) != None) and (self.player != self.currentboard.checkpos(self.rank+Brank,self.file+Bfile).player) and not(self.checkcheck(self.rank+Brank,self.file+Bfile))):
                    possiblemovesforoutput.append(  self.player + " "+ self.type +" from " +self.truefile+str(self.truerank)+ " to "+ chr(ord(self.truefile)+Bfile)+str(self.truerank-Brank)  )
                    None
                None
        None




class Rook(Kpiece):
    def __init__(self,inrank,infile,player,intype,board):
        Kpiece.__init__(self,inrank,infile,player,board)
        self.type = intype
        self.movements = [(1,0),(-1,0),(0,1),(0,-1)]
        self.rep = "R"
        self.moved = [True]
        self.score = 5
        

    def actions(self):
        possiblemovesforoutput = []
        possiblemovessimple = []
        newmove = self.movements[:]
        for pair in newmove:
            Brank = pair[0]
            Bfile = pair[1]
            while (not isinstance(self.currentboard.checkpos(self.rank+Brank,self.file+Bfile),Kpiece))  and (self.currentboard.checkpos(self.rank+Brank,self.file+Bfile) != None)and not(self.checkcheck(self.rank+Brank,self.file+Bfile)):
                possiblemovesforoutput.append(  self.player + " "+ self.type +" from " +self.truefile+str(self.truerank)+ " to "+ chr(ord(self.truefile)+Bfile)+str(self.truerank-Brank)  )
                Brank += pair[0]
                Bfile += pair[1]
                if self.moved[0] == False:
                    self.moved[0] = True

            else:
                if ((isinstance(self.currentboard.checkpos(self.rank+Brank,self.file+Bfile),self.capablePs))  and (self.currentboard.checkpos(self.rank+Brank,self.file+Bfile) != None) and (self.player != self.currentboard.checkpos(self.rank+Brank,self.file+Bfile).player)and not(self.checkcheck(self.rank+Brank,self.file+Bfile))):
                    possiblemovesforoutput.append(  self.player + " "+ self.type +" from " +self.truefile+str(self.truerank)+ " to "+ chr(ord(self.truefile)+Bfile)+str(self.truerank-Brank)  )
                    if self.moved[0] == False:
                        self.moved[0] = True
                    None
            None
        None

class Knight(Kpiece):
    def __init__(self,inrank,infile,player,intype,board):
        Kpiece.__init__(self,inrank,infile,player,board)
        self.type = intype
        self.movements = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(-1,2),(1,-2),(-1,-2)]
        self.rep = "N"
        self.score = 3

    def actions(self):
        possiblemovesforoutput = []
        possiblemovessimple = []
        newmove = self.movements[:]
        for pair in newmove:
            Brank = pair[0]
            Bfile = pair[1]
            if (not isinstance(self.currentboard.checkpos(self.rank+Brank,self.file+Bfile),Kpiece))  and (self.currentboard.checkpos(self.rank+Brank,self.file+Bfile) != None) and not(self.checkcheck(self.rank+Brank,self.file+Bfile)):
                possiblemovesforoutput.append(  self.player + " "+ self.type +" from " +self.truefile+str(self.truerank)+ " to "+ chr(ord(self.truefile)+Bfile)+str(self.truerank-Brank)  )
                None

            else:
                if ((isinstance(self.currentboard.checkpos(self.rank+Brank,self.file+Bfile),self.capablePs))  and (self.currentboard.checkpos(self.rank+Brank,self.file+Bfile) != None) and (self.player != self.currentboard.checkpos(self.rank+Brank,self.file+Bfile).player) and not(self.checkcheck(self.rank+Brank,self.file+Bfile))):
                    possiblemovesforoutput.append(  self.player + " "+ self.type +" from " +self.truefile+str(self.truerank)+ " to "+ chr(ord(self.truefile)+Bfile)+str(self.truerank-Brank)  )
                    None
            None
        None
    


class Queen(Kpiece):
    def __init__(self,inrank,infile,player,intype,board):
        Kpiece.__init__(self,inrank,infile,player,board)
        self.type = intype
        self.movements = [(1,1),(1,-1),(-1,1),(-1,-1),(1,0),(-1,0),(0,1),(0,-1)]
        self.rep = "Q"
        self.score = 9

    def actions(self):
        possiblemovesforoutput = []
        possiblemovessimple = []
        newmove = self.movements[:]
        for pair in newmove:
            Brank = pair[0]
            Bfile = pair[1]
            while (not isinstance(self.currentboard.checkpos(self.rank+Brank,self.file+Bfile),Kpiece))  and (self.currentboard.checkpos(self.rank+Brank,self.file+Bfile) != None)  and not(self.checkcheck(self.rank+Brank,self.file+Bfile)):
                possiblemovesforoutput.append(  self.player + " "+ self.type +" from " +self.truefile+str(self.truerank)+ " to "+ chr(ord(self.truefile)+Bfile)+str(self.truerank-Brank)  )
                Brank += pair[0]
                Bfile += pair[1]

            else:
                if ((isinstance(self.currentboard.checkpos(self.rank+Brank,self.file+Bfile),self.capablePs))  and (self.currentboard.checkpos(self.rank+Brank,self.file+Bfile) != None) and (self.player != self.currentboard.checkpos(self.rank+Brank,self.file+Bfile).player) and not(self.checkcheck(self.rank+1,self.file-1)) ):
                    possiblemovesforoutput.append(  self.player + " "+ self.type +" from " +self.truefile+str(self.truerank)+ " to "+ chr(ord(self.truefile)+Bfile)+str(self.truerank-Brank)  )
                    None
            None
        None



class King(Kpiece):
    def __init__(self,inrank,infile,player,intype,board):
        Kpiece.__init__(self,inrank,infile,player,board)
        self.type = intype
        self.movements = [(1,1),(1,-1),(-1,1),(-1,-1),(1,0),(-1,0),(0,1),(0,-1)]
        self.rep = "K"
        self.moved = [False]
        self.score = 0
        
        

    def checkcastle(self,possiblemovesforoutput):
        castle = 2
        direction = []
        if (self.currentboard.currentplayer == "White"):
            if(self.currentboard.whitecastleQ[0] == True ):
                direction.append((-1,4))
            if(self.currentboard.whitecastleK[0] == True ):
                direction.append((1,3))
        if (self.currentboard.currentplayer == "Black"):
            if(self.currentboard.blackcastleQ[0] == True ):
                direction.append((-1,4))
            if(self.currentboard.blackcastleK[0] == True ):
                direction.append((1,3))
        for side in direction:
            count = side[0]
            while (not isinstance(self.currentboard.checkpos(self.rank,self.file+count),Kpiece))  and (self.currentboard.checkpos(self.rank,self.file+count) != None) and (abs(count) < side[1])and not(self.checkcheck(self.rank,self.file+count)) :
                        if(abs(count) == side[1]-1) :
                            None
                            possiblemovesforoutput.append(  self.player + " "+ self.type +" from " +self.truefile+str(self.truerank)+ " to "+ chr(ord(self.truefile)+side[0]+side[0])+str(self.truerank)+" CASLTING"  )
                        else:
                            None
                            #possiblemovesforoutput.append(  self.player + " "+ self.type +" from " +self.truefile+str(self.truerank)+ " to "+ chr(ord(self.truefile)+count)+str(self.truerank)  )
                        count += side[0] 

            

        None



    def actions(self):
        possiblemovesforoutput = []
        possiblemovessimple = []
        newmove = self.movements[:]
        if(self.moved[0] == False):
            self.checkcastle(possiblemovesforoutput)
        for pair in newmove:
            Brank = pair[0]
            Bfile = pair[1]
            if (not isinstance(self.currentboard.checkpos(self.rank+Brank,self.file+Bfile),Kpiece))  and (self.currentboard.checkpos(self.rank+Brank,self.file+Bfile) != None):
                possiblemovesforoutput.append(  self.player + " "+ self.type +" from " +self.truefile+str(self.truerank)+ " to "+ chr(ord(self.truefile)+Bfile)+str(self.truerank-Brank)  )
                if self.moved[0] == False:
                    self.moved[0] = True
                    if(self.currentboard.currentplayer == "White"):
                        self.currentboard.whitecastleQ[0] = True
                        self.currentboard.whitecastleK[0] = True
                    elif(self.currentboard.currentplayer == "Black"):
                        self.currentboard.blackcastleQ[0] = True
                        self.currentboard.blackcastleK[0] = True

                None

            if ((isinstance(self.currentboard.checkpos(self.rank+Brank,self.file+Bfile),self.capablePs))  and (self.currentboard.checkpos(self.rank+Brank,self.file+Bfile) != None) and (self.player != self.currentboard.checkpos(self.rank+Brank,self.file+Bfile).player)):
                possiblemovesforoutput.append(  self.player + " "+ self.type +" from " +self.truefile+str(self.truerank)+ " to "+ chr(ord(self.truefile)+Bfile)+str(self.truerank-Brank)  )
                if self.moved[0] == False:
                    self.moved[0] = True
                    if(self.currentboard.currentplayer == "White"):
                        self.currentboard.whitecastleQ[0] = True
                        self.currentboard.whitecastleK[0] = True
                    elif(self.currentboard.currentplayer == "Black"):
                        self.currentboard.blackcastleQ[0] = True
                        self.currentboard.blackcastleK[0] = True
        None

            