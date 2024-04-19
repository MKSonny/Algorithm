def solution(data, ext, val_ext, sort_by):
    answer = []

    d = {"code": 0, "date": 1, "maximum": 2, "remain": 3}

    sel = d[ext]

    if sel == 1:
        val_ext = str(val_ext)
        ext_year = int(val_ext[:4])
        ext_mount = int(val_ext[4:6])
        ext_day = int(val_ext[6:])

        for item in data:
            date = str(item[1])
            year = int(date[:4])
            mounth = int(date[4:6])
            day = int(date[6:])

            if year < ext_year:
                answer.append(item)
            elif year == ext_year and mounth < ext_mount:
                answer.append(item)
            elif mounth == ext_mount and day < ext_day:
                answer.append(item)
            elif day == ext_day:
                answer.append(item)
    else:
        for item in data:
            if item[sel] <= val_ext:
                answer.append(item)

    answer.sort(key=lambda o: o[d[sort_by]])

    return answer