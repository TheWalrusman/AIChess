""" function minimax(node, depth, maximizingPlayer)
02     if depth = 0 or node is a terminal node
03         return the heuristic value of node

04     if maximizingPlayer
05         bestValue := −∞
06         for each child of node
07             v := minimax(child, depth − 1, FALSE)
08             bestValue := max(bestValue, v)
09         return bestValue

10     else    (* minimizing player *)
11         bestValue := +∞
12         for each child of node
13             v := minimax(child, depth − 1, TRUE)
14             bestValue := min(bestValue, v)
15         return bestValue

(* Initial call for maximizing player *)
minimax(origin, depth, TRUE)
 """
import Kpieces
def minimax(self,board,depth,MaxorMin,value = None):
    new_boards = []
    if (depth == 0) or (value != None) or (board.stalecheck()):
        return board.currentboard.currentmat("White")

    if(MaxorMin == True):
        bestval = -100000000000
        for rows in self.board:
            for piece in rows:
                if(isinstance(piece,Kpieces.Kpiece) and (piece.player == self.currentplayer)):
                    new_boards.extend(piece.action())
        for node in new_boards:
            tmpval = self.minimax(node,depth-1,False)
            bestval = max(bestval,tmpval)
        return bestval
    if(MaxorMin == False):
        bestval = 100000000000
        for rows in self.board:
            for piece in rows:
                if(isinstance(piece,Kpieces.Kpiece) and (piece.player == self.currentplayer)):
                    new_boards.extend(piece.action())
        for node in new_boards:
            tmpval = self.minimax(node,depth-1,True)
            bestval = min(bestval,tmpval)
        return bestval
    
                
    

