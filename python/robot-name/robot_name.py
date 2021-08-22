def generate_new_name():
    return "Alex"

class Robot:
    assigned_names = []

    def __init__(self):
        self.name = generate_new_name()
        Robot.assigned_names.append("Alex")


robot = Robot()
print(robot.name)
