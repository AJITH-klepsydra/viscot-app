<!---
<portfolio>
<image>
https://cdn.pixabay.com/photo/2020/03/22/16/17/coronavirus-4957673__340.jpg
</image>
<description>
The Python Code for getting Track of Novel Covid Pandemic growth in all over the world
</description>
<tags>
#python#pyqt5#beautifulsoup#opencv
</tags>
</portfolio>
-->

# Covid Tracker 

Data Tracker
---
## Current Tracker


![Covid-19 Confirmed](https://covid19-badges.herokuapp.com/confirmed/latest)       ![Covid-19 Recovered](https://covid19-badges.herokuapp.com/recovered/latest)       ![Covid-19 Deaths](https://covid19-badges.herokuapp.com/deaths/latest)


___
The Python Code for getting Track of Novel Covid Pandemic growth in all over the world

__Tracks__ and __Visualize__ __data__ on patients,death,recovery in __line plots__ and __pie charts__

The project has two versions working on diffrent API's choose between them according to your need

---

## Set-Up

```bash
$ pip install -r requirements.txt
```

---
# Covid Tracker 1

## API

The **[API](https://coronavirus-tracker-api.herokuapp.com/v2/locations)** we used

The **[Repo](https://github.com/ExpDev07/coronavirus-tracker-api)** api provider

---

<ol>
<li>Runs with slower Api</li>
<li>Province wise Detail-Analysis</li>
<li>Total population of a Country is present</li>
<li>Patient Recovery Details is not available</li>
</ol>

---


## Working

<ul>
Refer country.txt & province.txt while giving inputs

If they gets tampered run [countrylist.py](CovidTracker1/countrylist.py) , [provincelist.py](CovidTracker1/provincelist.py) respectively to regenrate them.

Do the same to update the lists
</ul>

| Result | File | command|
|--------|------|--------|
|To get latest Global updates |      [latest.py](CovidTracker1/latest.py)|``` python3 latest.py ```|
|To get Graphs on Result |      [timeline.py](CovidTracker1/timeline.py)|``` python3 timeline.py ```|
|To get Updates based on Country | [country.py](CovidTracker1/country.py)|``` python3 country.py ```|
|To get Updates based on Provinces | [province.py](CovidTracker1/provinces.py)|``` python3 province.py ```|
|To get Available Country list |      [countrylist.py](CovidTracker1/countrylist.py)|``` python3 countrylist.py ```|
|To get Available Province list |      [provincelist.py](CovidTracker1/provincelist.py)|``` python3 provincelist.py ```|
|Country list |      [country.txt](CovidTracker1/country.txt)||
|Province list |      [province.txt](CovidTracker1/province.txt)||
|To Convert json to dictionary | [jsontodict.py](CovidTracker1/jsontodict.py)||


---


# Covid Tracker 2

## API

The **[API](https://api.covid19api.com/)** we used

The **[Repo](https://github.com/CSSEGISandData/COVID-19)** api provider

---

<ol>
<li>Comparitively Much Faster Api</li>
<li>No  Province wise Details</li>
<li>Recovery number is  available</li>
<li>No data on Total population of a Country</li>
</ol>

---

## Working


<ul>
Refer country.txt while giving inputs

If it gets tampered run [countrylist.py](CovidTracker2/countrylist.py) to regenrate it.

Do the same to update the list
</ul>


| Result | File | command|
|--------|------|--------|
|To get latest Global updates |      [latest.py](CovidTracker2/latest.py)|``` python3 latest.py ```|
|To get Graphs on Result |      [timeline.py](CovidTracker2/timeline.py)|``` python3 timeline.py ```|
|To get Updates based on Country | [country.py](CovidTracker2/country.py)|``` python3 country.py ```|
|To get Available Country list |      [countrylist.py](CovidTracker2/countrylist.py)|``` python3 countrylist.py ```|
|Country list |      [country.txt](CovidTracker2/country.txt)||
|To Check connection ad to store url | [url.py](CovidTracker2/jsontodict.py)||



---



## Graph Plotting

### Line plot

Line graphs are plotted using matplotlib module
According to Provinces and Country Coresponding Graphs are produced

|![No. of Confirmed Cases](https://github.com/Niranjanprof/Covid-19-Tracker/blob/master/rsc/1%20(2).png)|![No. of Death Cases](https://github.com/Niranjanprof/Covid-19-Tracker/blob/master/rsc/1%20(1).png)|![No. of Recoverd Cases](https://github.com/Niranjanprof/Covid-19-Tracker/blob/master/rsc/1%20(4).png)|
|------------------------|-------------------------|------------------------|
|No. of Confirmed Cases|No. of Death Cases|No. of Recoverd Cases|

---



---

### Pie Plot

Pie charts are plotted using matplotlib.pyplot.pie function
According to Provinces and Country and Global details Coresponding Graphs are produced


|![Global](https://github.com/Niranjanprof/Covid-19-Tracker/blob/master/rsc/1.png)|![Country Specific](https://github.com/Niranjanprof/Covid-19-Tracker/blob/master/rsc/2.png)|![Country-Province](https://github.com/Niranjanprof/Covid-19-Tracker/blob/master/rsc/3.png)|
|------------------------|-------------------------|------------------------|
|Global|Country Specific|Country-Province|

---
## Task

<ul>
  <li>'travis.yml' build status development.</li> 
  <li>Adding Active Cases</li>
  <li>Adding Ratio's</li> 
</ul>

---

## Contributors


<table>
  <tr>
    <td align="center"><a href="https://github.com/Niranjanprof"><img src="https://avatars1.githubusercontent.com/u/48713926?s=400&u=a473cb9bbbc98506ae6b55ccd2b45cfdc941d517&v=4" width="200px;" alt=""/><br /><sub><b>Niranjan B(Prof Moriarty)</b></sub></a><br /><a href="https://github.com/Niranjanprof/Corvid-19-Tracker/commits?author=Niranjanprof" title="Code">💻</a> <a href="https://github.com/Niranjanprof/Corvid-19-Tracker/commits?author=Niranjanprof" title="Documentation">📖</a> <a href="#maintenance-Niranjanprof" title="Maintenance">🚧</a></td>
    <td align="center"><a href="https://github.com/AJITH-klepsydra"><img src="https://avatars3.githubusercontent.com/u/62293152?s=400&v=4" width="200px;" alt=""/><br /><sub><b>Ajith PM(Klepsydra Alpha)</b></sub></a><br /><a href="https://github.com/Niranjanprof/Corvid-19-Tracker/commits?author=AJITH-klepsydra" title="Code">💻</a> <a href="https://github.com/Niranjanprof/Corvid-19-Tracker/commits?author=AJITH-klepsydra" title="Documentation">📖</a></td>
  <td align="center"><a href="https://github.com/amalnathm7"><img src="https://avatars2.githubusercontent.com/u/64605131?s=400&u=7263b2b702f0175dff070e379d065557f6843a85&v=4" width="200px;" alt=""/><br /><sub><b>Amal Nath(Dr.Strange)</b></sub></a><br /><a href="https://github.com/Niranjanprof/Corvid-19-Tracker/commits?author=amalnathm7" title="Documentation">📖</a></td>
  </tr>

</table>

---

## License & copyright

© Niranjan B 
,Ajith PM

Licensed under the [GNU GPL](LICENSE)

---

Mention This [Repo](https://github.com/Niranjanprof/Covid-19-Tracker) while you use this in your projects :)

