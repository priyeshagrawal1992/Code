#!/usr/bin/env bash
################################################################################
#   Name: setenv.sh                                                            #
#                                                                              #
#   Description: This shell script is used to set path and library in          #
#                 different environment and to run python or spark script      #
#                                                                              #
#   Parameters:                                                                #
#                                                                              #
#   Authors: Priyesh Agrawal                                                   #
#                                                                              #
#   Change Log:                                                                #
#                                                                              #
#       Date                Changed By              Description                #
#   13-Sep-2018          Priyesh Agrawal        Initial creation               #
################################################################################

hostname

if [[ hostname | grep -c "UAT"=1 ]]
