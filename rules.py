from typing import List

from dump_file import DumpFileInfo, ThreadInfo


def _contains_frames(frames: List[str], thread_info: ThreadInfo):
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
    def __init__(self, frame_seq: List[str], message: str):
        self.frame_seq = frame_seq
        self.message = message

    def is_matched(self, dump_file: DumpFileInfo):
        edt_thread_info = dump_file.get_edt_info()
        if edt_thread_info is None:
            return False
        return _contains_frames(self.frame_seq, edt_thread_info)


class EdtWaitingRule:
    def __init__(self, message):
        self.message = message

    def is_matched(self, dump_file: DumpFileInfo):
        edt_thread_info = dump_file.get_edt_info()
        if edt_thread_info is None:
            return False
        if edt_thread_info.thread_state != "TIMED_WAITING":
            return False
        if not _contains_frames(["ReadMostlyRWLock.writeLock"], edt_thread_info):
            return False
        return True
