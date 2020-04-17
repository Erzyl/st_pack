import sys
import webbrowser

from st2common.runners.base_action import Action

class RoboStarter(Action):
    def run(self, the_test):
        print(the_test)

        webbrowser.open('http://net-informations.com', new=2)

        if the_test == 'working':
            return (True, the_test)
        return (False, the_test)