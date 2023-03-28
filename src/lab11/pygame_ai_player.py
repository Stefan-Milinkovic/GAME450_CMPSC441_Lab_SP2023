""" Create PyGameAIPlayer class here"""


class PyGameAIPlayer:
    pass


""" Create PyGameAICombatPlayer class here"""


class PyGameAICombatPlayer:
    def selectAction(self, state):
        
        if state.encounter_event:
            return random.choice(['a', 'r'])
        else:
            # Original AI strategy
            return super.selectAction(state)
    pass
