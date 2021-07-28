import time

from Grabber import scheduleGrabber
from SMS import SMSsend


def scheduleFormatter(schedule):
    """

    :param schedule: schedule Hashmap(Dictionary)
    :return: Formatted string with all schedule information
    """
    dayList = []
    finalStr = ''
    for i in schedule.items():
        dayName, data = i
        data = data.copy()
        try:
            if data[1] == 'OffNoPay':
                data[1] = 'Not Working'
        except(IndexError):
            data.append('Not Working')

        dayText = f'{dayName} {data[0]}\n' \
                  f'{data[1]}'
        dayList.append(dayText)
    for j in dayList:
        finalStr += j + "\n\n"
    return finalStr


# temporarily holds the last schedule for comparison
past = None

# Action Loop
while True:
    x = scheduleGrabber('vw94080', 'w@lker11')
    scheduleRaw = x.getSchedule()
    formatedSchedule = scheduleFormatter(scheduleRaw)
    if past == scheduleRaw:
        print("Already Sent")
        x.closeWindow()
        time.sleep(14400)
    else:
        SMSsend(formatedSchedule)
        past = scheduleRaw
        x.closeWindow()
