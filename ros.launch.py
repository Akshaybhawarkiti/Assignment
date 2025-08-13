from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='myrob',
            executable='camera',
            name='camera_node'
        ),
        Node(
            package='myrob',
            executable='editing',
            name='feed_editor_node'
        ),
        Node(
            package='myrob',
            executable='ui',
            name='ui_node'
        ),
        Node(
            package='myrob',
            executable='output',
            name='output_node'
        )
    ])

