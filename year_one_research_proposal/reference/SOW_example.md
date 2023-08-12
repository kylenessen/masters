# Scope of Work: Technical Support of WHPP 2023-2024

**Francis Villablanca, Ph.D.**

**California Polytechnic State University, San Luis Obispo**

**12 May 2023**

## Background and Introduction

The State Vehicular Recreation Areas (SVRAs) employ a Wildlife Habitat Protection Plan ([WHPP](https://ohv.parks.ca.gov/pages/1140/files/07-28-2021-5D-Wildlife%20Habitat%20Protection%20Plan%20(WHPP)%20Framework.pdf)). In regards to wildlife resources, the explicit purpose of the WHPP is to "Prepare and implement management and wildlife habitat protection plans for lands in… state vehicular recreation areas" and "compile and, when determined by the department to be necessary, periodically review and update an inventory of wildlife populations and prepare a wildlife habitat protection plan that conserves and improves wildlife habitats."  As the WHPP at the Oceano Dunes State Vehicular Recreation Area (ODSVRA) works to understand management relevant ecosystem health, wildlife populations, including small mammals, is a primary focus.  Cal Poly San Luis Obispo and California State Parks have been collaborating to study small mammal population dynamics at the ODSVRA as part of the park's WHPP (previously HMS2) program. This previous work has studied small mammal population dynamics (Villablanca 2017), monitoring methodologies (Hopkins et al. (a) _in prep_), and occurrence (Hopkins et al. (b) _in prep_), both with regards to detection sensitivity and user feasibility and workload sustainability.  While some questions have been answered thus far, additional work is needed.  Specifically, additional monitoring-based data collection and analysis, and work to ensure a full transfer of data collection and analytical methods to managers is needed.

The ODSVRA contains vegetation islands separated by large areas of open sand. The open sand is natural foredune and active dune habitat as well as open riding areas (ORA). The ORAs are used for Off Highway Vehicle (OHV) recreation. Small mammal populations exist across ODSVRA, on vegetation islands (I) surrounded by OHV (I-OHV), vegetation islands not (N) surrounded by OHV (I-NOHV), and areas not characterized as islands (NI) that are not exposed to OHV (NI-NOHV).  Small mammals, or rodents, are a diverse wildlife group whose population are often responsive to habitat attributes (Villablanca 2017).Studying small mammals across the park allows management to understand the effect of OHV activity and of fragmentation on these populations.  Since the park actively manages and restores vegetation, the study of small mammals also allows insight into the effect of these actions on wildlife populations.

Work to date has shown that small mammal populations occur throughout the ODSVRA and habitat characteristics (OHV activity, fragmentation, and restoration) can influence their populations (Hopkins et al. (b) _in prep._).  As these factors change over time (e.g.: increased restoration, decreased OHV activity, etc.), it is important for management to have the ability to continue monitoring small mammal populations to understand the effect of these changes.  We have made important advances that facilitate this monitoring by developing lower effort methodology to monitor small mammals and powerful but expedient analyses that can be conducted for inference (Hopkins et al. (b) _in prep_.).  However, additional work is needed to ensure management can continue these advanced strategies in the long term and independently.

Previous work has demonstrated the reduced effort and subsequent workload sustainability of monitoring small mammals through baited camera traps combined with machine learning (ML) models to process images (Hopkins et al. (a) _in prep_).  Our work has also shown that, with this methodology, calculations of species occurrence can be obtained using skills already possessed by park personnel.  Through a transition year, where Cal Poly personnel conducts monitoring and analysis alongside Park personnel, State Parks will become proficient at monitoring small mammals independently to derive inferences on species occurrence over time and effects of changes due to management actions.

Herein, we propose to use the current state of knowledge to conduct small mammal monitoring and in the process train and assist State Parks staff to continue their small mammal monitoring into the future.  This proposal will focus on making small mammal monitoring as sustainable and practical to Parks staff as possible.  In addition, steps will be taken to facilitate the transition to more complex analytic methods thus ensuring State Park staff ultimately adopt independent monitoring.  Thus, the six research objectives outlined below are intended to facilitate transferring the new monitoring methodology to State Parks employment, their gathering of the necessary insight to do so in the future, and providing the needed assistance so there is no lapse in data collection and analysis.

## Objective 1. Long Term Monitoring of Small Mammal Occurrence with Cameras

### Background:

Previous work at Oceano Dunes demonstrated the effectiveness and efficiency of camera trapping small mammals for occupancy analysis compared to the previous method of live trapping (Hopkins et al. (a) _in prep_).  This work showed that cameras, combined with a machine learning (ML) model to process the images, provide a much lower-effort method thus making monitoring of small mammals across the park more sustainable. A ML model was created during this work and has been trained on the seven small mammal species of management interest.  This model will be used to facilitate and reduce effort of camera trapping.  Therefore, by using cameras with ML image processing, versus live traps, monitoring of small mammals can be continued by analyzing small mammal occurrence data from across the habitats in the park.

In addition to demonstrating the drastically reduced effort of camera trapping compared to live trapping, the recent work (Hopkins et al. (a) _in prep_.) found that cameras provide far superior detection of rodents.  With this high detection probability achieved through cameras, data analysis can be streamlined thus providing management a more sustainable method.  Specifically, occupancy models (MacKenzie et al. 2002) that require in-depth knowledge of model analysis and model selection, and are run in the programming language R, are not required under the streamlined approach.  Instead, Hopkins et al. (a) (_in prep_.) found that naïve estimates (MacKenzie et al. 2002) provide almost identical results (1% difference) and do not require knowing and using coding software for statistical selection of occupancy model or their estimators.  The advantage of using cameras and naive occupancy is the simplicity and reduction in effort. The disadvantage is that only more complex analyses of occupancy allow an assessment of the influence of detection probabilities and sample sizes on the inference.  We propose the advantages outweigh the disadvantages given this method's practicality and accessibility to park personnel thereby providing for continued independent monitoring following the competition of this grant.

#### Specific camera monitoring proposal

1. Conduct camera trapping across six plots to monitor small mammal occurrence. The plots will be spread throughout the park and encompass two plots for each of the three plot types (I-OHV, I-NOHV, NI-NOHV) to obtain representative samples.
2. Obtain base line (2023-2024) naive occupancy estimates for small mammal species across the six representative plots for comparisons over time.
3. Train parks staff on camera trapping protocol and data collection methods so monitoring can continue independently of Cal Poly following completion of this grant. 
4. Train parks staff on image processing through ML model so processing can continue independently following completion of this grant.
5. Train parks staff on naive occupancy analysis so analysis can continue independently following completion of this grant.

### Methods:

#### Islands and Plots 
All six plots are existing and have a grid of sixteen stations, in a 4 x 4 array, with stations at 20-meter intervals. The most common plant alliances in the ODSVRA are Willow/Wax Myrtle, and Lupine/Mock Heather (Villablanca 2017). Therefore, in order to be representative, all plots are placed so they sample 50% of each alliance. Cameras will be placed at every other station on the grid, for a total of 8 camera stations per plot.  Half of the stations (4) will be placed in the Willow/Wax Myrtle alliance and half (4) will be placed in the Lupine/Mock Heather alliance.

#### Plot selection
We propose to sample two I-NOHV plots, two I-OHV plots, and two NI-NOHV plots.  This study design will provide equal representation for each plot type.  The I-NOHV plots to be sampled are: Dune Preserve 2 and Unnamed Veg Island.  The I-OHV plots to be sampled are: Tabletop and Pavilion hill. The NI-NOHV plots to be sampled are: Black Lake West and Phillips 66 East. These plots already contain a standardized grid, but work will need to be done to recreate the trail system and refurbish station markers.

#### Small mammals
Small mammals will be captured on camera.  Camera trapping will occur yearly (Fall) for a three-night session. ML model will process camera images and identify the species within.  Yearly trapping is sufficient to capture annual trends (Villablanca 2017), while also being the most sustainable study design.

### Analysis:

After images are processed through the ML model,we will estimate naïve occupancy for each species across the park using data from all six plots. These results will provide a baseline occupancy rate for each species in the park so future estimates can be compared to detect changes in species occurrence.  Data from 2021-2022, when both camera trapping and live trapping occurred at five plots (Hopkins _et al._ (b) i_n prep._), will be compared through a regression analysis to determine if the correlation between the two types of data is sufficient (or can be corrected using a model) such that live rapping data from the past might potentially be used to provide a deeper baseline.

| Expected Contributions and Responsibilities Objective 1  |
| --- |
|   | Data Collection | Data Analysis | Reporting |
| Cal Poly resources  |
| Principle Investigator | Support | Support | Support |
| Research Assistant | Lead | Lead | Lead |
| State Park Resources |
| Administrative personnel | Oversight | Oversight | Oversight |
| Field personnel | Lead | Lead |   |
| Field Vehicle  | Yes |   |   |

### Timeline: 
This is the anticipated timeline for this objective. Training protocol, data collection, and naïve occupancy results provided by Cal Poly.

| **Activity** | **Timeline** | **Duration - weeks** |
| --- | --- | --- |
| Finalize protocol for once yearly camera trapping | July | 1 |
| Data collection with parks staff | September | 3 |
| Data analysis with parks staff  | November-December | 1 |
| Technical Manual, Report | January-March | 3 |
| **Objective 1 cumulative** | July-March | 12 |

### Deliverables: 
Technical manual describing protocol for data collection, occupancy estimation, use of ML model, and naive occupancy rate estimation across species, and a publication quality report.

## Objective 2. Confirm or Reject Previous Study on the Effect of NI-NOHV, I-NOHV, and I-OHV on Small Mammal Occurrence

### Background:

Previous work analyzed occupancy rates for seven small mammal species across the three plot types at ODSVRA (NI-NOHV, I-NOHV, and I-OHV).  The study looked at the effect of OHV activity, fragmentation, and dominant vegetation on the occurrence of each rodent species across the SVRA.  Inference on the effect of these habitat characteristics provided valuable knowledge for the management of the ODSVRA.  The analysis found no negative effect of OHV on species occurrence, and a mixed effect of fragmentation on species occurrence (Hopkins et al. (b) _in prep_).  However, the analysis was done using live trapping data.  Additional work has demonstrated the biased effect of using live trap data for occupancy analysis, with occurrence being underestimated (Hopkins et al. (a) _in prep_).  Specifically, occupancy estimates through live trapping data can be significantly lower than the occupancy rate we know to be true by camera trapping.  Therefore, using the understanding that cameras provide far greater detection, precise occupancy estimates, and lower effort, we recommend repeating this important analysis using camera traps.

The previous analysis used data across 15 plots and seven years.  There was substantial variability in the study design, with some plots being trapped much more often than others, and a nonuniform distribution of plot types (i.e.: three I-NOHV plots, eleven I-OHV plots, and four NI-NOHV plots).  Our goal is to improve the study design in support of an analysis of species level occupancy rates across plot types.  Given the greater detection of these species through cameras compared to live traps, it will not be necessary to replicate the number of plots and years.  Instead, fewer plots should be sampled so that all plot types can be equally represented. Also, cameras will provide greater detection probability (better data), and data will be collected across all plots for four seasons (one year).  Understanding the effect of OHV activity and fragmentation on small mammal occurrence is of major significance to SVRA habitat management. Confirmation or rejection of previous analytical results will provide valuable information for habitat management at ODSVRA.

#### Specific camera monitoring proposal

1. Conduct quarterly camera trapping across nine plots to determine the effect of OHV activity and fragmentation on occurrence of seven species of small mammals. Three plots from each plot type (I-OHV, I-NOHV, NI-NOHV) will be used for a balanced design.
2. Analyze occupancy rates across each plot type for each small mammal species.
3. Determine if occurrence significantly varies for each species based on OHV activity and/or fragmentation.
4. Compare analysis results to previous results (Hopkins et al. (b) _in prep_) obtained from live trapped data.

### Methods:

#### Islands and Plots
 All plots have a grid of sixteen stations, in a 4 x 4 array, with stations at 20-meter intervals. The most common plant alliances in the ODSVRA are Willow/Wax Myrtle, and Lupine/Mock Heather (Villablanca 2017). Therefore, in order to be representative, all plots are placed so they sample 50% of each alliance. Cameras will be placed at every other station on the grid, for a total of 8 camera stations per plot.  Half of the stations (4) will be placed in the Willow/Wax Myrtle alliance and half (4) will be placed in the Lupine/Mock Heather alliance.

#### Plot selection
 We propose to sample the following nine plots. The I-NOHV plots to be sampled are: Dune Preserve 1, Dune Preserve 2, and Unnamed Veg Island.  The I-OHV plots to be sampled are: Heather, Tabletop, and Pavilion Hill. The NI-NOHV plots to be sampled are: Black Lake West, Phillips 66 East, and Maidenform. These plots already contain a standardized grid, but work will need to be done to recreate the trail and refurbish the station markers.  Plots will be evaluated and in the event it is not feasible to trap a plot, a different one will be selected before any data collection begins.

#### Small mammals
Small mammals will be captured on camera.  Camera trapping will involve a three-night session that will occur quarterly (Spring, Summer, Fall, Winter) in order to encompass seasonal changes in occupancy rates and obtain sufficient data in one year.  ML model will process camera images and identify the species within.

### Analysis:

We will use software (R) to estimate occupancy for each species across the three plot types to determine the effect of dominant vegetation type and OHV activity and fragmentation.  These methods follow Hopkins et al. (b) (_in prep_).  OHV and fragmentation will be regarded as having an important influence on species occurrence if occupancy estimates significantly vary between plot types (no confidence interval overlap).

| Expected Contributions and Responsibilities Objective 2 |
| --- |
|   | SummerData | Fall Data | Winter Data | Spring Data | Data Analysis | Reporting |
| Cal Poly resources  |
| Principle Investigator | Support | Support | Support | Support | Support | Support |
| Research Assistant | Lead | Lead | Lead | Lead | Lead | Lead |
| State Park Resources |
| Administrative personnel | Oversight | Oversight | Oversight | Oversight | Oversight | Oversight |
| Field personnel | Support | Support | Support | Support |   |   |
| Field Vehicle  | Yes | Yes | Yes | Yes |   |   |

### Timeline:
This is the anticipated timeline for this objective. Data collection and occupancy results provided by Cal Poly.

| **Activity ** | **Timeline** | **Duration - weeks** |
| --- | --- | --- |
| Finalize protocol for camera trapping | July | 1 |
| Prepare trails for deployment | July | 2 |
| Camera deployment | July, September, December, April | 12 |
| Data analysis  | April-May | 2 |
| Report | May-June | 3 |
| **Objective 2** | July-June | 30 |

### Deliverables:
A publication quality report on the effect of OHV and fragmentation on species occurrence.

## Objective 3. Assessment of Habitat Restoration Effects on Small Mammals Occupancy Monitored Via Camera Traps**.

### Background:

As restoration practices are implemented in areas of the park, monitoring has been done to investigate how the stabilization and succession of vegetation has impacted native wildlife.  Specifically, small mammal occurrence has been monitored through live trapping at five restoration plots following their removal from open riding area (OHV activity) and planting in either 2018 or 2020.  The analysis of the live trapping data showed a continued increase in occurrence for two rodent species as time since revegetation increased (Hopkins and Villablanca, _in prep_).  However, given the substantial effort live trapping takes, we propose switching monitoring of revegetated plots to camera trapping.  This lower effort would allow monitoring to continue on revegetated plots to see long term changes in species occurrence as time since revegetation proceeds.

Although small mammals have been monitored across five revegetated plots, it is difficult to draw concrete conclusions on the effect of time since revegetation as plots have received different treatments.  Specifically, the three foredune plots (F3, F4, F5) all received different revegetation treatments. Since there are no replicates for these plots, we cannot determine if differences in occurrence are due to treatment, time since treatment, or simply due to individual plot characteristics. Two other revegetated plots that have been monitored (Sand Sheet East and Sand Sheet West) both received the same revegetation treatment (but different from the foredune plots). These two plots are located farther inland and lack a key problem the foredune plots have: they cannot be trapped in summer due to the presence of nesting Western Snowy Plover (_Charadrius alexandrinus nivosus_, a federally listed species). Therefore, we propose monitoring small mammals at the two sand sheet plots to identify overall changes in species occurrence as time since revegetation increases.  Previous data collected quarterly from summer 2018 to winter 2020 will be combined with data collected quarterly from spring 2021 to fall 2022. These data will be combined with our proposed quarterly data collection from summer 2023 through spring 2024, giving the analysis five years of data.

In order to combine the past live trapping data (2018-2020 and 2021-2022) with the proposed camera trapping data (2023-2024), an analysis will need to be done to take into account the varying detection probability across the two methods of data collection.  Meaning, to simply switch to cameras and compare the naive occupancy estimates achieved through camera data to the past occupancy estimates achieved through live trapped data would be incorrect.  As previous work has shown (Hopkins et al. (a) _in prep_)_,_ occupancy estimates from live trapped data are downwardly biased and not comparable with those achieved through camera data.  However, we can use the past live trapped data with the new camera trapped data by performing a corrected occupancy analysis (MacKenzie et al. 2002).  This analysis will allow us to estimate occupancy across all years of data collection on restoration plots while accounting for the difference in detection probabilities from live traps and camera traps in the analytical model (MacKenzie et al. 2002).  By doing this, the occupancy estimates achieved through cameras will be known and available for future trend analysis once years since revegetation becomes even longer.  For continued monitoring of revegetated plots following the end of this grant, parks can continue data collection through the low effort method of cameras, images processed with ML model, and estimates of naïve occupancy.

#### Specific restoration camera monitoring proposal

1.     Conduct quarterly camera trapping across two plots that received vegetation restoration to determine the effect of restoration on small mammal occurrence.

2.     Analyze occupancy rates of species present on plot to look at occurrence over years since revegetation.  Analysis will incorporate both past live trapping data and camera trapping data by building data type into the analytical model (MacKenzie et al. 2002).

3.     Establish occupancy estimates for each year following revegetation using all available data.  Future monitoring using naïve occupancy will then be able to compare occupancy across previous years to analyze trends.

4. Compare time series with data collected to date.

### Methods:

_Islands and Plots._ The two sand sheet plots have a grid of sixteen stations, in a 4 x 4 array, with stations at 20-meter intervals. Cameras will be placed at every other station on the grid, for a total of 8 camera stations per plot.

_Small mammals._ Small mammals will be captured on camera.  Camera trapping will involve a three-night session that will occur quarterly (summer, fall, winter, spring). ML model will process camera images and identify the species within.

### Analysis:

We will use software (R) to estimate occupancy for all species on the sand sheet plots across the five years revegetation time series using data collection method as a covariate in the analysis.  Future monitoring will be possible through the lower effort analysis of naïve occupancy since the a five-year trendline will have been established.

| Expected Contributions and Responsibilities Objective 3 |
| --- |
|   | SummerData | Fall Data | Winter Data | Spring Data | Data Analysis | Reporting |
| Cal Poly resources  |
| Principle Investigator | Support | Support | Support | Support | Support | Support |
| Research Assistant | Lead | Lead | Lead | Lead | Lead | Lead |
| State Park Resources |
| Administrative personnel | Oversight | Oversight | Oversight | Oversight | Oversight | Oversight |
| Field personnel | Support | Support | Support | Support |   |   |
| Field Vehicle  | Yes | Yes | Yes | Yes |   |   |

### Timeline:
 This is the anticipated timeline for this objective. Data collection and occupancy results provided by Cal Poly.

| **Activity ** | **Timeline** | **Duration - weeks** |
| --- | --- | --- |
| Camera deployments | July, September, December, March | 5 |
| Data analysis  | April | 1 |
| Report | April-May | 2 |
| **Objective 3** | July-May | 8 |

### Deliverables:
A publication quality report on species occurrence changes across five years since revegetation providing trends for comparison with future data collected independently by Park personnel.

## Objective 4. Package the entire analytical method into an app

### Background

Currently, the analytical package is run through a General User Interface (GUI). The GUI is the first step to making the software work for someone who does not have coding experience and does not write software. In other words, it lets a user run the program.  The GUI is like a set of dialog boxes where the user moves from commanding one task, to commanding the next, and so on through completion. This works, but has the potential to crash. The standard procedure would be to create an app that runs the entire program. The user would define some parameters and then the program would run on its own and make the appropriate decisions given the parameters input by the user.  If the program gets the information upfront, then it can make all of the appropriate decisions and will not crash.

The objective of this task would be to develop the app. This would be done by the programmer who created the GUI version from a combination of their code (in Python) and Jaran Hopkin's code (in R). The GUI is written and compiled in Python. Thus, a portion of the work towards the app has been completed (to the stage of the GUI), but the entire app has not been completed. This objective would result in a fully developed and executable app.

| Expected Contributions and Responsibilities Objective 4 |
| --- |
|   | Complete code  | Test app and interface | Trial with users and install |
| Cal Poly resources |
| Principle Investigator | Support | Support | Support |
| Programmer | Lead | Lead | Lead |
| State Parks Resources  |
| Administrative personnel | Oversight | Oversight | Oversight |

### Timeline: 
This is the anticipated timeline for this objective. Conversion of code from GUI to app provided by Cal Poly.

| **Activity ** | **Timeline** | **Duration Weeks** |
| --- | --- | --- |
| Complete writing code for app | Summer | 4 |
| Test app and interface | Summer | 1.5 |
| Trial with users and install | Summer | 1 |
| **Objective 6** | July-Aug | 6.5 |

### Deliverables: 
An occupancy modeling app installed on Park Staff computers that runs analyses on wildlife camera images using artificial intelligence for species identification.

## Budget Justification

​​The Oceano Dunes State Vehicular Recreation Area (ODSVRA) employs a Wildlife Habitat Protection Program (WHPP) aimed at "detecting changes in species and/or communities overtime." Cal Poly San Luis Obispo and ODSVRA have been collaborating to study small mammal population dynamics as part of the park's WHPP program. Previous work at ODSVRA has studied small mammal populations that occur throughout the park, analyzing their population dynamics (Villablanca 2017), occurrence (Hopkins _et al._ (b) _in prep._), and monitoring methodologies applicable (Hopkins _et al._ (a) _in prep._). While some questions have been answered thus far, an additional year of monitoring work and research is needed to fulfill the goals and objectives of the WHPP. The proposed work will help the Senior Environmental Scientist fulfill the goals and objectives of the WHPP. This will require a year's worth of effort (50 weeks at 19.5 hrs per week) from a Cal Poly research assistant experienced with the ecosystem system, the data collection and analytical approaches, the management relevant research questions, and the production of publication quality reports. A research assistant with this experience is available and, importantly, will not require any additional training. This will also require the assistance of a computer programmer who will contribute 6.5 weeks at 20 hrs per week.

## Literature Cited

Hopkins, J.; Santos-Elizondo, G. M.; Villablanca, F. 2023 (_manuscript (a) in prep_). Detecting and Monitoring Rodents Using Camera Traps and Machine Learning versus Live Traps for Occupancy Modeling. California Polytechnic State University, San Luis Obispo, California.

Hopkins, J.; Trunzo, J.; Little, S.; Pawlak, C.; Villablanca, F. 2023 (_manuscript (b) in prep_). Vegetation and Habitat Fragmentation Predict Occupancy by Small Mammal Species in Coastal Dunes with off Highway Vehicular Recreation; California Polytechnic State University: San Luis Obispo, CA.

Hopkins, J. & Villablanca, F. 2023 (_Report in prep_.). Analysis of Species Occurrence Across Revegetated Plots at the ODSVRA. California Polytechnic State University, San Luis Obispo, California.

Lodge, D. M., Williams, S., MacIsaac, H. J., Hayes, K. R., Leung, B., Reichard, S., ... &

McMichael, A. 2006. Biological invasions: recommendations for US policy and management. Ecological Applications, 16(6), 2035-2054.

MacKenzie, D.I.; Nichols, J.D.; Lachman, G.B.; Droege, S.; Andrew Royle, J.; Langtimm, C.A. 2002. Estimating Site Occupancy Rates When Detection Probabilities Are Less Than One. Ecology, 83, 2248–2255.

McCarthy, M. A., Moore, J. L., Morris, W. K., Parris, K. M., Garrard, G. E., Vesk, P. A., ... & Yue, B. 2013. The influence of abundance on detectability. Oikos, 122(5), 717-726.

Rinella, M. J., Maxwell, B. D., Fay, P. K., Weaver, T., & Sheley, R. L. 2009. Control effort

exacerbates invasive‐species problem. Ecological Applications, 19(1), 155-162.

Royle, J. A., & Nichols, J. D. 2003. Estimating abundance from repeated

presence–absence data or point counts. Ecology, 84(3), 777–790.

Shiels, A. B., Pitt, W. C., Sugihara, R. T., & Witmer, G. W. 2014. Biology and impacts of

Pacific island invasive species. 11. _Rattus rattus_, the black rat (Rodentia: Muridae). Pacific Science, 68(2), 145-184.

Villablanca, F. 2017. HMS at the ODSVRA: A Small Mammal Perspective. California State Parks. 15Pg

Villablanca, F. 2023 (_report draft submitted_). Updated _Rattus rattus_ surveys to determine whether they still occur in Dune Preserve. California Polytechnic State University, San Luis Obispo, California.