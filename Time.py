def timeCheck(hour, minute, period):
  join = lambda lst: "".join(lst)

  for i in range(len(period)-1):
    start = int(join(period[i].split(":")))
    end = int(join(period[i+1].split(":")))
    current = int(hour + minute)

    if current in range(start, end):
      return period.index(period[i])
  else:
    return -1