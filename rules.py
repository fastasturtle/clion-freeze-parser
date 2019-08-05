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
    """
    Class for describing search rules.
    """

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


class PooledRule(NormalRule):
    """
    Class for describing rules involving stacktraces in pooled threads 
    """

    def __init__(self, edt_frame_seq, pooled_frame_seqs, message):
        """
        :param edt_frame_seq: List[str]
        :param pooled_frame_seqs: List[List[str]] list of excerpts of stacktraces of different pooled thread
        :param message: str
        """
        NormalRule.__init__(self, edt_frame_seq, message)
        self.pooled_frame_seqs = pooled_frame_seqs

    def is_matched(self, dump_file):
        if super(PooledRule, self).is_matched(dump_file):
            pooled_thread_infos = dump_file.get_pooled_info()
            if pooled_thread_infos is None:
                return False
            if all(
                    any(_contains_frames(pooled_seq, pooled_thread) for pooled_thread in pooled_thread_infos)
                    for pooled_seq in self.pooled_frame_seqs):
                return self.message
        return False


def desc(text, bug="CPP-?????", fixed=None):
    fixed_text = ("fixed in " + str(fixed) + " " if fixed else "")
    return fixed_text + text + " (" + bug + ")"


NO_EDT_MSG = "No EDT found"
WRITE_LOCK_MSG = "Waiting for write lock"
CIDR_IN_BACKGROUND_MSG = "CIDR in background, but not in EDT"
NO_CIDR_MSG = "No CIDR frames anywhere"

ENSURE_PARSED = "LazyParseableElement.getFirstChildNode"
WRITE_LOCK = ["ReadMostlyRWLock.writeLock", "ApplicationImpl.runWriteAction"]


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
