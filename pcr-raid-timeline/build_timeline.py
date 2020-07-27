import inspect
import roles
import squad
import sys
from timeline import Timeline as timeline

def init_squad() -> None:
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

def get_squad_timeline(role_name: str):
    for var_name, var_value in inspect.getmembers(squad):
        if var_name == role_name:
            return var_value
    return None

def build_timeline(tl: timeline, squad: list) -> timeline:
    for role_name in squad:
        tl = build_timeline_by_role(tl, role_name)
    return tl

def build_timeline_by_role(tl: timeline, role_name: str) -> timeline:
    role = roles.get_role(role_name)
    trigger_dict = get_squad_timeline(role_name)
    if role != None and trigger_dict != None:
        for i in range(0, 90):
            moment = 90 - i
            if role.__contains__("ex"):
                for trigger_point in trigger_dict["ex"]:
                    if trigger_point >= moment and moment > trigger_point - role["ex"]["duration"]:
                        tl.add_status(moment, role["ex"]["name"], role["ex"]["value"], role["ex"]["type"], role["ex"]["private"])
            if role.__contains__("s1"):
                for trigger_point in trigger_dict["s1"]:
                    if trigger_point >= moment and moment > trigger_point - role["s1"]["duration"]:
                        tl.add_status(moment, role["s1"]["name"], role["s1"]["value"], role["s1"]["type"], role["s1"]["private"])
            if role.__contains__("s2"):
                for trigger_point in trigger_dict["s2"]:
                    if trigger_point >= moment and moment > trigger_point - role["s2"]["duration"]:
                        tl.add_status(moment, role["s2"]["name"], role["s2"]["value"], role["s2"]["type"], role["s2"]["private"])
    return tl


if __name__ == "__main__":
    if len(sys.argv) == 1:
        # initialize squad
        init_squad()
    elif len(sys.argv) == 2:
        tl = timeline()
        tl = build_timeline(tl, squad.squad)
        tl.print()
    else:
        pass
