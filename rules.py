class NormalRule:
    def __init__(self, frame_seq, message):
        self.frame_seq = frame_seq
        self.message = message

    def is_matched(self, stack):
        for f in self.frame_seq:
            found = False
            for l in stack:
                if f in l:
                    found = True
                    break
            if not found:
                return False
        return True
