#!/bin/bash
#python ./testCaseExecutables/"$LINE" > temp/testCase"$i"results.txt

#Clear the temp files
echo "Clearing Temp Folder"
rm -r temp/*
rm -r reports/*

#Preps final ouput file with /scripts/html-template.txt
echo "Running Tests"
echo " "
while read LINE; do
	echo "$LINE" >> reports/testReport.html
done < "scripts/html-template.txt" 

#reads each line of test case txt files and saves them into html
for filename in testCases/*.txt; do
	i="${filename//[^0-9]/}"
	echo "Running Test $i"
	ARRAY=()
	while read LINE; do
		ARRAY+=("$LINE")
	done < "$filename"
	cd project/Jython/
	#runs jython and applicable test case
	OUTPUT=$(sh ./jython.sh -i  library/"${ARRAY[0]}" "${ARRAY[4]}" 2>&1)
	cd ../../
	#save output to temp txt files
	echo "$OUTPUT" >> temp/Test"$i"temp.txt
	
	#find actual output from temp files
	KEEPLINE="FALSE"
	while read LINE; do
		if [ "$KEEPLINE" == "True" ]; then
		   OUTPUT="$LINE"
		   KEEPLINE="False"	
		fi

		if [ "$LINE" == "--Result--" ]; then
		    KEEPLINE="True"
		fi
	done < temp/Test"$i"temp.txt
	#add info to final report for each test
	echo "<tr>
	<td>${ARRAY[0]}</td>
	<td>${ARRAY[1]}</td>
	<td>${ARRAY[2]}</td>
	<td>${ARRAY[3]}</td>
	<td>${ARRAY[4]}</td>
	<td>${ARRAY[5]}</td>
	<td>$OUTPUT</td>" >> temp/testcase"$i"result.html
	#Compare expected and actual output and store result in final report
        if [ "${ARRAY[5]}" == "$OUTPUT"  ]; then
		echo "<td>Pass</td></tr>" >> temp/testcase"$i"result.html
	else
		echo "<td>Fail</td></tr>" >> temp/testcase"$i"result.html
	fi
done

for filename in temp/*.html; do
	while read LINE; do
		echo "$LINE" >> reports/testReport.html
	done < "$filename"
done

echo "</table>" >> reports/testReport.html
echo "</body>" >> reports/testReport.html
echo "</html>" >> reports/testReport.html
#open html file
xdg-open reports/testReport.html
echo "done"
