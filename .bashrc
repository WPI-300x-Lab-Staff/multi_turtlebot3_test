force_color_prompt=yes
PS1='\[\033[1;36m\]\u\[\033[1;31m\]@\[\033[1;32m\]\h:\[\033[1;35m\]\w\[\033[1;31m\]\$\[\033[0m\] '

SSH_Turtlebot() {
	ssh ubuntu@$1.dyn.wpi.edu
}

PING_Turtlebot() {
	ping $1.dyn.wpi.edu
}

REMAKE_Workspace() {
	source /opt/ros/$(ls /opt/ros)/setup.bash
	cd ~/ak_labs_ws
	rm -r ./build ./devel
	catkin_make
}

source /opt/ros/$(ls /opt/ros)/setup.bash
source ~/catkin_ws/devel/setup.bash

export TURTLEBOT3_MODEL=burger

export ROS_MASTER_URI=http://$(hostname).wpi.edu:11311
export ROS_HOSTNAME=$(hostname).wpi.edu

