
class Room(object):
    def __init__(self, name, maxMember=4):
        super(Room, self).__init__()
        self.name = name
        self.maxMember = maxMember
        self.members = []

    def count(self):
        return len(self.members)

    def join_member(self, member):
        if self.count() < self.maxMember:
            self.members.append(member)

    def leave_member(self, sid):
        if self.members:
            for _member in self.members:
                if _member.sid == sid:
                    self.members.remove(_member)

    def full(self):
        if len(self.members) >= self.maxMember:
            return True
        return False

