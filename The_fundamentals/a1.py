def seconds_difference(time_1, time_2):
    '''(float, float) -> float
    Return the number of seconds later that a time in seconds
    time_2 is than a time in seconds time_1.
        
    >>> seconds_difference(1800.0, 3600.0)
    1800.0
    >>> seconds_difference(3600.0, 1800.0)
    -1800.0
    >>> seconds_difference(1800.0, 2160.0)
    360.0
    >>> seconds_difference(1800.0, 1800.0)
    0.0
    '''
    result = time_2-time_1
    return result


def hours_difference(time_1, time_2):
    '''(float, float) -> float

    Return the number of hours later that a time in seconds
    time_2 is than a time in seconds time_1.
        
    >>> hours_difference(1800.0, 3600.0)
    0.5
    >>> hours_difference(3600.0, 1800.0)
    -0.5
    >>> hours_difference(1800.0, 2160.0)
    0.1
    >>> hours_difference(1800.0, 1800.0)
    0.0
    '''
    in_seconds = seconds_difference(time_1,time_2)
    in_minutes = in_seconds /60
    in_hours = in_minutes/60
    return in_hours
    



def to_float_hours(hours, minutes, seconds):
   '''(int, int, int) -> float

   Return the total number of hours in the specified number
   of hours, minutes, and seconds.
   
   Precondition: 0 <= minutes < 60  and  0 <= seconds < 60
   
to   >>> to_float_hours(0, 15, 0)
   0.25
   >>> to_float_hours(2, 45, 9)
   2.7525
   >>> to_float_hours(1, 0, 36)
   1.01
   '''
   minutes_to = minutes/60
   seconds_to = seconds/3600
   all_t=hours + minutes_to+seconds_to
   return all_t



def to_24_hour_clock(hours):
    '''(number) -> number

    hours is a number of hours since midnight. Return the
    hour as seen on a 24-hour clock.

    Precondition: hours >= 0

    >>> to_24_hour_clock(24)
    0
    >>> to_24_hour_clock(48)
    0
    >>> to_24_hour_clock(25)
    1
    >>> to_24_hour_clock(4)
    4
    >>> to_24_hour_clock(28.5)
    4.5
    '''

    return hours % 24



### Write your get_hours function definition here:
def get_hours (i):
    '''(int)-> int
   Returns how many hours are in given i
     '''
    hours=i//3600
    return hours



### Write your get_minutes function definition here:
def get_minutes (a):
     '''(int)->int
    Returns how many minutes are in given a
     '''
     h = get_hours(a)
     hours_seconds = h*3600
     left = a - hours_seconds
     minutes = left//60
     return minutes
  



### Write your get_seconds function definition here:
 
def get_seconds (a):
    '''(int)->(int)
    Returns how many second are there in given a
    '''
    m = get_minutes(a)
    h = get_hours(a)
    hours_seconds=h*3600
    minutes_seconds = m*60
    left = a - hours_seconds - minutes_seconds
    return left    

def time_to_utc(utc_offset, time):
    '''(number, float) -> float

    Return time at UTC+0, where utc_offset is the number of hours away from
    UTC+0.

    >>> time_to_utc(+0, 12.0)
    12.0
    >>> time_to_utc(+1, 12.0)
    11.0
    >>> time_to_utc(-1, 12.0)
    13.0
    >>> time_to_utc(-11, 18.0)
    5.0
    >>> time_to_utc(-1, 0.0)
    1.0
    >>> time_to_utc(-1, 23.0)
    0.0
    '''
  
    t = to_24_hour_clock(time-(utc_offset))
    
    return t



def time_from_utc(utc_offset, time):
    '''(number, float) -> float

    Return UTC time in time zone utc_offset.

    >>> time_from_utc(+0, 12.0)
    12.0
    >>> time_from_utc(+1, 12.0)
    13.0
    >>> time_from_utc(-1, 12.0)
    11.0
    >>> time_from_utc(+6, 6.0)
    12.0
    >>> time_from_utc(-7, 6.0)
    23.0
    >>> time_from_utc(-1, 0.0)
    23.0
    >>> time_from_utc(-1, 23.0)
    22.0
    >>> time_from_utc(+1, 23.0)
    0.0
    '''
    t = to_24_hour_clock(time+(utc_offset))
    return t




