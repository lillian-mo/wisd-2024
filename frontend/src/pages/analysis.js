
const launchAngleList = [
    {description: 'Low launch angle: &lt; 8 degrees', key: 1},
    {description: 'Ideal launch angle: 8-32 degrees', key: 2},
    {description: 'High launch angle: &gt; 32 degrees?', key: 3}
    ];

export const AnalysisPage = () => {
    return(
        <>
        <h1>Analysis</h1>
        <p>
        MLB considers the ideal launch angle as the “sweet spot launch angle”, which is between 8-32 degrees. 
https://www.mlb.com/glossary/statcast/launch-angle</p>
        <ol>
                {launchAngleList.map(angle => {
                return (
                    <li key={angle.key}>{angle.description}</li>
                );
                })}
        </ol>
        <p>
Our data was grouped into 3 ranges:
1.	Low launch angle: &lt; 8 degrees
2.	Ideal launch angle: 8-32 degrees
3.	High launch angle: &gt; 32 degrees

There are 3 results of a pitch, being a strike, a hitintoplay, or a ball. Strikes are not desirable to the batter because 3 strikes lead to a strikeout, but  hitintoplays and  balls are desirable to the batter since four balls allow the batter to walk to first base. 

Method: 
1.	Import JSON files into Excel power query.
2.	Parse through JSON, creating columns for pitch results and angle. 
•	Since at bats that did not have hits were empty in “Events,” filtered out the rows that were null, then expanded “Events” to angles. 
3.	Since launch angle is in the second index of the angles list, create a new column indicating the row indices.
4.	Filter out the rows with odd indices, leaving only the launch angle behind in the angles column. 
5.	Determine % of strikes, % of hitintoplays, and % of balls for each launch angle range. 

The results from the data are: 

        </p>
        </>
    );
}