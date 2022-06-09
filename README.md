# multi_turtlebot3_test

This repository is a simple test in an attempt to recreate a previously observed issue regarding robots loosing connections. It will start all the robots in their namespaces, and when triggered, will execute a recriprocating front and backward motion. 

## Changes needed on the turtlebots
***Make sure you are ssh'd in the robots. Following commands are to be executed on the robots***

The hostnames for the turtlebots need to be set to the machine's name that you will be operating the test from. (Don't forget to `source` the new `.bashrc` after making the changes.) Once that step is done, you will need to add the frame `base_scan` to the namespace in the file `turtlebot3_robot.launch`

Open the file for editing:
```bash
rosed turtlebot3_bringup turtlebot3_robot.launch
```

Change the line 3, such that it reads:
```
<launch>
  <arg name="multi_robot_name" default=""/>
  <arg name="set_lidar_frame_id" default="$(arg multi_robot_name)/base_scan"/>
  .
  .
  .
```

With this change, no more changes are required on the robots. 

## Changes at the host computer
***Make sure you are on the host computer. Following commands are to be executed on the host computer***

You will need to make a change to the file `turtlebot3_gmapping.launch` whose editing rights you may not have. If you do have the writing rights, skip to the next sub-section. 

### Cloning a new turtlebot3 library
Create a new workspace (or `cd` to it if you already have a workspace) and clone the workspace
```bash
cd 
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/src
git clone https://github.com/ROBOTIS-GIT/turtlebot3.git

# or use following if you prefer ssh method
# git clone git@github.com:ROBOTIS-GIT/turtlebot3.git
```

### Clone this repository
```bash
cd ~/catkin_ws/src
git clone https://github.com/WPI-300x-Lab-Staff/multi_turtlebot3_test.git

# or use following if you prefer ssh method
# git clone git@github.com:WPI-300x-Lab-Staff/multi_turtlebot3_test.git
```

### make the workspace

you will need to make the workspace, after you have cloned the repositories
```bash
cd ~/catkin_ws
catkin_make
```

### Replace the gmapping launch file
The file needed for the testing is in the `launch` directory of this repository. Replace the existing file with this one. (As this file has an empty default `multi_robot_name`, you may leave it in the replaced, and may not need to revert the changes.)

```bash
cd ~/catkin_ws/src
mv  multi_turtlebot3_test/launch/turtlebot3_gmapping.launch turtlebot3/turtlebot3_slam/launch/turtlebot3_gmapping.launch 
```

These are all the changes you will need at the host machine

## Running the test

1. Start and connect to the robots as usual. 
2. Open the file to change the robot names:
```bash 
rosed multi_turtlebot3_test multi_turtlebot3_test.launch 
```
3. The git version of the code may have the more/lesser number of robots than you may be testing, and their names may be different. Hence make sure that your host version launch file matches your testing robots. In the file, you will find multiple alterations of the following three lines. This launch config will launch the setup for that one robot. Hence, change the robot name in the field `value` below, and only keep the robot names that you need. Delete/comment out the rest.  
```
    <include file="$(find multi_turtlebot3_test)/launch/single_turtlebot3_test.launch">
        <arg name="multi_robot_name" value="luigi"/>
    </include>
```
4. Launch the robots ***ssh into the robots for this command***
```
roslaunch turtlebot3_bringup turtlebot3_robot.launch multi_robot_name:=<robot_name> __ns:=<multi_robot_name>
```
> Here, the `<robot_name>` refers to the robot's given name. For example, for the robot luigi, the command will look like this:
> `roslaunch turtlebot3_bringup turtlebot3_robot.launch multi_robot_name:=luigi __ns:=luigi`

5. Once you see the `calibration ended` message on all the robots, and the host has done launching process, you can trigger the robot receprocation motion test with the following command:
```bash
rostopic pub /start_motion std_msgs/Bool "data: true"
```

6. The robots should be executing the motion now

> There may be some slight delay in between the robots (they may not be completely in sync with each other) and that is completely fine. 

## To stop the test
To stop the test, publish a `false` message on the same topic:
```bash
rostopic pub /start_motion std_msgs/Bool "data: false"
```
