from setuptools import setup

package_name = 'my_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='hyeonjoonpark',
    maintainer_email='hyeonjoonpark@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'simplepub = my_pkg.simplepub:main'
            'simplepub2 = my_pkg.simplesub:main'
            'simpletimepub = my_pkg.simpletimepub:main'
            'simpletimesub = my_pkg.simpletimesub:main'
        ],
    },
)
