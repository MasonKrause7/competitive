s = int(input())

minutes = s // 60
seconds = s % 60
hours = minutes // 60
minutes = minutes % 60
print(f"{hours} : {minutes} : {seconds}")
