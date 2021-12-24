def hourRange(hour):
  if hour[0] == "0":
    return f"0{int(hour) + 1}"
  else:
    return f"{int(hour) + 1}"

def timeCheck(hour, minute, period):
  new = list(
    filter(
      lambda pair: (
        pair[:2] == hour or pair[:2] == hourRange(hour)
      ), period
    )
  )

  if len(new) == 1:
    return period.index(new[0])
  else:
    for i in range(len(new)-1):
      start = int(new[i][:2] + new[i][3:])
      end = int(new[i+1][:2] + new[i+1][3:])
      if start <= int(hour + minute) < end:
        return period.index(new[i])
    else:
      return -1