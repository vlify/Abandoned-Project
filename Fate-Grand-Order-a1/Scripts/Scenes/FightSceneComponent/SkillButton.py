from Core.Game.function import get_system
from Core.UI.UIBase import ScaleButton


class SkillButton(ScaleButton):
    def __init__(self, surface, pos, scale, event=[]):
        super(SkillButton, self).__init__(surface, pos, scale, event)
        self.able = False

    def update(self, *args):
        super(SkillButton, self).update()
        if get_system().state is "skill":
            self.able = True
        else:
            self.able = False
