#

Prerequisites:

* A List type variable called 'UATGateList' must be defined in the release template - or globally, if you desire.
* The ${UATGateList} can be populated through a User Input task, or on the launch page
* The UAT phase must be exactly named "UAT"
* The gate task in the UAT phase must be exactly named "Execute UAT Gates"
* 'Run scripts as user' must be set in the release's Properties
