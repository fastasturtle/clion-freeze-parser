from typing import List, Optional

STATE_PREFIX = "java.lang.Thread.State: "


class ThreadInfo:
    def __init__(self, frames: List[str], is_edt: bool, thread_state: str):
        self.frames = frames
        self.is_edt = is_edt
        self.thread_state = thread_state


class DumpFileInfo:
    def __init__(self, thread_infos: List[ThreadInfo]):
        self.thread_infos = thread_infos

    def get_edt_info(self) -> ThreadInfo:
        return next((i for i in self.thread_infos if i.is_edt), None)


def split_into_threads(lines: List[str]) -> List[List[str]]:
    start_indices = [i - 1 for i, s in enumerate(lines) if STATE_PREFIX in s]
    start_indices.append(len(lines))
    if len(start_indices) < 2:
        return []
    return [lines[begin:end] for begin, end in zip(start_indices[:-1], start_indices[1:])]


def parse_thread_info(thread: List[str]) -> Optional[ThreadInfo]:
    if len(thread) <= 3:
        return None

    if STATE_PREFIX not in thread[1]:
        return None

    is_edt = "AWT-EventQueue" in thread[0]
    thread_state = thread[1].strip().replace(STATE_PREFIX, "")
    return ThreadInfo(thread, is_edt, thread_state)


def parse_dump_file(lines: List[str]) -> Optional[DumpFileInfo]:
    infos = list(filter(lambda i: i is not None, (parse_thread_info(thread) for thread in split_into_threads(lines))))
    return DumpFileInfo(infos) if infos else None
