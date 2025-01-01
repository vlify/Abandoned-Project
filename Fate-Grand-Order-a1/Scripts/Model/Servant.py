from Scripts.Model.Base.Character import Character, Feature
from Scripts.Type import StandType
from Scripts.Type import WeaponType


class Servant(Character):
    def __init__(self, data, level=1):
        super(Servant, self).__init__(data, level)
        self.see = self.data['see']
        self.love = self.data['love']
        self.team_location = self.data['team_location']
        self.identity = self.data['identity']

        self.mainparm = self.data['mainparm']

        self.weapon = self.data['weapon']
        self.weapon_list = []
        self.weapon_str = ''
        for weapon in self.weapon:
            self.weapon_str += getattr(WeaponType, 'str_' + weapon) + ' | '
            self.weapon_list.append(getattr(WeaponType, weapon))
        self.weapon_str = self.weapon_str[:-2]

        self.weight = self.data['weight']
        self.stand = getattr(StandType, self.data['stand'])
        self.stand_str = getattr(StandType, 'str_' + self.data['stand'])
        self.move = self.data['move']
        self.movetype = self.data['movetype']

        self.features_num = self.data['features_num']
        self.interaction_num = self.data['interaction_num']

        self.production_num = self.data['production_num']

        self.features_list = self.data['features']
        self.features = []
        for feature in self.features_list:
            self.features.append(Feature(feature))
