# В этом задании также необходимо скачать данные на ваш компьютер.

# В данных сохранены две количественные переменные, проверьте гипотезу о равенстве средних этих переменных при помощи t- теста для независимых выборок.

# Если обнаружены значимые различия (p< 0.05), то введите через пробел три числа: среднее значение первой переменной, среднее значение второй переменной, p - уровень значимости. Например:

# 22.45 12.56 0.04

# Если значимые различия не обнаружены, то в поле для ответа введите:

# "The difference is not significant"

# В этой задаче оставьте var.equal = FALSE

df <- read.table("dataset_11504_16.txt")
t.test(df$V1, df$V2)
mean(df$V1)
mean(df$V2)