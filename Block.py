import sys


class Block(object):
    def __init__(self, sensor_list, start_time):
        self.updateStart_time(start_time)
        self.end_time = 0
        self.sensor_list = []
        self.addAllSensor(sensor_list)

    def addAllSensor(self, sensor_list):
        for i in range(len(sensor_list)):
            self.addSensor(sensor_list[i])

    def updateStart_time(self, start_time):
        self.end_time += start_time - self.start_time
        self.start_time = start_time

    def updateEnd_time(self, sensor):
        if self.start_time + sensor.process_time > self.end_time:
            self.end_time = self.start_time + sensor.process_time

    def addSensor(self, sensor):
        self.sensor_list.append(sensor)
        self.updateEnd_time(sensor)

    def removeSensor(self, sensor):
        self.sensor_list.remove(sensor)
        if self.start_time + sensor.process_time is self.end_time:
            for i in range(len(self.sensor_list)):
                self.updateEnd_time(self.sensor_list[i])

    def changeSensor(self,index, sensor):
        self.updateEnd_time(sensor)
        self.sensor_list[index] = sensor

