#!/bin/bash
#python ./testCaseExecutables/"$LINE" > temp/testCase"$i"results.txt
echo "Clearing Temp Folder"
rm -r temp/*
rm -r reports/*

echo "Running Tests"
echo " "
while read LINE; do
	echo "$LINE" >> reports/testReport.html
done < "scripts/html-template.txt" 

for filename in testCases/*.txt; do
	i="${filename//[^0-9]/}"
	echo "Running Test $i"
	ARRAY=()
	while read LINE; do
		ARRAY+=("$LINE")
	done < "$filename"
	OUTPUT=$(python ./testCaseExecutables/"${ARRAY[0]}")
	
	echo "<tr>
	<td>${ARRAY[0]}</td>
	<td>${ARRAY[1]}</td>
	<td>${ARRAY[2]}</td>
	<td>${ARRAY[3]}</td>
	<td>${ARRAY[4]}</td>
	<td>${ARRAY[5]}</td>
	<td>$OUTPUT</td>" >> temp/testcase"$i"result.html

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


echo "done"
