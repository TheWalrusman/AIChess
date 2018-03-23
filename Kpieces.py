

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
        


    def ifmoved(self):
        if(self.player == "White"):

            None
    




class Pawn(Kpiece):
    def __init__(self,inrank,infile,player,intype,board):
        Kpiece.__init__(self,inrank,infile,player,board)
        self.type = intype
        self.possiblepromotes = ["Queen","Knight","Rook","Bishop",]
        self.rep = "P"
        

    def checkpromote(self,rank,file):
        if (self.currentboard.currentplayer == "White") and (rank == 0):
            return True
        elif(self.currentboard.currentplayer == "Black") and (rank == 8):
            return True
        else:
            return False


    def actions(self):
        possiblemovesforoutput = []
        possiblemovessimple = []
        if(self.player == "White"):
            if(self.rank == 6):
                #checkforcheck
                if((not isinstance(self.currentboard.checkpos(self.rank-2,self.file),Kpiece)) and (not isinstance(self.currentboard.checkpos(self.rank-1,self.file),Kpiece)) and (self.currentboard.checkpos(self.rank-2,self.file) != None)):
                    possiblemovesforoutput.append("White Pawn from "+self.truefile+str(self.truerank) +" to "+ (self.truefile)+str(self.truerank+2))
                    if((isinstance(self.currentboard.checkpos(self.rank-2,self.file+1),Kpiece)) or (isinstance(self.currentboard.checkpos(self.rank-2,self.file-1),Kpiece))):
                        newenpassant = (self.rank-1,self.file)
                        nicenewenpassant = (self.truefile+str(self.truerank+1))
                    None

            if(not isinstance(self.currentboard.checkpos(self.rank-1,self.file),Kpiece)  and (self.currentboard.checkpos(self.rank-1,self.file) != None)):
                if(self.checkpromote(self.rank-1,self.file)):
                    possiblemovesforoutput.append("White Pawn from "+self.truefile+str(self.truerank) +" to "+ (self.truefile)+str(self.truerank+1)+" With Promotion: "+str(random.choice(self.possiblepromotes)))
                else:
                    possiblemovesforoutput.append("White Pawn from "+self.truefile+str(self.truerank) +" to "+ (self.truefile)+str(self.truerank+1))

            if((isinstance(self.currentboard.checkpos(self.rank-1,self.file-1),Kpiece) or (self.currentboard.enpassant ==(chr(ord(self.truefile)-1)+str(self.truerank+1))))  and (self.currentboard.checkpos(self.rank-1,self.file-1) != None)and (self.player != self.currentboard.checkpos(self.rank-1,self.file-1).player)):
                if(self.checkpromote(self.rank-1,self.file-1)):
                    possiblemovesforoutput.append("White Pawn from "+self.truefile+str(self.truerank) +" to "+ chr(ord(self.truefile)-1)+str(self.truerank+1)+" With Promotion: "+str(random.choice(self.possiblepromotes)))
                else:
                    possiblemovesforoutput.append("White Pawn from "+self.truefile+str(self.truerank) +" to "+ chr(ord(self.truefile)-1)+str(self.truerank+1))

            if((isinstance(self.currentboard.checkpos(self.rank-1,self.file+1),Kpiece) or (self.currentboard.enpassant ==(chr(ord(self.truefile)+1)+str(self.truerank+1))) )  and (self.currentboard.checkpos(self.rank-1,self.file+1) != None)and (self.player != self.currentboard.checkpos(self.rank-1,self.file+1).player)):
                if(self.checkpromote(self.rank-1,self.file+1)):
                    possiblemovesforoutput.append("White Pawn from "+self.truefile+str(self.truerank) +" to "+ chr(ord(self.truefile)+1)+str(self.truerank+1)+" With Promotion: "+str(random.choice(self.possiblepromotes)))
                else:
                    possiblemovesforoutput.append("White Pawn from "+self.truefile+str(self.truerank) +" to "+ chr(ord(self.truefile)+1)+str(self.truerank+1))

        elif(self.player == "Black"):
            if(self.rank == 1):
                #checkforcheck
                if(not isinstance(self.currentboard.checkpos(self.rank+2,self.file),Kpiece)and (not isinstance(self.currentboard.checkpos(self.rank+1,self.file),Kpiece)) and (self.currentboard.checkpos(self.rank+2,self.file) != None)):
                    possiblemovesforoutput.append(str("Black Pawn from "+self.truefile+str(self.truerank) +" to "+ (self.truefile)+str(self.truerank-2)))
                    if((isinstance(self.currentboard.checkpos(self.rank+2,self.file+1),Kpiece)) or (isinstance(self.currentboard.checkpos(self.rank+2,self.file-1),Kpiece))):
                        newenpassant = (self.rank+1,self.file)
                        nicenewenpassant = (self.truefile+str(self.truerank-1))
                    None

            if(not isinstance(self.currentboard.checkpos(self.rank+1,self.file),Kpiece)  and (self.currentboard.checkpos(self.rank+1,self.file) != None)):
                if(self.checkpromote(self.rank+1,self.file)):
                    possiblemovesforoutput.append("Black Pawn from "+self.truefile+str(self.truerank) +" to "+ (self.truefile)+str(self.truerank-1)+" With Promotion: "+str(random.choice(self.possiblepromotes)))
                else:
                    possiblemovesforoutput.append("Black Pawn from "+self.truefile+str(self.truerank) +" to "+ (self.truefile)+str(self.truerank-1))

            if((isinstance(self.currentboard.checkpos(self.rank+1,self.file-1),Kpiece) or (self.currentboard.enpassant ==(chr(ord(self.truefile)-1)+str(self.truerank-1))))  and (self.currentboard.checkpos(self.rank+1,self.file-1) != None)and (self.player != self.currentboard.checkpos(self.rank+1,self.file-1).player)):
                if(self.checkpromote(self.rank+1,self.file-1)):
                    possiblemovesforoutput.append("Black Pawn from "+self.truefile+str(self.truerank) +" to "+ chr(ord(self.truefile)-1)+str(self.truerank-1)+" With Promotion: "+str(random.choice(self.possiblepromotes)))
                else:
                    possiblemovesforoutput.append("Black Pawn from "+self.truefile+str(self.truerank) +" to "+ chr(ord(self.truefile)-1)+str(self.truerank-1))

            if((isinstance(self.currentboard.checkpos(self.rank+1,self.file+1),Kpiece) or (self.currentboard.enpassant ==(chr(ord(self.truefile)+1)+str(self.truerank-1))))  and (self.currentboard.checkpos(self.rank+1,self.file+1) != None)and (self.player != self.currentboard.checkpos(self.rank+1,self.file+1).player)):
                if(self.checkpromote(self.rank+1,self.file+1)):
                    possiblemovesforoutput.append("Black Pawn from "+self.truefile+str(self.truerank) +" to "+ chr(ord(self.truefile)+1)+str(self.truerank-1)+" With Promotion: "+str(random.choice(self.possiblepromotes)))
                else:
                    possiblemovesforoutput.append("Black Pawn from "+self.truefile+str(self.truerank) +" to "+ chr(ord(self.truefile)+1)+str(self.truerank-1))

        None
        return possiblemovesforoutput









