import sys

from st2common.runners.base_action import Action

class RoboStarter(Action):
    def run(self, the_test):
        print(the_test)

        if the_test == 'working':
            return (True, the_test)
        return (False, the_test)