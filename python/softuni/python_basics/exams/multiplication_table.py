n = int(input())

n_edinici = n % 10
n_stotici = n // 100
n_desetici = (n // 10) - (n_stotici * 10)

m1 = 1
m2 = 1
m3 = 1

if (n_edinici > 0 and n_desetici > 0 and n_stotici > 0):
    for i in range(1, n_stotici + 1):
        result = m1 * m2 * i
        print(f"{m1} * {m2} * {i} = {result};")
        if i >= n_stotici:
            while True:
                m2 += 1
                for i in range(1, n_stotici + 1):
                    result = m1 * m2 * i
                    print(f"{m1} * {m2} * {i} = {result};")
                if m2 >= n_desetici:
                    m2 = 1
                    break
            while True:
                m1 += 1
                for i in range (1, n_stotici + 1):
                    result = m1 * m2 * i
                    print(f"{m1} * {m2} * {i} = {result};")
                while True:
                    m2 += 1
                    for i in range(1, n_stotici + 1):
                        result = m1 * m2 * i
                        print(f"{m1} * {m2} * {i} = {result};")
                    if m2 >= n_desetici:
                        m2 = 1
                        break
                if m1 >= n_edinici:
                    break