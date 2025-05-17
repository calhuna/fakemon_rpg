class PlayerParty:
    def __init__(self):
        self.fakemon_list = []

    def add_fakemon(self, fakemon_instance):
        if len(self.fakemon_list) < 6:
            self.fakemon_list.append(fakemon_instance)
        else:
            print("Party is full! Send to storage (not implemented yet).")

    def get_first_healthy(self):
        for mon in self.fakemon_list:
            if not mon.is_fainted():
                return mon
        return None

    def all_fainted(self):
        return all(mon.is_fainted() for mon in self.fakemon_list)

    def heal_all(self):
        for mon in self.fakemon_list:
            mon.current_hp = mon.hp

    def __repr__(self):
        return "\n".join([f"{idx+1}. {mon}" for idx, mon in enumerate(self.fakemon_list)])
