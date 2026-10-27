# 강의실 예약 시스템 — 아래 클래스를 완성하세요. (클래스·메서드 이름은 바꾸지 마세요)

ROOMS = ("A101", "A102", "B201")
DAYS = ("월", "화", "수", "목", "금")
OPEN_HOUR = 9
CLOSE_HOUR = 21
MAX_HOURS = 3
MAX_PER_PERSON_PER_DAY = 2


def _is_int(value):
    # bool·IntEnum 같은 int 하위 타입은 정수로 보지 않음
    return type(value) is int


def _is_valid_place(room, day):
    return isinstance(room, str) and isinstance(day, str) and room in ROOMS and day in DAYS


def _is_valid_name(name):
    # None·빈 문자열·공백만·제어문자/제로폭 문자가 섞인 이름은 거절
    return isinstance(name, str) and name.strip() != "" and name.isprintable()


class RoomBooking:
    def __init__(self):
        # (room, day) -> [(start, end, name), ...]
        self._bookings = {}

    def book(self, room, day, start, end, name):
        if not _is_valid_place(room, day) or not _is_valid_name(name):
            return False
        if not _is_int(start) or not _is_int(end):
            return False
        if start < OPEN_HOUR or end > CLOSE_HOUR:
            return False
        if start >= end:
            return False
        if end - start > MAX_HOURS:
            return False

        slots = self._bookings.get((room, day), [])
        for s, e, _ in slots:
            # 끝나는 시각에 바로 시작하는 것은 겹침이 아님
            if start < e and s < end:
                return False

        count = sum(
            1
            for (_, d), items in self._bookings.items()
            if d == day
            for _, _, n in items
            if n == name
        )
        if count >= MAX_PER_PERSON_PER_DAY:
            return False

        self._bookings.setdefault((room, day), []).append((start, end, name))
        return True

    def cancel(self, room, day, start, name):
        if not _is_valid_place(room, day) or not _is_int(start) or not _is_valid_name(name):
            return False
        slots = self._bookings.get((room, day), [])
        for i, (s, _, n) in enumerate(slots):
            if s == start:
                if n != name:
                    return False
                del slots[i]
                return True
        return False

    def get_schedule(self, room, day):
        if not _is_valid_place(room, day):
            return []
        return sorted(self._bookings.get((room, day), []))
