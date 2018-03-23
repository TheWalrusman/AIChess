




import Kpieces
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


    def checkpos(self,inrank,infile):
        if((infile <0) or (infile >7) or (inrank <0) or (inrank >7)):
            return None
        return self.board[inrank][infile]

    def pretty(self):
        self.prettyboard = [[y.rep if y.player=="White" else y.rep.lower() for y in x] for x in self.board]