from matplotlib import pyplot as plt

figure = plt.figure(figsize=(6,6))
ax1 = figure.add_subplot(3, 1, 1)
ax2 = figure.add_subplot(3, 1, 2)
ax3 = figure.add_subplot(3, 1, 3)

#speed
x1 = [10, 13, 16, 19, 22, 25, 28, 31]
low = [1, 0.7, 0.5, 0, 0, 0, 0, 0]
avg = [0, 0, 0.4, 0.6, 1, 0.5, 0, 0]
high = [0, 0, 0, 0, 0, 0.6, 0.8, 1]
ax1.plot(x1,low, color='#e4a3e7')
ax1.plot(x1,avg, color='#fe9305')
ax1.plot(x1,high, color='#01bfcd')
ax1.legend(('low', 'avg', 'high'))

#distance
x2 = [30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85]
low = [1, 0.6, 0.5, 0.3, 0.2, 0, 0, 0, 0, 0, 0, 0]
avg = [0, 0, 0, 0.2, 0.4, 0.8, 1, 0.9, 0.6, 0.3, 0, 0]
high = [0, 0, 0, 0, 0, 0, 0, 0, 0.4, 0.7, 0.9, 1]
ax2.plot(x2, low, color='#e4a3e7')
ax2.plot(x2, avg, color='#fe9305')
ax2.plot(x2, high, color='#01bfcd')
ax2.legend(('low', 'avg', 'high'))

rect1 = plt.bar([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 0.6, 0.4, 0, 0, 0, 0, 0, 0, 0], color='#e4a3e7')
rect2 = plt.bar([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [0, 0, 0.2, 0.5, 1, 0.6, 0.4, 0, 0, 0], color='#fe9305')
rect3 = plt.bar([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [0, 0, 0, 0, 0, 0, 0.3, 0.6, 0.8, 1], color='#01bfcd')
plt.legend((rect1, rect2, rect3), ('low', 'avg', 'high'))

plt.show()

print("Введите скорость машины в м/с:")
s = int(input())
print("Введите расстояние до машины:")
d = int(input())

#функции принадлежности
def low_speed(s):
    a = 10
    b = 19
    if (s <= a):
        return 1.0
    elif (s > a and s < b):
        return round((b - s)/(b - a), 1)
    else:
        return 0.0

def avg_speed(s):
    a = 13
    b = 22
    c = 28
    if  (s <= a):
        return 0.0
    elif (s > a and s <= b):
        return round((s - a)/(b - a), 1)
    elif (s >= b and s < c):
        return round((c - s)/(c - b), 1)
    else:
        return 0.0

def high_speed(s):
    a = 22
    b = 31
    if (s <= a):
        return 0.0
    elif (s > a and s <= b):
        return round((s - a)/(b - a), 1)
    else:
        return 1.0

def low_distance(d):
    a = 30
    b = 55
    if (d <= a):
        return 1.0
    elif (d > a and d < b):
        return round((b - d)/(b - a), 1)
    else:
        return 0.0

def avg_distance(d):
    a = 40
    b = 60
    c = 80
    if  (d <= a):
        return 0.0
    elif (d > a and d <= b):
        return round((d - a)/(b - a), 1)
    elif (d >= b and d < c):
        return round((c - d)/(c - b), 1)
    else:
        return 0.0

def high_distance(d):
    a = 65
    b = 85
    if (d <= a):
        return 0.0
    elif (d > a and d <= b):
        return round((d - a)/(b - a), 1)
    else:
        return 1.0


#база правил и степень активизации правил
rule1 = min(high_speed(s), low_distance(d)) #high_power
rule2 = min(high_speed(s), avg_distance(d)) #avg_power
rule3 = min(high_speed(s), high_distance(d)) #low_power

rule4 = min(avg_speed(s), low_distance(d)) #high_power
rule5 = min(avg_speed(s), avg_distance(d)) #avg_power
rule6 = min(avg_speed(s), high_distance(d)) #low_power

rule7 = min(low_speed(s), low_distance(d)) #avg_power
rule8 = min(low_speed(s), avg_distance(d)) #low_power
rule9 = min(low_speed(s), high_distance(d)) #low_power

#определение степени активизации
high_power = max(rule1, rule4)
avg_power = max(rule2, rule5, rule7)
low_power = max(rule3, rule6, rule8, rule9)

result1 = 1*(min(1, low_power)) + 2*(min(0.6, low_power)) + 3*(max(min(0.4, low_power), min(0.2, avg_power))) + \
          4*(min(0.5, avg_power)) + 5*(min(1, avg_power)) + 6*(min(0.6, avg_power)) + \
          7*(max(min(0.4, avg_power), min(0.3, high_power))) + 8*(min(0.6, high_power)) + \
          9*(min(0.8, high_power)) + 10*(min(1, high_power))

result2 = (min(1, low_power)) + (min(0.6, low_power)) + (max(min(0.4, low_power), min(0.2, avg_power))) + \
          (min(0.5, avg_power)) + (min(1, avg_power)) + (min(0.6, avg_power)) + \
          (max(min(0.4, avg_power), min(0.3, high_power))) + (min(0.6, high_power)) + \
          (min(0.8, high_power)) + (min(1, high_power))
if (d >= 90):
    result = 0
elif (d <= 15):
    result = 10
else:
    result = round(result1/result2)

print("Мощность лампы:", result, "Ватт")