# ROS2 Robot Config Manager

## Overview

ROS2 Robot Config Manager is a simple ROS2 Python package that demonstrates how to use ROS2 Parameters for robot configuration management.

The node loads robot settings such as robot name, battery threshold, and temperature threshold. Parameters can be configured using default values, command-line arguments, or YAML configuration files.

---

## Features

* Declare ROS2 parameters
* Read parameter values
* Override parameters from the command line
* Load parameters from YAML files
* Validate parameter values
* Display warning messages for unsafe configurations

---

## Parameters

| Parameter             | Default Value | Description                          |
| --------------------- | ------------- | ------------------------------------ |
| robot_name            | Robot_1       | Robot identifier                     |
| battery_threshold     | 20            | Minimum battery level before warning |
| temperature_threshold | 35            | Maximum safe temperature             |

---

## Run with Default Parameters

```bash
source install/setup.bash

ros2 run robot_config_manager config_manager
```

### Example Output

```text
Robot Name: Robot_1
Battery Threshold: 20
Temperature Threshold: 35
```

---

## Override Parameters from CLI

```bash
ros2 run robot_config_manager config_manager --ros-args \
-p robot_name:=WarehouseBot \
-p battery_threshold:=15 \
-p temperature_threshold:=45
```

### Example Output

```text
Robot Name: WarehouseBot
Battery Threshold: 15
Temperature Threshold: 45
```

---

## Load Parameters from YAML

### robot_params.yaml

```yaml
robot_config_manager:
  ros__parameters:
    robot_name: WarehouseBot
    battery_threshold: 15
    temperature_threshold: 45
```

### Run

```bash
ros2 run robot_config_manager config_manager \
--ros-args \
--params-file src/ros2-robot-config-manager/robot_config_manager/config/robot_params.yaml
```

---

## Validation Examples

Low Battery Warning:

```text
Battery threshold is too low!
```

High Temperature Warning:

```text
Temperature threshold is too high!
```

---

## Project Structure

```text
robot_config_manager/
├── config/
│   └── robot_params.yaml
├── robot_config_manager/
│   ├── __init__.py
│   └── config_manager.py
├── package.xml
├── setup.py
├── setup.cfg
└── README.md
```

---

## Technologies Used

* ROS2 Jazzy
* Python
* rclpy
* YAML Configuration Files
* Git & GitHub

---

## Learning Objectives

This project demonstrates:

* ROS2 Parameters
* Parameter Overrides
* YAML Parameter Files
* ROS2 Node Configuration
* Basic Validation Logic
* ROS2 Package Development
