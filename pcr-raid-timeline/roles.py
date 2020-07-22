import sys
import inspect

黑骑 = {
    "name": "纯",
    "s2": {
        "name": "护甲破坏",
        "type": "debuff",
        "self": False,
        "value": 59,
        "duration": 12,
        "timeline": [82, 69, 52, 36, 19, 2]
    }
}

偶像 = {
    "name": "望",
    "ex": {
        "name": "演出开始",
        "type": "buff",
        "self": False,
        "value": 446,
        "duration": 18,
        "timeline": []
    }
}

狼 = {
    "name": "真琴",
    "ex": {
        "name": "天狼噬斩",
        "type": "debuff",
        "self": False,
        "value": 89,
        "duration": 18,
        "timeline": [62, 43, 22, 4]
    },
    "s2": {
        "name": "勇气呐喊",
        "type": "debuff",
        "self": False,
        "value": 79,
        "duration": 12,
        "timeline": [82, 69, 51, 35, 18, 1]
    }
}

猫拳 = {
    "name": "日和",
    "s2": {
        "name": "猫咪组合拳",
        "type": "buff",
        "self": True,
        "value": 1089,
        "duration": 12,
        "timeline": []
    }
}

熊锤 = {
    "name": "绫音",
    "s2": {
        "name": "噗吉飓风击",
        "type": "debuff",
        "self": False,
        "value": 20,
        "duration": 12,
        "timeline": [82, 69, 51, 35, 18, 1]
    }
}

病娇 = {
    "name": "惠理子",
    "s1": {
        "name": "痴迷执念",
        "type": "buff",
        "self": True,
        "value": 743,
        "duration": 12,
        "timeline": []
    }
}

兔子 = {
    "name": "美美",
    "s2": {
        "name": "兔兔应援",
        "type": "buff",
        "self": False,
        "value": 297,
        "duration": 12,
        "timeline": [82, 70, 52, 30, 14]
    }
}

忍 = {
    "name": "忍",
    "ex": {
        "name": "亡灵恐惧",
        "type": "debuff",
        "self": False,
        "value": 42,
        "duration": 18,
        "timeline": [82, 70, 51, 35, 18, 2]
    },
    "s2": {
        "name": "虚弱亡魂",
        "type": "debuff",
        "self": False,
        "value": 15,
        "duration": 12,
        "timeline": [78, 61, 45, 28, 11]
    }
}

可可萝 = {
    "name": "可可萝",
    "ex": {
        "name": "极光",
        "type": "buff",
        "self": False,
        "value": 446,
        "duration": 18,
        "timeline": [47, 19]
    },
    "s2": {
        "name": "加速",
        "type": "buff",
        "self": False,
        "value": 114,
        "duration": 12,
        "timeline": [82, 67, 51, 34, 20]
    }
}

深月 = {
    "name": "深月",
    "s2": {
        "name": "蔷薇领域",
        "type": "debuff",
        "self": False,
        "value": 119,
        "duration": 8,
        "timeline": [82, 68, 50, 34, 17]
    }
}

暴击弓 = {
    "name": "铃奈",
    "s2": {
        "name": "魅力全开",
        "type": "buff",
        "self": True,
        "value": 1485,
        "duration": 12,
        "timeline": [80, 68, 50, 31, 14]
    }
}

女仆 = {
    "name": "铃莓",
    "ex": {
        "name": "旋风气流",
        "type": "debuff",
        "self": False,
        "value": 42,
        "duration": 18,
        "timeline": [82, 70, 51, 35, 18, 2]
    }
}

黑猫 = {
    "name": "凯露",
    "s2": {
        "name": "护甲削弱",
        "type": "debuff",
        "self": False,
        "value": 40,
        "duration": 12,
        "timeline": [81, 67, 49, 31, 13]
    }
}

千歌 = {
    "name": "千歌",
    "s1": {
        "name": "激励之歌",
        "type": "buff",
        "self": False,
        "value": 792,
        "duration": 12,
        "timeline": []
    }
}


def get_role(role_name: str):
    for var_name, var_value in inspect.getmembers(sys.modules[__name__]):
        if var_name == role_name:
            return var_value
    return None