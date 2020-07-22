import inspect
import roles
import sys

def init_squad() -> None:
    import squad
    squad_list = squad.squad
    f = open("squad.py", "w+", encoding="utf-8")
    # squad line: squad = ["", "", "", "", ""]
    squad_line = "squad = ["
    for role_name in squad_list:
        squad_line += "\"" + role_name + "\", "
    squad_line += "]"
    squad_line = squad_line.replace(", ]", "]")
    f.write(squad_line + "\n\n")
    # role line: role = { "s2": [], "ex": [] }
    for role_name in squad_list:
        role = roles.get_role(role_name)
        if role != None:
            role_line = role_name + " = { "
            if role.__contains__("ex"):
                role_line += "\"ex\": ["
                for trigger in role["ex"]["timeline"]:
                    role_line += str(trigger) + ", "
                role_line += "], "
            if role.__contains__("s1"):
                role_line += "\"s1\": ["
                for trigger in role["s1"]["timeline"]:
                    role_line += str(trigger) + ", "
                role_line += "], "
            if role.__contains__("s2"):
                role_line += "\"s2\": ["
                for trigger in role["s2"]["timeline"]:
                    role_line += str(trigger) + ", "
                role_line += "], "
            role_line = role_line.replace(", ]", "]")
            role_line += "}"
            role_line = role_line.replace(", }", " }")
            f.write(role_line + "\n")
    f.close()

def init_timeline() -> list:
    timeline = []
    for i in range(90, 0, -1):
        timeline.append(0)
    return timeline

def get_squad_timeline(role_name: str):
    import squad
    for var_name, var_value in inspect.getmembers(squad):
        if var_name == role_name:
            return var_value
    return None

def build_timeline_for_squad(timeline_buff: list, timeline_debuff: list, squad: list) -> list:
    for role_name in squad:
        timeline_buff, timeline_debuff = build_timeline(timeline_buff, timeline_debuff, role_name)
    return timeline_buff, timeline_debuff

def build_timeline(timeline_buff: list, timeline_debuff: list, role_name: str) -> list:
    role = roles.get_role(role_name)
    trigger_dict = get_squad_timeline(role_name)
    if role == None or trigger_dict == None:
        return timeline_buff, timeline_debuff
    else:
        for i in range(0, 90):
            current_second = 90 - i
            if role.__contains__("ex"):
                if role["ex"]["type"] == "buff" and role["ex"]["self"] == False:
                    duration = role["ex"]["duration"]
                    buff = role["ex"]["value"]
                    for trigger_point in trigger_dict["ex"]:
                        if trigger_point >= current_second and current_second > trigger_point - duration:
                            timeline_buff[i] = timeline_buff[i] + buff
                if role["ex"]["type"] == "debuff":
                    duration = role["ex"]["duration"]
                    debuff = role["ex"]["value"]
                    for trigger_point in trigger_dict["ex"]:
                        if trigger_point >= current_second and current_second > trigger_point - duration:
                            timeline_debuff[i] = timeline_debuff[i] + debuff
            if role.__contains__("s1"):
                if role["s1"]["type"] == "buff" and role["s1"]["self"] == False:
                    duration = role["s1"]["duration"]
                    buff = role["s1"]["value"]
                    for trigger_point in trigger_dict["s1"]:
                        if trigger_point >= current_second and current_second > trigger_point - duration:
                            timeline_buff[i] = timeline_buff[i] + buff
                if role["s1"]["type"] == "debuff":
                    duration = role["s1"]["duration"]
                    debuff = role["s1"]["value"]
                    for trigger_point in trigger_dict["s1"]:
                        if trigger_point >= current_second and current_second > trigger_point - duration:
                            timeline_debuff[i] = timeline_debuff[i] + debuff
            if role.__contains__("s2"):
                if role["s2"]["type"] == "buff" and role["s2"]["self"] == False:
                    duration = role["s2"]["duration"]
                    buff = role["s2"]["value"]
                    for trigger_point in trigger_dict["s2"]:
                        if trigger_point >= current_second and current_second > trigger_point - duration:
                            timeline_buff[i] = timeline_buff[i] + buff
                if role["s2"]["type"] == "debuff":
                    duration = role["s2"]["duration"]
                    debuff = role["s2"]["value"]
                    for trigger_point in trigger_dict["s2"]:
                        if trigger_point >= current_second and current_second > trigger_point - duration:
                            timeline_debuff[i] = timeline_debuff[i] + debuff
        return timeline_buff, timeline_debuff

