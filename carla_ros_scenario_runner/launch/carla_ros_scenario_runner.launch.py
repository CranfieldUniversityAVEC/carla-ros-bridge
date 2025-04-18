import launch
import os
import launch_ros.actions

# Get the value of the SCENARIO_RUNNER_ROOT environment variable
scenario_runner_root = os.getenv('SCENARIO_RUNNER_ROOT')


def generate_launch_description():
    ld = launch.LaunchDescription([
        launch.actions.DeclareLaunchArgument(
            name='host',
            default_value='localhost'
        ),
        launch.actions.DeclareLaunchArgument(
            name='port',
            default_value='2000'
        ),
        launch.actions.DeclareLaunchArgument(
            name='role_name',
            default_value='hero'
        ),
        launch.actions.DeclareLaunchArgument(
            name='scenario_runner_path',
            default_value=scenario_runner_root
        ),
        launch.actions.DeclareLaunchArgument(
            name='wait_for_ego',
            default_value='True'
        ),
        launch_ros.actions.Node(
            package='carla_ros_scenario_runner',
            executable='carla_ros_scenario_runner',
            name='carla_ros_scenario_runner',
            output='screen',
            emulate_tty='True',
            on_exit=launch.actions.Shutdown(),
            parameters=[
                {
                    'host': launch.substitutions.LaunchConfiguration('host')
                },
                {
                    'port': launch.substitutions.LaunchConfiguration('port')
                },
                {
                    'role_name': launch.substitutions.LaunchConfiguration('role_name')
                },
                {
                    'scenario_runner_path': launch.substitutions.LaunchConfiguration('scenario_runner_path')
                },
                {
                    'wait_for_ego': launch.substitutions.LaunchConfiguration('wait_for_ego')
                }
            ]
        )
    ])
    return ld


if __name__ == '__main__':
    generate_launch_description()
