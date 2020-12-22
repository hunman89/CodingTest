logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
dig = []
let = []
for log in logs:
  if log.split()[1].isdigit():
    dig.append(log)
  else: 
    let.append(log)

let.sort(key=lambda x : (x.split()[1:], x.split()[0]))
print(let+dig)