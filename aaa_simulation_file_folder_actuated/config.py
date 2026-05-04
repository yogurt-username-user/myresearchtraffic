import os
import sys


simulationTime = 22000#time at the end of the simulation 39600
startTime = 21600 #time at which the simulation starts
stepTime = 0.25 #length of the step 0.25
tram_to_tls_det_distance = 1.5 #distance away from tls, where trams get detected
sumoBinary = "sumo" 
xml2csv_path = "/usr/share/sumo/tools/xml/xml2csv.py"