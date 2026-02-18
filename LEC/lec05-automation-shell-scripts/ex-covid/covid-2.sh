#!/usr/bin/env bash
# Script to process covid data from the JHU CSSE repo using shell and python

# Download several files of covid data from the repo:
# https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data
# We will get the 10th of each month of 2021
# This is the raw url stem:
# https://raw.githubusercontent.com/CSSEGISandData/COVID-19/refs/heads/master/csse_covid_19_data/csse_covid_19_daily_reports_us
# Store them in a data/ subdirectory
cd data
# curl -sO https://raw.githubusercontent.com/CSSEGISandData/COVID-19/refs/heads/master/csse_covid_19_data/csse_covid_19_daily_reports_us/[01-12]-10-2021.csv

state="Connecticut"   # state to filter for, e.g. "Connecticut"

# Grab the first line of one of the files to get the header, and write it to the output file we will use
head -1 01-10-2021.csv > state.csv

# Filter them down to desired state
for file in *-2021.csv
do
    # echo $file
	grep "$state" "$file" >> state.csv
done

csvcut -c Date,Province_State,Confirmed,Deaths,Recovered state.csv > state-trim.csv

cd ..
