class TulipStrategy(object):
    """Mealy transducer.

    Internal states are integers, the current state
    is stored in the attribute "state".
    To take a transition, call method "move".

    The names of input variables are stored in the
    attribute "input_vars".

    Automatically generated by tulip.dumpsmach on 2018-01-14 18:20:49 UTC
    To learn more about TuLiP, visit http://tulip-control.org
    """
    def __init__(self):
        self.state = 18
        self.input_vars = ['Base', 'Goal', 'GoalPos']

    def move(self, Base, Goal, GoalPos):
        """Given inputs, take move and return outputs.

        @rtype: dict
        @return: dictionary with keys of the output variable names:
            ['loc']
        """
        output = dict()
        if self.state == 0:
            if (Base == False) and (Goal == False) and (GoalPos == False):
                self.state = 0

                output["loc"] = 'Water100'
            elif (Base == False) and (Goal == False) and (GoalPos == True):
                self.state = 1

                output["loc"] = 'Water100'
            elif (Base == False) and (Goal == True) and (GoalPos == False):
                self.state = 2

                output["loc"] = 'Water100'
            elif (Base == True) and (Goal == False) and (GoalPos == False):
                self.state = 4

                output["loc"] = 'Water100'
            elif (Base == True) and (Goal == True) and (GoalPos == False):
                self.state = 5

                output["loc"] = 'Water100'
            elif (Base == False) and (Goal == True) and (GoalPos == True):
                self.state = 6

                output["loc"] = 'Water60'
            else:
                self._error(Base, Goal, GoalPos)
        elif self.state == 1:
            if (Base == False) and (Goal == False) and (GoalPos == False):
                self.state = 0

                output["loc"] = 'Water100'
            elif (Base == False) and (Goal == False) and (GoalPos == True):
                self.state = 1

                output["loc"] = 'Water100'
            elif (Base == False) and (Goal == True) and (GoalPos == False):
                self.state = 2

                output["loc"] = 'Water100'
            elif (Base == True) and (Goal == False) and (GoalPos == False):
                self.state = 4

                output["loc"] = 'Water100'
            elif (Base == True) and (Goal == True) and (GoalPos == False):
                self.state = 5

                output["loc"] = 'Water100'
            elif (Base == False) and (Goal == True) and (GoalPos == True):
                self.state = 6

                output["loc"] = 'Water60'
            else:
                self._error(Base, Goal, GoalPos)
        elif self.state == 2:
            if (Base == False) and (Goal == False) and (GoalPos == False):
                self.state = 0

                output["loc"] = 'Water100'
            elif (Base == False) and (Goal == False) and (GoalPos == True):
                self.state = 1

                output["loc"] = 'Water100'
            elif (Base == False) and (Goal == True) and (GoalPos == False):
                self.state = 2

                output["loc"] = 'Water100'
            elif (Base == True) and (Goal == False) and (GoalPos == False):
                self.state = 4

                output["loc"] = 'Water100'
            elif (Base == True) and (Goal == True) and (GoalPos == False):
                self.state = 5

                output["loc"] = 'Water100'
            elif (Base == False) and (Goal == True) and (GoalPos == True):
                self.state = 6

                output["loc"] = 'Water60'
            else:
                self._error(Base, Goal, GoalPos)
        elif self.state == 3:
            if (Base == False) and (Goal == False) and (GoalPos == False):
                self.state = 0

                output["loc"] = 'Water100'
            elif (Base == False) and (Goal == False) and (GoalPos == True):
                self.state = 1

                output["loc"] = 'Water100'
            elif (Base == False) and (Goal == True) and (GoalPos == False):
                self.state = 2

                output["loc"] = 'Water100'
            elif (Base == True) and (Goal == False) and (GoalPos == False):
                self.state = 4

                output["loc"] = 'Water100'
            elif (Base == True) and (Goal == True) and (GoalPos == False):
                self.state = 5

                output["loc"] = 'Water100'
            elif (Base == False) and (Goal == True) and (GoalPos == True):
                self.state = 6

                output["loc"] = 'Water60'
            else:
                self._error(Base, Goal, GoalPos)
        elif self.state == 4:
            if (Base == False) and (Goal == False) and (GoalPos == False):
                self.state = 0

                output["loc"] = 'Water100'
            elif (Base == False) and (Goal == False) and (GoalPos == True):
                self.state = 1

                output["loc"] = 'Water100'
            elif (Base == False) and (Goal == True) and (GoalPos == False):
                self.state = 2

                output["loc"] = 'Water100'
            elif (Base == True) and (Goal == False) and (GoalPos == False):
                self.state = 4

                output["loc"] = 'Water100'
            elif (Base == True) and (Goal == True) and (GoalPos == False):
                self.state = 5

                output["loc"] = 'Water100'
            elif (Base == False) and (Goal == True) and (GoalPos == True):
                self.state = 6

                output["loc"] = 'Water60'
            else:
                self._error(Base, Goal, GoalPos)
        elif self.state == 5:
            if (Base == False) and (Goal == False) and (GoalPos == False):
                self.state = 0

                output["loc"] = 'Water100'
            elif (Base == False) and (Goal == False) and (GoalPos == True):
                self.state = 1

                output["loc"] = 'Water100'
            elif (Base == False) and (Goal == True) and (GoalPos == False):
                self.state = 2

                output["loc"] = 'Water100'
            elif (Base == True) and (Goal == False) and (GoalPos == False):
                self.state = 4

                output["loc"] = 'Water100'
            elif (Base == True) and (Goal == True) and (GoalPos == False):
                self.state = 5

                output["loc"] = 'Water100'
            elif (Base == False) and (Goal == True) and (GoalPos == True):
                self.state = 6

                output["loc"] = 'Water60'
            else:
                self._error(Base, Goal, GoalPos)
        elif self.state == 6:
            if (Base == True) and (Goal == False) and (GoalPos == False):
                self.state = 4

                output["loc"] = 'Water100'
            elif (Base == True) and (Goal == True) and (GoalPos == False):
                self.state = 5

                output["loc"] = 'Water100'
            elif (Base == False) and (Goal == False) and (GoalPos == False):
                self.state = 7

                output["loc"] = 'Water60'
            elif (Base == False) and (Goal == False) and (GoalPos == True):
                self.state = 8

                output["loc"] = 'Water60'
            elif (Base == False) and (Goal == True) and (GoalPos == False):
                self.state = 9

                output["loc"] = 'Water60'
            elif (Base == False) and (Goal == True) and (GoalPos == True):
                self.state = 10

                output["loc"] = 'Water20'
            else:
                self._error(Base, Goal, GoalPos)
        elif self.state == 7:
            if (Base == True) and (Goal == False) and (GoalPos == False):
                self.state = 4

                output["loc"] = 'Water100'
            elif (Base == True) and (Goal == True) and (GoalPos == False):
                self.state = 5

                output["loc"] = 'Water100'
            elif (Base == False) and (Goal == False) and (GoalPos == False):
                self.state = 7

                output["loc"] = 'Water60'
            elif (Base == False) and (Goal == False) and (GoalPos == True):
                self.state = 8

                output["loc"] = 'Water60'
            elif (Base == False) and (Goal == True) and (GoalPos == False):
                self.state = 9

                output["loc"] = 'Water60'
            elif (Base == False) and (Goal == True) and (GoalPos == True):
                self.state = 10

                output["loc"] = 'Water20'
            else:
                self._error(Base, Goal, GoalPos)
        elif self.state == 8:
            if (Base == True) and (Goal == False) and (GoalPos == False):
                self.state = 4

                output["loc"] = 'Water100'
            elif (Base == True) and (Goal == True) and (GoalPos == False):
                self.state = 5

                output["loc"] = 'Water100'
            elif (Base == False) and (Goal == False) and (GoalPos == False):
                self.state = 7

                output["loc"] = 'Water60'
            elif (Base == False) and (Goal == False) and (GoalPos == True):
                self.state = 8

                output["loc"] = 'Water60'
            elif (Base == False) and (Goal == True) and (GoalPos == False):
                self.state = 9

                output["loc"] = 'Water60'
            elif (Base == False) and (Goal == True) and (GoalPos == True):
                self.state = 10

                output["loc"] = 'Water20'
            else:
                self._error(Base, Goal, GoalPos)
        elif self.state == 9:
            if (Base == True) and (Goal == False) and (GoalPos == False):
                self.state = 4

                output["loc"] = 'Water100'
            elif (Base == True) and (Goal == True) and (GoalPos == False):
                self.state = 5

                output["loc"] = 'Water100'
            elif (Base == False) and (Goal == False) and (GoalPos == False):
                self.state = 7

                output["loc"] = 'Water60'
            elif (Base == False) and (Goal == False) and (GoalPos == True):
                self.state = 8

                output["loc"] = 'Water60'
            elif (Base == False) and (Goal == True) and (GoalPos == False):
                self.state = 9

                output["loc"] = 'Water60'
            elif (Base == False) and (Goal == True) and (GoalPos == True):
                self.state = 10

                output["loc"] = 'Water20'
            else:
                self._error(Base, Goal, GoalPos)
        elif self.state == 10:
            if (Base == True) and (Goal == False) and (GoalPos == False):
                self.state = 4

                output["loc"] = 'Water100'
            elif (Base == True) and (Goal == True) and (GoalPos == False):
                self.state = 5

                output["loc"] = 'Water100'
            elif (Base == False) and (Goal == False) and (GoalPos == False):
                self.state = 11

                output["loc"] = 'Water20'
            elif (Base == False) and (Goal == False) and (GoalPos == True):
                self.state = 12

                output["loc"] = 'Water20'
            elif (Base == False) and (Goal == True) and (GoalPos == False):
                self.state = 13

                output["loc"] = 'Water20'
            elif (Base == False) and (Goal == True) and (GoalPos == True):
                self.state = 14

                output["loc"] = 'Water0'
            else:
                self._error(Base, Goal, GoalPos)
        elif self.state == 11:
            if (Base == True) and (Goal == False) and (GoalPos == False):
                self.state = 4

                output["loc"] = 'Water100'
            elif (Base == True) and (Goal == True) and (GoalPos == False):
                self.state = 5

                output["loc"] = 'Water100'
            elif (Base == False) and (Goal == False) and (GoalPos == False):
                self.state = 11

                output["loc"] = 'Water20'
            elif (Base == False) and (Goal == False) and (GoalPos == True):
                self.state = 12

                output["loc"] = 'Water20'
            elif (Base == False) and (Goal == True) and (GoalPos == False):
                self.state = 13

                output["loc"] = 'Water20'
            elif (Base == False) and (Goal == True) and (GoalPos == True):
                self.state = 14

                output["loc"] = 'Water0'
            else:
                self._error(Base, Goal, GoalPos)
        elif self.state == 12:
            if (Base == True) and (Goal == False) and (GoalPos == False):
                self.state = 4

                output["loc"] = 'Water100'
            elif (Base == True) and (Goal == True) and (GoalPos == False):
                self.state = 5

                output["loc"] = 'Water100'
            elif (Base == False) and (Goal == False) and (GoalPos == False):
                self.state = 11

                output["loc"] = 'Water20'
            elif (Base == False) and (Goal == False) and (GoalPos == True):
                self.state = 12

                output["loc"] = 'Water20'
            elif (Base == False) and (Goal == True) and (GoalPos == False):
                self.state = 13

                output["loc"] = 'Water20'
            elif (Base == False) and (Goal == True) and (GoalPos == True):
                self.state = 14

                output["loc"] = 'Water0'
            else:
                self._error(Base, Goal, GoalPos)
        elif self.state == 13:
            if (Base == True) and (Goal == False) and (GoalPos == False):
                self.state = 4

                output["loc"] = 'Water100'
            elif (Base == True) and (Goal == True) and (GoalPos == False):
                self.state = 5

                output["loc"] = 'Water100'
            elif (Base == False) and (Goal == False) and (GoalPos == False):
                self.state = 11

                output["loc"] = 'Water20'
            elif (Base == False) and (Goal == False) and (GoalPos == True):
                self.state = 12

                output["loc"] = 'Water20'
            elif (Base == False) and (Goal == True) and (GoalPos == False):
                self.state = 13

                output["loc"] = 'Water20'
            elif (Base == False) and (Goal == True) and (GoalPos == True):
                self.state = 14

                output["loc"] = 'Water0'
            else:
                self._error(Base, Goal, GoalPos)
        elif self.state == 14:
            if (Base == True) and (Goal == False) and (GoalPos == False):
                self.state = 4

                output["loc"] = 'Water100'
            elif (Base == True) and (Goal == True) and (GoalPos == False):
                self.state = 5

                output["loc"] = 'Water100'
            elif (Base == False) and (Goal == True) and (GoalPos == True):
                self.state = 14

                output["loc"] = 'Water0'
            elif (Base == False) and (Goal == False) and (GoalPos == False):
                self.state = 15

                output["loc"] = 'Water0'
            elif (Base == False) and (Goal == False) and (GoalPos == True):
                self.state = 16

                output["loc"] = 'Water0'
            elif (Base == False) and (Goal == True) and (GoalPos == False):
                self.state = 17

                output["loc"] = 'Water0'
            else:
                self._error(Base, Goal, GoalPos)
        elif self.state == 15:
            if (Base == True) and (Goal == False) and (GoalPos == False):
                self.state = 4

                output["loc"] = 'Water100'
            elif (Base == True) and (Goal == True) and (GoalPos == False):
                self.state = 5

                output["loc"] = 'Water100'
            elif (Base == False) and (Goal == True) and (GoalPos == True):
                self.state = 14

                output["loc"] = 'Water0'
            elif (Base == False) and (Goal == False) and (GoalPos == False):
                self.state = 15

                output["loc"] = 'Water0'
            elif (Base == False) and (Goal == False) and (GoalPos == True):
                self.state = 16

                output["loc"] = 'Water0'
            elif (Base == False) and (Goal == True) and (GoalPos == False):
                self.state = 17

                output["loc"] = 'Water0'
            else:
                self._error(Base, Goal, GoalPos)
        elif self.state == 16:
            if (Base == True) and (Goal == False) and (GoalPos == False):
                self.state = 4

                output["loc"] = 'Water100'
            elif (Base == True) and (Goal == True) and (GoalPos == False):
                self.state = 5

                output["loc"] = 'Water100'
            elif (Base == False) and (Goal == True) and (GoalPos == True):
                self.state = 14

                output["loc"] = 'Water0'
            elif (Base == False) and (Goal == False) and (GoalPos == False):
                self.state = 15

                output["loc"] = 'Water0'
            elif (Base == False) and (Goal == False) and (GoalPos == True):
                self.state = 16

                output["loc"] = 'Water0'
            elif (Base == False) and (Goal == True) and (GoalPos == False):
                self.state = 17

                output["loc"] = 'Water0'
            else:
                self._error(Base, Goal, GoalPos)
        elif self.state == 17:
            if (Base == True) and (Goal == False) and (GoalPos == False):
                self.state = 4

                output["loc"] = 'Water100'
            elif (Base == True) and (Goal == True) and (GoalPos == False):
                self.state = 5

                output["loc"] = 'Water100'
            elif (Base == False) and (Goal == True) and (GoalPos == True):
                self.state = 14

                output["loc"] = 'Water0'
            elif (Base == False) and (Goal == False) and (GoalPos == False):
                self.state = 15

                output["loc"] = 'Water0'
            elif (Base == False) and (Goal == False) and (GoalPos == True):
                self.state = 16

                output["loc"] = 'Water0'
            elif (Base == False) and (Goal == True) and (GoalPos == False):
                self.state = 17

                output["loc"] = 'Water0'
            else:
                self._error(Base, Goal, GoalPos)
        elif self.state == 18:
            if (Base == False) and (Goal == False) and (GoalPos == False):
                self.state = 0

                output["loc"] = 'Water100'
            elif (Base == False) and (Goal == False) and (GoalPos == True):
                self.state = 1

                output["loc"] = 'Water100'
            elif (Base == False) and (Goal == True) and (GoalPos == False):
                self.state = 2

                output["loc"] = 'Water100'
            elif (Base == False) and (Goal == True) and (GoalPos == True):
                self.state = 3

                output["loc"] = 'Water100'
            elif (Base == True) and (Goal == False) and (GoalPos == False):
                self.state = 4

                output["loc"] = 'Water100'
            elif (Base == True) and (Goal == True) and (GoalPos == False):
                self.state = 5

                output["loc"] = 'Water100'
            else:
                self._error(Base, Goal, GoalPos)
        else:
            raise Exception("Unrecognized internal state: " + str(self.state))
        return output

    def _error(self, Base, Goal, GoalPos):
        raise ValueError("Unrecognized input: " + (
            "Base = {Base}; "
            "Goal = {Goal}; "
            "GoalPos = {GoalPos}; ").format(
                Base=Base,
                Goal=Goal,
                GoalPos=GoalPos))
