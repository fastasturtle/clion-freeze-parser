

def _contains_frames(frames, thread_info):
    """
    :param frames: List[str]
    :param thread_info: hreadInfo
    :return:
    """
    for f in frames:
        found = False
        for l in thread_info.frames:
            if f in l:
                found = True
                break
        if not found:
            return False
    return True


class NormalRule:
    def __init__(self, frame_seq, message):
        """
        :param frame_seq: List[str]
        :param message: str
        """
        self.frame_seq = frame_seq
        self.message = message

    def is_matched(self, dump_file):
        """
        :param dump_file: DumpFileInfo
        :return:
        """
        edt_thread_info = dump_file.get_edt_info()
        if edt_thread_info is None:
            return False
        if _contains_frames(self.frame_seq, edt_thread_info):
            return self.message
        return False


NO_EDT_MSG = "No EDT found"
WRITE_LOCK_MSG = "Waiting for write lock"
CIDR_IN_BACKGROUND_MSG = "CIDR in background, but not in EDT"
NO_CIDR_MSG = "No CIDR frames anywhere"


def is_waiting_for_write_lock(edt_thread_info):
    if edt_thread_info.thread_state != "TIMED_WAITING":
        return False
    if not _contains_frames(["ReadMostlyRWLock.writeLock"], edt_thread_info):
        return False
    return True


def has_cidr(info):
    """
    :param info: ThreadInfo
    :return:
    """
    for frame in info.frames:
        if "cidr" in frame:
            return True
    return False


def process_custom(dump_file):
    """
    :param dump_file: DumpFileInfo
    :return: Optional[str]
    """
    edt_thread_info = dump_file.get_edt_info()
    if edt_thread_info is None:
        return NO_EDT_MSG
    if is_waiting_for_write_lock(edt_thread_info):
        return WRITE_LOCK_MSG

    cidr_in_edt = False
    cidr_in_background = False
    for info in dump_file.thread_infos:
        if has_cidr(info):
            if info.is_edt:
                cidr_in_edt = True
            else:
                cidr_in_background = True
    if not cidr_in_edt and cidr_in_background:
        return CIDR_IN_BACKGROUND_MSG
    elif not cidr_in_edt and not cidr_in_background:
        return NO_CIDR_MSG
    else:
        return None
