from math import *
from Robot import *
from Path import *

class Follower:
    
    def __init__(self, file):
        print('Sending commands to MRDS server', MRDS_URL)
        self.robot = Robot()
        self.path = Path(file)
        self.path = self.path.getPath()
        self.startTime = None
        self.speed = 0.7
        self.aSpeed = 1.3
        self.lookAhead = 1
        
    def follow(self):
        self.startTime = time.time()
        print('GO!')
        while self.path:
            position = self.robot.getPosition()
            heading = self.robot.getHeading()
            newPosition = self.robot.carrotPoint(self.path, position, self.lookAhead)
            
            if newPosition:
                distance = self.robot.getDistance((newPosition['X'] - position['X']),
                                           (newPosition['Y'] - position['Y']))
                bearing = self.robot.getBearing((position['X'], position['Y']),
                                                       (newPosition['X'], newPosition['Y']))
                turnAmount = self.robot.turnAngle(bearing, heading)
                response = self.robot.setMotion(self.speed, turnAmount)
                time.sleep(0.15)
                    
            response = self.robot.setMotion(0,0)
        self.goalTime = time.time()
        print('Goal reached in %.2f seconds.' % (self.goalTime - self.startTime))            
            
if __name__ == '__main__':
    pathFollower = Follower('Path-to-bed.json')
    pathFollower.follow()