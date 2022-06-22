#!/bin/bash

set -e

# Start a new problem for python practive of Leetcode
# 1. Create the problem folder in ./PythonPractice
#   <Index><ProblemName>
# 2. Ceate the problem file
# 3. Create the case yaml file
# 4. Add content in ./vscode/launch.json

# ex:
# ./start_python_problem.sh 34 Find First and Last Position in Sorted Array
# ./start_python_problem.sh 278 First Bad Version
# ./start_python_problem.sh 268 Missing Number
# ./start_python_problem.sh 204 Count Primes
# ./start_python_problem.sh 136 Single Number
# ./start_python_problem.sh 657 Robot Return to Origin
# ./start_python_problem.sh 67 Add Binary

# ./start_python_problem.sh 1 Two Sum

PythonPracticeDir=${PythonPracticeDir-.}
templateName="LeetCodeTemplate"
# Create the problem folder

firstUpperName=""
lowerName=""

for ((i = 1; i <= $#; i++)); do
    # echo "i: ${i}"
    # echo "${!i}"
    if [[ "$i" -eq 1 ]]; then
        index="${!i}"
    else
        str="${!i}"
        # echo ${str}
        upperFirst=$(echo "${str:0:1}" | awk '{print toupper($0)}')
        # lowerFirst=$(echo ${upperFirst} | awk '{print tolower($0)}')
        remain="${str:1}"
        firstUpperName+="${upperFirst}${remain}"
        # lowerName+="${lowerFirst}${remain}"
    fi
done

echo "index: ${index}"
echo "firstUpperName: ${firstUpperName}"

problemDir=${index}${firstUpperName}

cd $PythonPracticeDir
mkdir $problemDir
cd $problemDir

cp ../${templateName}/${templateName}.py "${firstUpperName}.py"
cp ../${templateName}/${templateName}Case.yml "${firstUpperName}Case.yml"
echo
echo "Copy the following into .launch for debugging"

cat << EOF
        ,
        {
            "name": "${firstUpperName}",
            "type": "python",
            "program": "\${workspaceFolder}/${problemDir}/${firstUpperName}.py",
            "request": "launch",
            "console": "integratedTerminal",
            "env": {
                "SERVICE_LOG_LEVEL": "DEBUG",
            },
            "args" : ["--case", "${problemDir}/${firstUpperName}Case.yml"]
        }
EOF

echo "Create finished!!"