# def svetafor(name, frequency, main_light, diff, secondary_light, ):
#     start = 1
#     sariq = 4
#     qizil1 = 10
#     a = 10
#     b = 5
#
#     while a > 0:
#         print(name)
#         if start == main_light - diff:
#
#             # while secondary_light > 0:
#                 # if start == main_light:
#                 #     start = 0
#                 # start += 1
#                 # secondary_light -=1
#                 # time.sleep(frequency)
#             # while secondary_light > 0:
#             #     print("Start phase 2")
#             #     secondary_light -= 1
#             #     time.sleep(frequency)
#             #     start = 0
#             # print("Start phase 2")
#             # start = 0
#             # secondary_light = secondary_light
#         start += 1
#
#         a -= 1
#         if a == 0:
#             print(11111111)
#             a = b
#         time.sleep(frequency)
#
#
# main = multiprocessing.Process(target=svetafor, args=("phase 1", 1, 10, 2, 12))
# secondary = multiprocessing.Process(target=svetafor, args=("phase 2", 5, "dadaaada"))
#
# main.start()
# secondary.start()

from datetime import timedelta

phase1 = timedelta(seconds=0)
phase2 = timedelta(seconds=0)
raznitsa = timedelta(seconds=3)
end_phase1 = timedelta(seconds=10)
end_phase2 = timedelta(seconds=20)
# -------------------------------------------------
# while True:
#     print(f"phase_1>>>{phase1}")
#     time.sleep(1)
#     phase1 += timedelta(seconds=1)
#     if phase1 == end_phase1 - raznitsa:
#         # while True:
#         d = 3
#         for a in range(end_phase2.seconds - raznitsa.seconds):
#
#             print(f"phase_2<<<{phase2}")
#             if d > 0:
#                 print(f"phase_1<<<{phase1}")
#             time.sleep(1)
#             d -= 1
#             phase2 += timedelta(seconds=1)
#             phase1 = timedelta(seconds=0)
#
#     phase2 = timedelta(seconds=0)
# --------------------------------------------------
from datetime import timedelta
import time

while True:
    print(f"phase_1---{phase1}")
    time.sleep(1)
    phase1 += timedelta(seconds=1)
    if phase1 == end_phase1 - raznitsa:
        for a in range(end_phase2.seconds - raznitsa.seconds):
            print(f"phase_2>{phase2}")
            time.sleep(1)
            phase2 += timedelta(seconds=1)
            if phase2 == raznitsa:
                print(end_phase1, "end_phase1")
                phase1 = timedelta(0)
    phase2 = timedelta(seconds=0)
