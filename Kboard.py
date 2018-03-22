




import Kpieces
class Board:
    def __init__(self):
        self.board = [[Kpieces.Empty() for y in range(8)] for x in range(8)]
        self.blackcastleQ = "-"
        self.blackcastleK = "-"
        self.whitecastleQ = "-"
        self.whitecastleK = "-"
        self.enpassant = ""
        self.prettyenpassant = ""
        self.currentplayer = ""
        self.prettyboard = [[y.rep for y in x] for x in self.board]


    def checkpos(self,inrank,infile):
        if((infile <0) or (infile >7) or (inrank <0) or (inrank >7)):
            return None
        return self.board[inrank][infile]