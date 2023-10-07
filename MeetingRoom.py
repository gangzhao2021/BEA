import datetime


class MeetingRoom:
    def __init__(self, name):
        self.name = name
        self.bookings = []

    def book(self, date, start_time, end_time, user):
        for booking in self.bookings:
            if booking['date'] == date and not (booking['end_time'] <= start_time or booking['start_time'] >= end_time):
                return False  # Time slot already booked
        self.bookings.append({
            'date': date,
            'start_time': start_time,
            'end_time': end_time,
            'user': user
        })
        return True

    def cancel(self, date, start_time, end_time, user):
        for booking in self.bookings:
            if booking['date'] == date and booking['start_time'] == start_time and booking['end_time'] == end_time and booking['user'] == user:
                self.bookings.remove(booking)
                return True
        return False

    def show_bookings(self, date):
        bookings_today = [b for b in self.bookings if b['date'] == date]
        return sorted(bookings_today, key=lambda x: x['start_time'])


class ReservationSystem:
    def __init__(self):
        self.rooms = {}

    def add_room(self, name):
        if name not in self.rooms:
            self.rooms[name] = MeetingRoom(name)
            return True
        return False

    def book(self, room_name, date, start_time, end_time, user):
        if room_name not in self.rooms:
            print(f"No room named {room_name} found.")
            return
        return self.rooms[room_name].book(date, start_time, end_time, user)

    def cancel(self, room_name, date, start_time, end_time, user):
        if room_name not in self.rooms:
            print(f"No room named {room_name} found.")
            return
        return self.rooms[room_name].cancel(date, start_time, end_time, user)

    def show_bookings(self, room_name, date):
        if room_name not in self.rooms:
            print(f"No room named {room_name} found.")
            return
        return self.rooms[room_name].show_bookings(date)


if __name__ == "__main__":
    system = ReservationSystem()
    system.add_room("A")
    print(system.book("A", "2023-10-07", "09:00", "11:00", "user1"))  # True
    print(system.show_bookings("A", "2023-10-07"))
    # print(system.book("A", "2023-10-07", "10:00", "12:00", "user2"))  # False because of overlap
    print(system.book("A", "2023-10-07", "11:00", "13:00", "user2"))  # True
    print(system.show_bookings("A", "2023-10-07"))
    print(system.book("A", "2023-10-07", "07:00", "09:00", "user3"))  # True
