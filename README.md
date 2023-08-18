# AMAG Framework

## Table of Contents

- [AMAG Framework](#amag-framework)
    - [Introduction](#introduction)
    - [Problem Statement](#problem-statement)
    - [About the Data](#about-the-data)
    - [Installation](#installation)
    - [Usage](#usage)
    - [Object Functional Requirements With Example](#object-functional-requirements-with-example)
    - [Testing](#testing)
    - [Deployment](#deployment)

## Introduction

AMAG Framework is a Python-based framework designed for analyzing and visualizing vector data obtained from videos
showing vehicles driving over a scene. This README provides an overview of the framework's functionality, installation
instructions, and usage examples.

## Problem Statement

One of the core systems of AMAG involves evaluating vector data from vehicle trajectory videos. The framework's purpose
is to provide an object-oriented solution for analyzing and visualizing this data. The framework allows users to segment
data by Id, apply filters, and plot trajectories.

## About the Data

The data is provided in the `data.npy` file and includes columns for index, id, latitude (x), and longitude (y).

## Installation

1. Clone this repository:

   ```sh
   git clone https://github.com/RakibCSE/AMAG_Framework.git
   cd AMAG_Framework
   ```
2. Create virtual environment and activate it:

    ```sh
   python -m venv venv
   source venv/bin/activate
   ```

3. Install required dependencies:

   ```sh
   pip install -r requirements.txt
   ```

## Usage

1. Import the framework in your Python code:

   ```python
   from framework.vehicle_data import VehicleData
   from framework.plotter import Plotter
   ```

2. Create a `VehicleData` instance using the data file path:

   ```python
   data_path = 'path/to/data.npy'
   obj = VehicleData(data_path)
   ```

3. Use the framework's functionalities, such as filtering and plotting:

   ```python
   filtered_segments = obj.filter(length_filter)
   plotter = Plotter()
   plotter.plot(filtered_segments)
   ```

## Object Functional Requirements With Example

- **Segment:** Get data for a specific Id:

  ```python
  id_data = obj.get_data_by_id(1)
  ```

- **Filter:** Filter data based on a custom function:

  ```python
  def length_filter(segment):
      return len(segment) > 10

  filtered_segments = obj.filter(length_filter)
  ```

- **Plot:** Plot segments:

  ```python
  plotter.plot_segments(filtered_segments)
  ```

## Testing

Run unit tests to ensure code correctness:

```sh
python -m unittest discover -s tests
```

## Deployment

This project contains Python scripts that can be executed on various platforms, including local computers, compute
servers, as well as cloud-based environments like Kaggle or Google Colab. While the framework can certainly be deployed
on compute servers, it's not limited to that option alone.
