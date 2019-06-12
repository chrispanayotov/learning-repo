number = int(input())

n_edinici = number % 10
n_stotici = number // 100
n_desetici = (number // 10) - (n_stotici * 10)

rows = n_stotici + n_desetici
columns = n_stotici + n_edinici
new_line = "\n"

for row in range(rows):
    for column in range(columns):
        if number % 5 == 0:
            number -= n_stotici
            print(f"{number} ", end='')
        elif number % 3 == 0:
            number -= n_desetici
            print(f"{number} ", end='')
        else:
            number += n_edinici
            print(f"{number} ", end='')
    print(new_line.strip())