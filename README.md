# Equitable-4G-Coverage-Optimization

# Satellite Coverage Reallocation Using K-means Clustering

## Overview

This repository contains a Python script that demonstrates the use of K-means clustering to propose coverage reallocation for global dead spots by adjusting the positions of a set number of orbital satellites. The code provides visualizations and quantifiable metrics to evaluate the predicted impact of this reallocation, focusing on coverage improvement and dead spot area reduction.


## Motivation

Satellite coverage plays a vital role in modern communication, navigation, and remote sensing. However, ensuring global coverage can be challenging due to various factors, including orbital dynamics and geographical constraints. This project aims to address this challenge by reallocating satellites using data-driven techniques like K-means clustering. The motivation behind this effort is to:

- **Improve Global Connectivity**: Enhancing satellite coverage leads to improved connectivity in remote or underserved areas, enabling access to vital services and information.

- **Optimize Resource Allocation**: By strategically relocating satellites, we can optimize the use of available resources, reducing redundancy and costs.

- **Enhance Disaster Response**: Improved coverage can expedite disaster response efforts, providing timely communication and navigation support in critical situations.

- **Enable Scientific Research**: Researchers can benefit from enhanced satellite coverage for data collection and analysis in various fields, such as climate science and environmental monitoring.

## Key Features

- **Satellite Reallocation**: The code uses K-means clustering to allocate satellites to areas with dead spots, optimizing coverage.

- **Visualization**: It provides visualizations of the original satellite positions, dead spots, and new satellite positions on a world map.

- **Coverage Heatmaps**: The code generates heatmaps to visualize coverage before and after reallocation, quantifying the impact.

- 

![satellite_reallocation](https://github.com/saduri2004/Equitable-4G-Coverage-Optimization/assets/113476494/02bef6f1-5d78-4253-9a24-c597a70e1d47)
![coverage_before_reallocation](https://github.com/saduri2004/Equitable-4G-Coverage-Optimization/assets/113476494/7051fbea-6ae5-4c2b-b9fa-d39ffc318ffc)
![coverage_after_reallocation](https://github.com/saduri2004/Equitable-4G-Coverage-Optimization/assets/113476494/0a411ecf-7bef-4eb4-a4b3-cce0edb6d1f1)


## Results

The impact of the satellite coverage reallocation is assessed in two key ways:

1. **Coverage Improvement**: The code calculates the predicted improvement in coverage by area. This metric reflects the percentage increase in the area covered by satellites after reallocation.

2. **Dead Spot Area Reduction**: It quantifies the reduction in the total area of dead spots, highlighting the percentage decrease in areas without satellite coverage.
