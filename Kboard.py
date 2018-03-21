





class Board:
    def __init__(self):
        self.board = [[0 for y in range(8)] for x in range(8)]
        self.blackcastleQ = "-"
        self.blackcastleK = "-"
        self.whitecastleQ = "-"
        self.whitecastleK = "-"
        self.enpassant = ""


    def checkpos(self,inrank,infile):
        if((infile <0) or (infile >7) or (inrank <0) or (inrank >7)):
            return None
        return self.board[inrank][infile]