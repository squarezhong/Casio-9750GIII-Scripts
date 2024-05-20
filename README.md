# Casio-9759GIII-Scripts

## 1. Introduction

Simple python scripts for the Casio fx-9750GIII (9860) calculator.

## 2. Usage

1. Connect the calculator to the computer via USB cable.
2. Copy the script to the [Program] folder in the root directory of the calculator.
3. [MENU] -> [PYTHON] -> select the script to run.
4. Follow the instructions on the screen.

## 3. Scripts

> Since these code finally run on Casio calculator, python-minifier is used to minify the scripts.

### 3.1 Robotics
#### 3.1.1 rotation conversion
- a = axis-angle,
- e = euler angles,
- r = rotation matrix,
- q = quaternion
- o = others (all)


ps1. right-hand coordinate system

ps2. euler angles have 12 different representations, the script use body (intrinsic) 3-2-1 sequence.

**Conversion to euler angles is better avoided, since it is non-linear and has singularities.**

ps3. intrinsic 3-2-1 sequence = extrinsic 1-2-3 sequence (内旋与外旋)

- a2o.py: convert axis-angle to others
- e2o.py: convert euler angles to others
- r2o.py: convert rotation matrix to others
- q2o.py: convert quaternion to others
- qmq.py: Multiply two quaternions

#### 3.1.2 forward kinematics
To be continued...

## Contribution
1. Fork the repository
2. Create a new branch
3. Commit the changes and push to the remote
5. Create a pull request

## License
MIT License
