class Timeline(object):
    
    timeline = []

    def __init__(self):
        for i in range(90, 0, -1):
            self.timeline.append({"status": []})
    
    def add_status(self, moment: int, name: str, value: int, type: str, private: bool) -> None:
        self.timeline[90 - moment]["status"].append({"name": name, "value": value, "type": type, "private": private})
    
    def print(self) -> None:
        for i in range(90, 0, -1):
            print("[" + str(i) + "]" + str(self.timeline[90 - i]["status"]))


if __name__ == "__main__":
    timeline = Timeline()
    timeline.add_status(10, "天狼噬斩", 89, "debuff", False)
    timeline.add_status(10, "勇气呐喊", 79, "debuff", False)
    timeline.add_status(8, "勇气呐喊", 79, "debuff", False)
    timeline.print()