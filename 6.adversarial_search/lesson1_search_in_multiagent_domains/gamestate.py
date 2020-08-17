
# TODO: implement the __init__ class below by adding properties
# that meet the three requirements specified
xlim, ylim = 3, 2  # board dimension constants

class GameState:

    def __init__(self):
        """The GameState class constructor performs required
        initializations when an instance is created. The class
        should:
        
        1) Keep track of which cells are open/closed
        2) Identify which player has initiative
        3) Record the current location of each player
        
        Parameters
        ----------
        self:
            instance methods automatically take "self" as an
            argument in python
        
        Returns
        -------
        None
        """
        # You can define attributes like this:
        # self.value = 73  # an arbitrary number
        # reassign it to a string (variable type is dynamic in Python)
        # self.value = "some string"
        # self.foo = []  # create an empty list
        self._board = [[0] * ylim for _ in range(xlim)]
        self._board[-1][-1] = 1  # block lower-right corner
        self._parity = 0
        self._player_locations = [None, None]


if __name__ == "__main__":
    # This code is only executed if "gameagent.py" is the run
    # as a script (i.e., it is not run if "gameagent.py" is
    # imported as a module)
    emptyState = GameState()  # create an instance of the object
