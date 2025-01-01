
rooms = []
all_members = []
sids = []


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


class Member(object):
    def __init__(self, sid, name):
        super(Member, self).__init__()
        self.sid = sid
        self.name = name


def print_r():
    for room in rooms:
        print "{0} count :{1}".format(room.name, room.count())
        for member in room.members:
            print "{0} : {1}".format(room.name, member.sid)
    print "all_members count:{0}".format(len(all_members))
    print "rooms count:{0}".format(len(rooms))


def send_message(msg):
    sio.emit("message", {"type": "info", "massage": msg})


@app.route('/')
def index():
    """Serve the client-side application."""
    return render_template('index.html')


@sio.on('connect')
def connect(sid, environ):
    member = Member(sid, "member")
    all_members.append(member)
    sids.append(sid)
    if not rooms:
        rooms.append(Room("r_1"))
        room = rooms[0]
        room.join_member(member)
    else:
        rooms_full = []
        for room in rooms:
            if room.full():
                rooms_full.append(1)
            else:
                rooms_full.append(0)
        if 0 in rooms_full:
            index = rooms_full.index(0)
            room = rooms[index]
            room.join_member(member)
        else:
            room = Room("r_" + str(len(rooms) + 1))
            room.join_member(member)
            rooms.append(room)
    send_message("welcom {0}".format(sid))
    # print_r()