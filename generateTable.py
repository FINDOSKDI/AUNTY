from generateVectors import *
ok124b60 = genOk(124, 60)
ok124b70 = genOk(124, 70)
ok124b80 = genOk(124, 80)
ok124b90 = genOk(124, 90)
alarm124b60 = genAlarm(124, 60)
alarm124b70 = genAlarm(124, 70)
alarm124b80 = genAlarm(124, 80)
alarm124b90 = genAlarm(124, 90)
ok108b70 = genOk(108, 70)
ok108b80 = genOk(108, 80)
ok108b90 = genOk(108, 90)
alarm108b70 = genAlarm(108, 70)
alarm108b80 = genAlarm(108, 80)
alarm108b90 = genAlarm(108, 90)

for i in range(30):
    print(
        "min. {} &${:.2f}$/${:.2f}$& ${:.2f}$/${:.2f}$ & ${:.2f}$/${:.2f}$ & ${:.2f}$/${:.2f}$ & ${:.2f}$/${:.2f}$ & ${:.2f}$/${:.2f}$ & ${:.2f}$/${:.2f}$  &\\\\[.2ex]".format(i+1, ok124b60[i], alarm124b60[i],
                                    ok124b70[i], alarm124b70[i],
                                    ok124b80[i], alarm124b80[i],                                                                                                                ok124b90[i], alarm124b90[i],
                                    ok108b70[i], alarm108b70[i],
                                    ok108b80[i], alarm108b80[i],                                                                                                                ok108b90[i], alarm108b90[i])
        )
