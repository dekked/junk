# В этой задаче вам потребуется написать ассемблерный код, который проверяет поместится ли сумма двух заданных беззнаковых чисел в 32 битовый регистр. Числа поступают на вход в регистрах %eax и %edx. Если сумма чисел не поместится в 32 битный регистр запишите в регистр %eax значение 0, если сумма поместится в 32 битный регистр, то запишите 1. Для выполнения этого задания вам потребуются следующие инструкции:

#     add %src, %dst  - складывает значение в регистре %src со значением в регистре %dst и сохраняет результат в регистр %dst
#     jc branch - передает управление коду с меткой branch, если в результате предыдущей операции произошло беззнаковое переполнение, в противном случае просто пропускается
#     jmp branch - передает управление коду с меткой branch
#     mov $C, %dst - записывает значение C в регистр %dst.

# Sample Input:

# There is no test input

# Sample Output:

# OK