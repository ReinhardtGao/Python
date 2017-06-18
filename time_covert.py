hour = 1
minute = hour * 60
print(hour, '''hour has ''',minute, '''minutes''')
second = minute * 60
print(hour, '''hour has ''',second, '''seconds''')
second_per_hour = second
day = 24
day_seconds = 24 * second_per_hour
print(day, '''day has''', day_seconds, '''seconds''')
second_per_day = hour * 24 * 60 * 60
print(day, '''day has''', second_per_day, '''seconds''')
output1 = second_per_day/second_per_hour
print(output1)
output2 = second_per_day//second_per_hour
print(output2)


