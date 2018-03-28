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
def minimax(board,depth,startdepth,MaxorMin,value = None):
    new_boards = []
    if (depth == 0) or (value != None) or (board.stalecheck()):
        if(board.stalecheck()):
            return (0,board.currmove)
        else:
            return (board.currentmat("White"),board.currmove)

    if(MaxorMin == True):
        bestval = (-100000000000,None)
        for rows in board.board:
            for piece in rows:
                if(isinstance(piece,Kpieces.Kpiece) and (piece.player == board.currentplayer)):
                    new_boards.extend(piece.actions())
        if(not new_boards ):
            return (-1000,board.currmove)
        for node in new_boards:
            tmpval = minimax(node,depth-1,startdepth,False)
            tmptup = [bestval,tmpval]
            bestval = max(tmptup, key=lambda t: (t[0]))
            #bestval = max(bestval,tmpval)
        if(depth == startdepth):
            return bestval
        else:
            return (bestval[0],board.currmove)
    if(MaxorMin == False):
        bestval = (100000000000,None)
        for rows in board.board:
            for piece in rows:
                if(isinstance(piece,Kpieces.Kpiece) and (piece.player == board.currentplayer)):
                    new_boards.extend(piece.actions())
        if(not new_boards ):
            return (1000,board.currmove)
        for node in new_boards:
            tmpval = minimax(node,depth-1,startdepth,True)
            tmptup = [bestval,tmpval]
            bestval = min(tmptup, key=lambda t: (t[0]))
            #bestval = min(bestval,tmpval)
        if(depth == startdepth):
            return bestval
        else:
            return (bestval[0],board.currmove)
    
                
    

