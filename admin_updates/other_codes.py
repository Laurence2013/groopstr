def __group_ids(self, week):
    week_right = []
    week_left = []
    is_end_week = 1
    for i in range(0, len(week)):
        if is_end_week < len(week):
            if week[i] == week[i+1]:
                week_right.append(week[i].get('week_no'))
                week_left.append(week[i+1].get('week_no'))
            is_end_week += 1
    final_week = week_right + week_left
    print(final_week)
    is_end_week2 = 1
    for j in range(0, len(week)):
        if is_end_week2 < len(final_week):
            if week[j].get('week_no') == final_week[is_end_week2]:
                print(week[j].get('week_no'), final_week[is_end_week2])
        is_end_week2 += 1

def __group_ids_1(self, week):
    group_week = []
    is_end_week = 1
    for i in range(0, len(week)):
        if is_end_week < len(week):
            if week[i] == week[i+1]:
                group_week.append(week[i+1].get('week_no'))
        is_end_week += 1
    print(group_week)
    return group_week

def __group_ids_2(self, group_week):
    is_end_week = 1
    for i in range(0, len(group_week)):
        if is_end_week < len(group_week):
            if group_week[i] == group_week[i+1]:
                return True
            is_end_week += 1
    return False

def __group_ids_3(self, group_week):
    group_week2 = []
    is_end_week2 = 1
    for j in range(0, len(group_week)):
        if is_end_week2 < len(group_week):
            if group_week[j] == group_week[j+1]:
                group_week2.append(group_week[j])
                break
            else:
                group_week2.append(group_week[j])
        is_end_week2 += 1
    print(group_week2)
