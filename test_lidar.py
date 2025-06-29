import os
import ydlidar
import time

ydlidar.os_init();
ports = ydlidar.lidarPortList();
port = "/dev/ttyUSB0";
laser = ydlidar.CYdLidar();
laser.setlidaropt(ydlidar.LidarPropSerialPort, port);
laser.setlidaropt(ydlidar.LidarPropSerialBaudrate, 115200);
laser.setlidaropt(ydlidar.LidarPropLidarType, ydlidar.TYPE_TRIANGLE);
laser.setlidaropt(ydlidar.LidarPropDeviceType, ydlidar.YDLIDAR_TYPE_SERIAL);
laser.setlidaropt(ydlidar.LidarPropScanFrequency, 10.0);
laser.setlidaropt(ydlidar.LidarPropSampleRate, 3);
laser.setlidaropt(ydlidar.LidarPropSingleChannel, True);

ret = laser.initialize();
if ret:
    ret = laser.turnOn();
    scan = ydlidar.LaserScan();
    while ret and ydlidar.os_isOk() :
        r = laser.doProcessSimple(scan);
        if r:
            print("Scan received[",scan.stamp,"]:",scan.points.size());
            for point in scan.points:
                print("angle:", point.angle, " range: ", point.range)
        else :
            print("Failed to get Lidar Data")
        time.sleep(0.05);
    laser.turnOff();
laser.disconnecting();
