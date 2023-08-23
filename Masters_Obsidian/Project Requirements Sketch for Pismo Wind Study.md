Kyle Nessen
August 22nd, 2023
# Background
In my consulting work, I have developed wind modeling methods to gain more insight into how  monarch overwintering groves create wind protection, and how proposed actions may change those wind conditions. While these methods appear to work for relative measures, they have not been validated with real world observations. 

The study outlined below is my current thinking on how to go about a validation exercise of wind simulations in monarch groves.
# Study Site
Pismo Monarch Grove presents an exciting study site for several reasons:

1. Pismo is a reliable site that routinely ranks among the largest in any overwintering season
2. Existing monitoring efforts will complement this study and vice versa
3. The site sits in a topographical "simple" context, with few nearby confounding terrain features such as hillsides or deep valleys
4. Pismo Monarch Grove is a popular attraction where the public can have an excellent introduction to the monarch migration story, warranting prioritization for conservation efforts that this study may facilitate 

However, because of the grove's popularity and uncommon public access there are several constraints that this study must design around:

1. Any instrumentation that is installed needs to be out of reach of potential vandalism
2. Sensors must not be excessive in their visual intrusion and potential for interfering with monarch butterflies
3. Access to the sensors for data retrieval needs to be minimized in order to not encourage other members of the public to access off limit areas

These constraints are workable, however, which I outline below. 
# Wind Sensors and Their Placement
We propose to install [RainWise WindLog](https://rainwise.com/windlog-wind-data-logger) data loggers as the primary instrument for this study. 

These sensors were used in a previous monarch study,[Hierarchy and Scale Influence the Western Monarch Butterfly Overwintering Microclimate by Saniee and Villablanca](https://www.frontiersin.org/articles/10.3389/fcosc.2022.844299/full), and we propose to mount this sensors in a similar way to address the constraints mentioned in the previous section. It's worth noting that the configuration presented below was deployed in nine overwintering sites for an entire season without an incident of vandalism or observable disturbance to the monarch butterflies. 
## Tree Mounting Design
The design for installing these sensors within the grove is detailed in the figure below. 

A pivot joint will be strapped to a suitable tree using non-invasive means. A 30ft telescoping pole will be attached to this pivot joint, and hoisted to the desired elevation by means of metal cable that utilizes a supporting branch. The wind sensor (WindLog anemometer) will be mounted at the end of this pole, with an attached nylon "access" cord, which will run through the telescoping pole into a lock box at the base of the tree. This will allow the sensor to be lowered and hoisted back up without the need for biologists or trained professionals to climb the tree to retrieve data. The lock box will be out of reach for the public, and can be accessed via a small ladder. 

![[Project Requirements Sketch for Pismo Wind Study 2023-08-22 14.09.54.excalidraw]]

## Number of Sensors and Placement
Wind sensors will be installed as described above at various locations inside and outside the grove. The goal is to maximize the diversity of samples that are experienced during the overwintering season with the fewest number of sensors.

I plan to study this more formally, by running simulations of the grove under many different conditions (varying wind direction and speed). This will produce a population of predicted wind speeds at any location within the grove. Using an algorithm called maximum entropy, it is then possible to assess how much "new information" is gained with the placement of each additional sensor. This will allow me to robustly ensure I am capturing the data necessary before conducting the experiment.

The figure below shows some preliminary points that may be used in the final sensor layout. 

Important to note that there are sensors on the periphery of the grove and also within it. We may include sensors at known clustering sites if it is feasible. 

Having sensors on the outside allows me to know what were the wind speeds before entering the grove, so I have numbers to compare against. 

It will be important to get high accuracy points for the sensors, which can be done using Althouse and Meade RTK equipment. This will allow me to control the spatial component so I am making valid numerical comparisons of wind speed.

![[Approximate project requirements for Pismo Wind Study 2023-08-22 13.23.31.excalidraw]]

## Data Retrieval and Duration
Ideally, data would be retrieved from the sensors at a regular interval. There is no wireless communication protocols with these sensors, so to access the data, we need to physically connect to the sensors. 

In the tree mounting figure, I describe how an access cord can be used to lower and raise the sensor for this purpose. It was used successfully in Kiana's project. 

The sensors are limited to 1MB of storage, and each row of data takes approximately 14 bytes of data. Based on that information, here is a table of how long to fill the memory for the available recording intervals:

|Interval (minutes)|Time to 100% Memory (days)|
|---|---|
|1|52|
|2|104|
|5|260|
|10|520|
|15|780|
|20|1040|
|30|1560|
|60|3120|

Based on these intervals, we are not limited by memory storage, and can choose any interval we like, given that data access is possible. It would be best to regularly visit the sensors to make sure they are working and recording data (weekly to biweekly), in which case I would pick **1 min**, but if we can't access the data at all, it appears 5 mins will be more than sufficient.

The sensors will be installed in September and run from the beginning of the overwintering season (October 1st, 2023) till the monarchs have left sometime in February to March. After which point they will be taken down by trained professionals.

## Sensor Reliability
Unfortunately, the wind sensors did not work for Kiana, or she was unable to make them work. This has caused some concern about whether to use them for the study presented here.

I have done some independent tests, and at least on two of the sensors, the appear to be working reliably. 

Below is a test I ran today. I hung both sensors upside down and placed a **stationary** fan pointed at the two wind meters. I let them run at 1 min intervals for several hours. Below are the graphs.

The initial spike at the beginning of both charts seems common when connecting or formatting the wind meters. There should be steps to "clip" in to the data set to avoid effects when interacting with the sensors.

Otherwise, the graphs look as you would expect. A steady average wind (blue) and fluctuating values of the max wind speed (gust, red).

If the sensors were having issues, I would expect big deviations from in the blue or red lines, but everything seems to agree under these controlled conditions.

![[FunStorm_upside_down.png]]

![[LlamaLog_upside_down.png]]

# Validation of Simulation Methods
Once the overwintering season is over. The wind sensors will be taken down, and any remaining wind data will be collected. 

I will fly the site sometime in the spring with a Cal Poly LiDAR drone to get a current, high resolution point cloud of the site. I will then take this data and recreate the site in my wind modeling software. I'll extract a number of observed wind scenarios from the wind sensors, and recreate it in my model. I will then compare predicted measurements versus actual, and will refine my model parameters till they agree.
# Outcomes
If this project is successful, I will be able to calibrate my wind modeling methods to real world numbers. Hopefully, the predicted values agree well with the measured wind speeds, and is robust to small changes in the model or input parameters. 

The implication of such a model is that we can more reliably test and investigate how proposed actions (such as restoration) will behave in the near and long term. It gives us a tool to test hypotheses, and make defensible claims against project impacts. 

For Pismo Monarch Grove specifically, we will have an updated, high resolution lidar dataset of the site, and a state of the art wind study of the grove. This should prove helpful in future grove management decisions.

