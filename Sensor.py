class Sensor(object):
    def __init__(self,process_time, due_date):
        self.process_time = process_time
        self.due_date = due_date

    def tardy_time(self, end_time):
        return end_time - self.due_date


