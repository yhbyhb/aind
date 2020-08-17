from copy import deepcopy

xlim, ylim = 3, 2  # board dimension constants

# The eight movement directions possible for a chess queen
RAYS = [(1, 0), (1, -1), (0, -1), (-1, -1),
        (-1, 0), (-1, 1), (0, 1), (1, 1)]


class GameState:
    """
    Attributes
    ----------
    TODO: Copy in your implementation from the previous quiz
    """
    def __init__(self):
        # TODO: Copy in your implementation from the previous quiz
        self._board = [[0] * ylim for _ in range(xlim)]
        self._board[-1][-1] = 1  # block lower-right corner
        self._parity = 0
        self._player_locations = [None, None]
        
    def actions(self):
        """ Return a list of legal actions for the active player 
        
        You are free to choose any convention to represent actions,
        but one option is to represent actions by the (row, column)
        of the endpoint for the token. For example, if your token is
        in (0, 0), and your opponent is in (1, 0) then the legal
        actions could be encoded as (0, 1) and (0, 2).
        """
        # TODO: Finish this function!
        return self.liberties(self._player_locations[self._parity])
    
    def player(self):
        """ Return the id of the active player 
        
        Hint: return 0 for the first player, and 1 for the second player
        """
        # TODO: Finish this function!
        return self._parity
    
    def result(self, action):
        """ Return a new state that results from applying the given
        action in the current state
        
        Hint: Check out the deepcopy module--do NOT modify the
        objects internal state in place
        """
        # TODO: Finish this function!
        assert action in self.actions(), "Attempted forecast of illegal move"
        newBoard = deepcopy(self)
        newBoard._board[action[0]][action[1]] = 1
        newBoard._player_locations[self._parity] = action
        newBoard._parity ^= 1
        return newBoard
    
    def terminal_test(self):
        """ return True if the current state is terminal,
        and False otherwise
        
        Hint: an Isolation state is terminal if _either_
        player has no remaining liberties (even if the
        player is not active in the current state)
        """
        # TODO: Finish this function!
        return (not self._has_liberties(self._parity)
            or not self._has_liberties(1 - self._parity))
    
    def liberties(self, loc):
        """ Return a list of all open cells in the
        neighborhood of the specified location.  The list 
        should include all open spaces in a straight line
        along any row, column or diagonal from the current
        position. (Tokens CANNOT move through obstacles
        or blocked squares in queens Isolation.)
        
        Note: if loc is None, then return all empty cells
        on the board
        """
        # TODO: Finish this function!
        if loc is None: return self._get_blank_spaces()
        moves = []
        for dx, dy in RAYS:  # check each movement direction
            _x, _y = loc
            while 0 <= _x + dx < xlim and 0 <= _y + dy < ylim:
                _x, _y = _x + dx, _y + dy
                if self._board[_x][_y]:  # stop at any blocked cell
                    break
                moves.append((_x, _y))
        return moves
    
    def _has_liberties(self, player_id):
        """ Check to see if the specified player has any liberties """
        return any(self.liberties(self._player_locations[player_id]))

    def _get_blank_spaces(self):
        """ Return a list of blank spaces on the board."""
        return [(x, y) for y in range(ylim) for x in range(xlim)
                if self._board[x][y] == 0]