plot(t, rad2deg(y[:, 3:]))
xlabel('Time [s]')
ylabel('Angular Rate [deg/s]')
legend(["${}$".format(vlatex(s)) for s in speeds])