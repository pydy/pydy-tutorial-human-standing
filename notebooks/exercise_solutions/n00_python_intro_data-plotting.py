time = arange(0,5,0.1)
a = 1
b = 2
c = 3

f1, f2, f3 = three_sine_waves(time, a, b, c)

plot(time, f1, 'r', time, f2, 'g', time, f3, 'b')
xlabel('x axis')
ylabel('y axis')
legend(['f1', 'f2', 'f3'], 'upper left')