def build_buff_timeline_for_role(timeline_buff: list, role_name: str) -> list:
    role = roles.get_role(role_name)
    trigger_dict = get_squad_timeline(role_name)
    if role == None or trigger_dict == None:
        return timeline_buff
    else:
        for i in range(0, 90):
            current_second = 90 - i
            if role.__contains__("ex"):
                if role["ex"]["type"] == "buff" and role["ex"]["self"] == True:
                    duration = role["ex"]["duration"]
                    buff = role["ex"]["value"]
                    for trigger_point in trigger_dict["ex"]:
                        if trigger_point >= current_second and current_second > trigger_point - duration:
                            timeline_buff[i] = timeline_buff[i] + buff
            if role.__contains__("s1"):
                if role["s1"]["type"] == "buff" and role["s1"]["self"] == True:
                    duration = role["s1"]["duration"]
                    buff = role["s1"]["value"]
                    for trigger_point in trigger_dict["s1"]:
                        if trigger_point >= current_second and current_second > trigger_point - duration:
                            timeline_buff[i] = timeline_buff[i] + buff
            if role.__contains__("s2"):
                if role["s2"]["type"] == "buff" and role["s2"]["self"] == True:
                    duration = role["s2"]["duration"]
                    buff = role["s2"]["value"]
                    for trigger_point in trigger_dict["s2"]:
                        if trigger_point >= current_second and current_second > trigger_point - duration:
                            timeline_buff[i] = timeline_buff[i] + buff
        return timeline_buff

def print_timeline(timeline_buff: list, timeline_debuff: list) -> None:
    # print every 15 seconds in a line
    print_line(timeline_buff, timeline_debuff, 0, 15)
    print_line(timeline_buff, timeline_debuff, 15, 30)
    print_line(timeline_buff, timeline_debuff, 30, 45)
    print_line(timeline_buff, timeline_debuff, 45, 60)
    print_line(timeline_buff, timeline_debuff, 60, 75)
    print_line(timeline_buff, timeline_debuff, 75, 90)

def print_line(timeline_buff: list, timeline_debuff: list, start_time: int, end_time: int):
    str_time =   "time:   "
    str_buff =   "buff:   "
    str_debuff = "debuff: "
    for i in range(start_time, end_time):
        buff = timeline_buff[i]
        debuff = timeline_debuff[i]
        if debuff > 270 and buff > 500:
            color_format = "\033[0;30;44m"
        elif debuff > 270 and buff > 100:
            color_format = "\033[0;30;45m"
        elif 160 < debuff and buff > 100:
            color_format = "\033[0;30;42m"
        elif 80 < debuff and buff > 500:
            color_format = "\033[0;30;42m"
        else:
            color_format = "\033[0m"
        str_time += format(color_format + str(90 - i).rjust(5) + " ") + format("\033[0m")
        str_buff += format(color_format + str(buff).rjust(5) + " ") + format("\033[0m")
        str_debuff += format(color_format + str(debuff).rjust(5) + " ") + format("\033[0m")
    print(str_time)
    print(str_buff)
    print(str_debuff)
    print()

if __name__ == "__main__":
    if len(sys.argv) == 1:
        # initialize squad
        init_squad()
    elif len(sys.argv) == 2:
        # build timeline
        import squad
        timeline_buff = init_timeline()
        timeline_debuff = init_timeline()
        timeline_buff, timeline_debuff = build_timeline_for_squad(timeline_buff, timeline_debuff, squad.squad)
        role_name = sys.argv[1]
        if role_name in squad.squad:
            timeline_buff = build_buff_timeline_for_role(timeline_buff, role_name)
            print_timeline(timeline_buff, timeline_debuff)
        else:
            print_timeline(timeline_buff, timeline_debuff)
    else:
        pass