class Bishop(Kpiece):
    def __init__(self,inrank,infile,player,intype,board):
        Kpiece.__init__(self,inrank,infile,player,board)
        self.type = intype
        self.movements = [(1,1),(1,-1),(-1,1),(-1,-1)]
        self.rep = "B"


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
        self.rep = "R"
        self.moved = [True]
        

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
                if self.moved[0] == False:
                    self.moved[0] = True

            else:
                if ((isinstance(self.currentboard.checkpos(self.rank+Brank,self.file+Bfile),Kpiece))  and (self.currentboard.checkpos(self.rank+Brank,self.file+Bfile) != None) and (self.player != self.currentboard.checkpos(self.rank+Brank,self.file+Bfile).player)):
                    possiblemovesforoutput.append(  self.player + " "+ self.type +" from " +self.truefile+str(self.truerank)+ " to "+ chr(ord(self.truefile)+Bfile)+str(self.truerank-Brank)  )
                    if self.moved[0] == False:
                        self.moved[0] = True
                    None
                None

class Knight(Kpiece):
    def __init__(self,inrank,infile,player,intype,board):
        Kpiece.__init__(self,inrank,infile,player,board)
        self.type = intype
        self.movements = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(-1,2),(1,-2),(-1,-2)]
        self.rep = "N"

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
        self.rep = "Q"

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
        self.rep = "K"
        self.moved = [False]
        
        

    def checkcastle(self):
        castle = 2
        possiblemovesforoutput = []
        direction = []
        if (self.currentboard.currentplayer == "White"):
            if(self.currentboard.whitecastleQ[0] == True ):
                direction.append(-1)
            if(self.currentboard.whitecastleK[0] == True ):
                direction.append(1)
        if (self.currentboard.currentplayer == "Black"):
            if(self.currentboard.blackcastleQ[0] == True ):
                direction.append(-1)
            if(self.currentboard.blackcastleK[0] == True ):
                direction.append(1)
        for side in direction:
            count = side
            while (not isinstance(self.currentboard.checkpos(self.rank,self.file+count),Kpiece))  and (self.currentboard.checkpos(self.rank,self.file+count) != None) and (abs(count) < 3):
                        if(abs(count) == 2) :
                            None
                            possiblemovesforoutput.append(  self.player + " "+ self.type +" from " +self.truefile+str(self.truerank)+ " to "+ chr(ord(self.truefile)+count)+str(self.truerank)  )
                        else:
                            None
                            possiblemovesforoutput.append(  self.player + " "+ self.type +" from " +self.truefile+str(self.truerank)+ " to "+ chr(ord(self.truefile)+count)+str(self.truerank)  )
                        count += side 

            

        None



    def actions(self):
        possiblemovesforoutput = []
        possiblemovessimple = []
        newmove = self.movements[:]
        if(self.moved[0] == False):
            self.checkcastle()
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

            if ((isinstance(self.currentboard.checkpos(self.rank+Brank,self.file+Bfile),Kpiece))  and (self.currentboard.checkpos(self.rank+Brank,self.file+Bfile) != None) and (self.player != self.currentboard.checkpos(self.rank+Brank,self.file+Bfile).player)):
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

            