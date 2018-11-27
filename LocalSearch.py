import random

from Block import Block


def swapS(block_list ,i1, i2):
    block1 = block_list[i1]
    block2 = block_list[i2]
    i1 = random.randint(len(block1))
    i2 = random.randint(len(block2))
    temp = block1.sensor_list[i1]
    block1.changeSensor(i1, block2.sensor_list[i2])
    block2.changeSensor(i2, temp)


def shilfS(block_list ,i1, i2):
    block1 = block_list[i1]
    block2 = block_list[i2]
    i1 = random.randint(len(block1))
    block2.addSensor(block2.sensor_list[i1])
    block1.removeSensor(block1.sensor_list[i1])


def swapB(block_list, i1, i2):
    temp = block_list[i1]
    block_list[i1] = block_list[i2]
    block_list[i2] = temp


def shiftB(block_list, i1, i2):
    temp = block_list[i1]
    block_list.remove(temp)
    block_list.insert(i2 - 1, temp)


def breakdownB(block_list, index):
    sensor_list = []
    n = random.randint(len(block_list[index]))
    for i in range(n):
        sensor = block_list[index].sensor_list[i]
        sensor_list.append(sensor)
        block_list[index].sensor_list.remove(sensor)
    newBlock = Block(sensor_list, block_list[index - 1].end_time)
    block_list[index].updateStart_time(newBlock.end_time)
    block_list.insert(index, newBlock)


def combineB(block_list, i1, i2):
    temp = block_list[i2]
    block_list.remove(temp)
    block_list[i1].addAllSensor(temp.sensor_list)


