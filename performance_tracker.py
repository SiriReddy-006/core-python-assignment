students = {
    "John": [85, 78, 92],
    "Alice": [88, 79, 95],
    "Bob": [70, 75, 80]
}

def calc_avg():
    avgs = {}
    for name in students:

        marks = students[name]
        total = sum(marks)
        count = len(marks)

        avg = total / count
        avgs[name] = round(avg, 2)
    print("Average Marks:", avgs)
    top_name = ""
    top_avg = 0
    for name in avgs:
        if avgs[name] > top_avg:
            top_avg = avgs[name]
            top_name = name
          
    print("Top Performer:", top_name)
  
calc_avg()
