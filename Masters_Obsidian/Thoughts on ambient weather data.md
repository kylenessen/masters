I've been worried about how will I track weather data OUTSIDE the grove for the wind study at Pismo. 

An initial thought was to use the Oceano Airport as a baseline, but unfortunately, it hasn't worked since April. 

I had the idea to check out weather underground again, and I'm glad I did. There are several stations that are making wind measurements very close to the grove, giving me some redundancy. 

There's also a very simple API to get both current conditions AND historical conditions. 

The historical comes in increments of 5 minutes, but can be retrieved for past dates. I may have to rely on this 

Documentation for current conditions
https://docs.google.com/document/d/1KGb8bTVYRsNgljnNH67AMhckY8AQT2FVwZ9urj8SWBs/edit#heading=h.9qco2mv7yhvd

documentation for historical observations
https://docs.google.com/document/d/1w8jbqfAk0tfZS5P7hYnar1JiitM0gQZB-clxDfG3aD0/edit#heading=h.fqwxgomkqqxb

Here's a working link to get current conditions
https://api.weather.com/v2/pws/observations/current?apiKey=e1f10a1e78da46f5b10a1e78da96f525&stationId=KCAGROVE114&numericPrecision=decimal&format=json&units=e

The thought here is run that api every 15 seconds or so and check if there is a new observation. If so, record it to a sql database. 

Probably can't do this today, but good for the future