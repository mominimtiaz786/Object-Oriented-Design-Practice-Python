from .order_command import OrderCommand

class OrderManager:
    def __init__(self):
        self.command_queue: list[OrderCommand] = []

    def addCommand(self, command: OrderCommand):
        self.command_queue.append(command);

    def executeCommands(self):
        for command in self.command_queue:
            command.execute()
        self.command_queue.clear()
