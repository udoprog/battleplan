#!/bin/bash
sudo mysqldump eve mapSolarSystems mapRegions mapConstellations | gzip -f - > dump.sql.gz
