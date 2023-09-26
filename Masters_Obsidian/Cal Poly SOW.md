---
author: Kyle Nessen
created: 2023-09-04
Project: "[[Cal Poly SOW]]"
---

# Validating Wind Modeling Methods in Monarch Overwintering Groves
## RFP Language
![[Xerces RFP Language]]
## Background and Introduction
- The multi-generational journey of monarch butterflies is one of the most famous examples of migration in the animal kingdom (National Geographic Society 2022)
- Every year, monarch butterflies in western North America travel up to thousands of miles from their summer breeding grounds to gather in dense clusters along the California coast.
- Critical to the success of monarch migration, is the availability and suitability of overwintering groves along coastal California. 
- Forest structure is thought to provide suitable habitat by creating a microclimate that has favorable temperature, humidity, light availability, and wind protection. 
## Methods
### Overview
- Select a site to conduct the experiment
- Identify where wind data loggers will be placed (both within and outside the grove)
- Install wind data loggers and collect data through overwintering period
- Fly a LiDAR mission using Cal Poly drone
- Create the forest geometry from lidar data using voxels
- Calculate the plant volume density for voxels
- Analyze the wind data for distinct and repeated wind conditions (speed and direction)
- Model those wind conditions in my wind simulation software
- Compare measured results to predicted results
- Adjust tree parameters and rerun simulations
- Repeat until an optimum tree parameter set is found
- Conduct sensitivity analysis
- Report the tree parameters and accuracy of the model for various wind conditions
### Site Selection
- Before instruments are installed, a site needs to be selected
- It should be a reliable monarch overwintering site that is routinely visited each year by monarch butterflies
- Ideally, the site should be free of any topographical complications, such as neighboring hills or residing in deep canyons.
- A quality site will also have minimal obstructions from the prevailing winds, such as sites that are near the ocean. 
- Preferably sites will be secure from the public, but steps can be taken to reduce potential of bad actors tampering with the equipment
- As part of the site selection, a wind study detailing prevailing winds should be conducted to ensure that sufficiently strong storms are likely to occur
- Proximity to a local airport and weather data or other sources of long term wind monitoring data will be helpful during the analysis and during site selection
### Sensor Placement and Data Collection
- The location and number of sensors needs to be determined once the site is selected
- Instruments will mounted to nearby trees, following the design in Saniee and Villablanca paper (figure)
![[Project Requirements Sketch for Pismo Wind Study 2023-08-22 14.09.54.excalidraw]]
-  A site visit will be conducted to assess where sensors can be installed following the design below to create a maximum sensor set
- some subset of those possible locations will be chosen at random within the interior of the grove to minimize against bias
- Sensors will be no closer than 10 meter apart to avoid autocorrelation
- Instruments needs to be placed outside the canopy in the direction of the most common winds in order to capture what wind conditions are like outside
- This is important for the model simulation step, so I know which wind speeds to input 
- Wind data loggers will be installed as early as possible, and allowed to collect data throughout the overwintering period. 
- Periodic data retrieval events will happen throughout the overwintering period, via the access cord as described in the figure above
![[Cal Poly SOW 2023-08-30 17.04.18.excalidraw]]
### LiDAR Dataset
- In order to recreate the forest structure, LiDAR data will be captured of the selected site
- The Cal Poly Environmental Geospatial Systems will lend its UAV aircraft to capture high density point cloud
	- AeroVironment Vapor 55 (UAV)
	- [Yellowscan Explorer](https://www.yellowscan.com/products/explorer/) (LiDAR Sensor)
- Lidar point cloud should have on the order of approximately 200 points per square meter
	- NV5. 2022. “Ellwood Mesa Monarch Butterfly Habitat Characterization.” Goleta, CA: Althouse and Meade, Inc.
- The point cloud should be controlled for maximum geospatial accuracy through the use of ground control points which will be surveyed in by GNSS receivers.
- Horizontal and vertical accuracies of the point cloud should not exceed 10cm
- LiDAR will be flown after monarchs have left the site
- Permissions will be acquired by the authors to fly over the given site depending on its location, and necessary conditions will be met for safety
- All FAA regulations and Cal Poly rules will be followed regarding mission flights
## Analysis
### Forest Geometry and Plant Density

### Analyzing Wind Patterns
### Simulate Wind Patterns in Simulation Software
### Iteratively Test Tree Parameters
### Sensitivity Analysis

## Timeline
![[Cal Poly SOW 2023-09-01 15.49.41.excalidraw]]
## Deliverables

