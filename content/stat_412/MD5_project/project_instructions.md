# STAT 412 — Module 5 Midterm Project Instructions

Source files in this folder:

- `STAT 412 Printable Midterm Project Instructions.docx`
- `about.html`
- `Dataset_STAT412_Project_Final.xlsx`
- `Dataset_STAT412_Project_Final(ArrivalData).csv`
- `Dataset_STAT412_Project_Final(Data Dictionary).csv`

The original Word and Excel files should remain untouched. Use the CSV exports
and the helper/script outputs for planning, checking, and scratch work.

Note: the Word extraction contained one garbled phrase in Section 8 referring to
"age of aircraft." The Canvas `about.html` text says Section 8 is about
**on-time arrival data**, which is consistent with the rest of the project.

## Activity overview

On-time arrival data is important for airlines because it affects profitability
and customer satisfaction. In this project, analyze on-time arrival data and use
statistical methods to make conclusions that could help an airline make informed
decisions.

You will use Excel for statistical calculations and graphical displays.

Both files must be submitted:

1. Completed Word document template.
2. Excel workbook showing calculations and graphs.

For the final project in Module 9, this same dataset will be analyzed further
with more advanced statistical methods.

## Data

The dataset comes from the Bureau of Transportation Statistics / U.S. Department
of Transportation.

For this project, focus on column M:

- `ARR_DELAY`: difference in minutes between scheduled and actual arrival time.
- Negative values mean the flight arrived early.
- Positive values mean the flight arrived late.

The dataset also includes a `Data Dictionary` sheet explaining the column names.

## Section 1 — Select a sample

Randomly select 250 rows of data for the analysis.

The instructions allow any random selection method, including a random number
table, random.org, or Excel. One Excel method:

1. In cell `R2`, enter `=RAND()`.
2. Drag/fill that command down through all rows in the table.
3. Because `RAND()` recalculates whenever Excel changes, copy column R and use
   Paste Values into column S to freeze the random numbers.
4. Sort the dataset by column S in ascending order.
5. Keep the first 250 rows and remove the remaining rows from the working copy.

Important: do this in a working copy of the Excel file, not the original source
file.

## Section 2 — Descriptive statistics

Analyze `ARR_DELAY` for the 250-row sample. Round answers to one decimal place
and include units where appropriate.

Provide:

a. Mean  
b. Median  
c. Standard deviation  
d. Variance  
e. Minimum  
f. Maximum  
g. 1st quartile  
h. 3rd quartile  
i. Sort by `UNIQUE_CARRIER`, select any two airlines, compare mean and standard
deviation for Airline #1 vs. Airline #2, and state a conclusion.  
j. Compare the median on-time arrival results for Airline #1 vs. Airline #2 and
state a conclusion.

## Section 3 — Trimmed mean

Calculate and interpret a 20% trimmed mean for `ARR_DELAY`.

a. Calculate the 20% trimmed mean.  
b. Decide whether it is significantly different from the untrimmed mean from
Section 2(a).  
c. Explain why the result is or is not significantly different.  
d. Explain why someone might use a trimmed mean instead of an untrimmed mean.

## Section 4 — Side-by-side boxplots

Sort by `UNIQUE_CARRIER` and select any two airlines at random for comparison.

a. Use Excel to create a side-by-side boxplot for arrival delays of Airline #1
vs. Airline #2. Copy/paste the graph into the Word template.  
b. For each airline, comment on distribution shape: symmetric, skewed left, or
skewed right.  
c. Identify whether outliers appear. If outliers appear, explain what they
indicate about arrival delays and whether the airline should be concerned.  
d. Compare the two boxplots and identify important differences in the
distributions.  
e. Assume you are a manager at Airline #1 and state a conclusion based on the
boxplot comparison.

## Section 5 — Pareto chart

For the 250-row sample, calculate the average arrival delay for each airline.
Create a Pareto-style chart where:

- Horizontal axis = airline name/code.
- Vertical axis = average arrival delay.
- Airlines are ordered from worst to best average delay.

Answer:

a. Copy/paste the Pareto chart into the Word template.  
b. Identify the worst-performing airline by average arrival delay.  
c. Identify the best-performing airline by average arrival delay.  
d. Explain the benefit of a Pareto chart compared with a regular bar chart.  
e. As manager of the worst-performing airline, discuss what you would
investigate to improve on-time arrival. Separate factors within the airline's
control from factors outside the airline's control.

## Section 6 — Applying the normal distribution

Assume `ARR_DELAY` follows a normal distribution. Use the sample mean from
Section 2(a) and the sample standard deviation from Section 2(c). Round answers
to three decimal places.

Excel's `NORM.DIST` command calculates areas under the normal curve.

a. Calculate the probability that a flight arrives early.  
b. Calculate the probability that a flight arrives late.  
c. Calculate the probability that arrival delay falls between the 1st quartile
and 3rd quartile from Section 2(g) and 2(h).  
d. Decide whether the result from part (c) is reasonable. State the expected
area under a normal curve between the 1st and 3rd quartiles and compare your
numeric result.  
e. Calculate the probability that arrival delay falls between two standard
deviations below the mean and two standard deviations above the mean.  
f. Decide whether the result from part (e) is reasonable. State the expected
normal area within two standard deviations of the mean and compare your numeric
result.

## Section 7 — Inverse normal distribution

Assume `ARR_DELAY` follows a normal distribution. Use the sample mean and sample
standard deviation from Section 2. Round answers to one decimal place.

Excel's inverse normal command calculates arrival-delay cutoffs from cumulative
area.

a. Find the arrival delay that cuts off the top 10% of the distribution.  
b. Find the arrival delay that cuts off the bottom 15% of the distribution.

## Section 8 — Chebyshev's theorem

Use the sample mean and sample standard deviation from Section 2.

a. Assume the on-time arrival data is skewed left. Use Chebyshev's theorem to
find the probability that arrival delay falls within three standard deviations
of the mean. Show the calculation.  
b. Using the normal distribution, find the probability that arrival delay falls
within three standard deviations of the mean. Show the calculation and include
Excel commands used.  
c. Compare the Chebyshev and normal results. State what this shows about
Chebyshev's theorem.
