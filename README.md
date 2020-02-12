# Jamf Pro Backup

I currently work in an IT shop where many employees of different departments have access to our jamfcloud environment. Jamf tracks modifications to Policies or Configuration Profiles in Settings > System Settings > Change Management Logs. These logs indicate what user made the modification with a timestamp. It does not track specifically what was changed. The purpose of this repo is to create pseudo version control of important features in Jamf Pro.


## Pre-Reqs

 - GitLab, Runners with python 3 installed.
 - Service account that has READ access to Jamf API.

## Configuration

Set Environment Variables


## Use

Set schedule in GitLab
