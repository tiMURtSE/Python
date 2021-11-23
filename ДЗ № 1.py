seconds = int(input())

days = seconds / (60 * 60 * 24)
hours = (days - int(days)) * 24
minutes = (hours - int(hours)) * 60
seconds_2 = (minutes - int(minutes)) * 60


h_zero, m_zero, s_zero = "", "", ""
if hours < 10:
    h_zero = "0"
if minutes < 10:
    m_zero = "0"
if seconds_2 < 10:
    s_zero = "0"
    
print(f"{int(days)}:{h_zero}{int(hours)}:{m_zero}{int(minutes)}:{s_zero}{round(seconds_2)}")
