n = int(input())

n_edinici = n % 10
n_stotici = n // 100
n_desetici = (n // 10) - (n_stotici * 10)

if (n_edinici > 0 and n_desetici > 0 and n_stotici > 0):
    for m1 in range(1, n_edinici + 1):
        for m2 in range(1, n_desetici + 1):
            for m3 in range(1, n_stotici + 1):
                result = m1 * m2 * m3
                print(f"{m1} * {m2} * {m3} = {result};")
