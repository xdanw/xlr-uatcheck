
thisRelease = getCurrentRelease();

# currrent release: str
thisReleaseId = thisRelease.id;

# variable list: List<Var>
varList = releaseApi.getVariables(thisReleaseId);

# get UATGateList dict
for var in varList:
    # print x;
    # print "[key: " + x.key + "]";
    if var.key == "UATGateList":
        uatVar = var;

print "UATGateList: ";

for z in uatVar.value:
    print "[" + z + "]";

# Find task

taskList = taskApi.searchTasksByTitle("Execute UAT Gates", "UAT", thisReleaseId);

# Grab the LAST one
uatTask = taskList.pop();

uatTaskId = uatTask.id;

print "uatTaskId: " + uatTaskId;

for uatItem in uatVar.value:
    cond = Condition();
    cond.setTitle(uatItem);
    cond.setChecked(0);
    taskApi.addCondition(uatTaskId, cond);
