import rclpy
from rclpy.node import Node 


class ConfigManager(Node):

    def __init__(self):

        super().__init__('config_manager')

        self.declare_parameter("robot_name", "Robot_1")

        self.declare_parameter("battery_threshold", 20)

        self.declare_parameter("temperature_threshold", 35)

        robot_name = self.get_parameter("robot_name").value

        battery_threshold = self.get_parameter("battery_threshold").value

        temperature_threshold = self.get_parameter("temperature_threshold").value

        if battery_threshold < 10:
            self.get_logger().warning("Battery threshold is too low!")

        if temperature_threshold > 50:
            self.get_logger().warning("Temperature threshold is too high!")

        self.get_logger().info(
            f"Robot Name: {robot_name}"
        )

        self.get_logger().info(
            f"Battery Threshold: {battery_threshold}"
        )

        self.get_logger().info(
            f"Temperature Threshold: {temperature_threshold}"
        )


def main(args=None):

    rclpy.init(args=args)

    node = ConfigManager()

    rclpy.spin_once(node, timeout_sec=1)

    node.destroy_node()

    rclpy.shutdown()

if __name__ == '__main__':
    main()