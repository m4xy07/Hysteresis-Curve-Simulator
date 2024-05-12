# Hysteresis Curve Simulator
This program is a simple hysteresis curve simulator that allows you to explore the behavior of hysteresis curves by adjusting three sliders.

## What is a Hysteresis Curve?
A hysteresis curve is a graphical representation of the relationship between two variables, where the output variable lags behind the input variable due to the system's internal delay or memory. In other words, the output variable depends not only on the current input value but also on the history of previous input values.

Hysteresis curves are commonly observed in physical systems, such as magnetic materials, where the magnetic field strength and magnetization are related by a hysteresis loop.

## How to Use the Simulator
The hysteresis curve simulator consists of a graph and three sliders. The graph displays the hysteresis curve, and the sliders allow you to adjust the parameters of the curve.

The three sliders have the following functions:

**Amplitude (A)**: This slider adjusts the amplitude of the hysteresis curve. The amplitude determines the maximum and minimum values of the output variable.
**Frequency (B)**: This slider adjusts the frequency of the hysteresis curve. The frequency determines how often the output variable oscillates between its maximum and minimum values.
**Phase Shift (C)**: This slider adjusts the phase shift of the hysteresis curve. The phase shift determines the time delay between the input and output variables.
To use the simulator, simply adjust the sliders and observe the resulting hysteresis curve on the graph. The graph will update in real-time as you move the sliders.

To reset the graph, click the **"Clear"** button.

## Requirements
Python 3.x
Matplotlib
Tkinter


## Installation
To install the required packages, run the following command:

> pip install matplotlib tk

## Usage
To run the simulator, download the `hysteresis_simulator.py` file and execute it using the Python interpreter:

> python hysteresis_simulator.py

## License
This program is released under the MIT License. See the LICENSE file for details.