# Module 7 Discussion: Confidence Intervals and Hypothesis Tests

## Discussion prompt

In Modules 6 and 7, we reviewed concepts related to confidence intervals and hypothesis tests. For this assignment, reflect on these statistical concepts and how they are used in different fields and applications.

Your initial post must address the following:

1. Provide at least two real-world applications of confidence intervals. At least one application must be from an aeronautical field. For each application:
   - Explain the parameter being studied.
   - Explain why a confidence interval is being used.
   - Evaluate whether the cited confidence level, such as 90%, 95%, or 99%, is appropriate. If not, recommend a different confidence level and explain why.
   - Include a link to a reference where classmates can view the details of the application.

2. Provide at least two real-world applications of hypothesis testing. At least one application must be from an aeronautical field. For each application:
   - Explain the claim or hypothesis being studied.
   - Explain why a hypothesis test is being used.
   - Evaluate whether the cited significance level, such as $\alpha=0.05$ or $\alpha=0.10$, is appropriate. If not, recommend a different significance level and explain why.
   - Include a link to a reference where classmates can view the details of the application.

The initial post is due by the fourth day of the module.

## Classmate-response requirements

Reply to at least two classmates by the last day of the module. In each reply:

1. For every confidence-interval application, give a one-sentence interpretation of the interval in context. Explain it in language suitable for someone with no statistical background.
2. For every hypothesis-test application, explain in context what it would mean to reject the null hypothesis and what it would mean to fail to reject the null hypothesis. Explain it in language suitable for someone with no statistical background.

## Relevant learning objectives

### Module 6: Parameter Estimation with Confidence Intervals

Upon successful completion of Module 6, students should be able to:

1. Construct confidence intervals for the mean of a normal distribution using either the normal distribution or the $t$-distribution. (LO12)
2. Construct confidence intervals for the variance and standard deviation of a normal distribution. (LO12)
3. Construct confidence intervals for a population proportion. (LO12)
4. Use a general method to construct an approximate confidence interval for a parameter. (LO12)
5. Analyze data to form statistically sound conclusions. (LO1-13)

### Module 7: Statistical Inference for a Single Sample

Upon successful completion of Module 7, students should be able to:

1. Structure engineering decision-making problems as hypothesis tests. (LO13)
2. Test hypotheses about the mean of a normal distribution using either a $Z$-test or a $t$-test. (LO13)
3. Test hypotheses about the variance or standard deviation of a normal distribution. (LO13)
4. Test hypotheses about a population proportion. (LO13)
5. Use the $p$-value approach to make decisions in hypothesis tests. (LO13)
6. Compute power and Type II error probability and make sample-size decisions for tests of means, variances, and proportions. (LO13)
7. Explain the relationship between confidence intervals and hypothesis tests. (LO12, LO13)
8. Analyze data to form statistically sound conclusions. (LO1-13)

---

## Initial discussion post

One aviation example of a confidence interval comes from an AOPA survey of about 1,200 general-aviation pilots. It found that 91% used an electronic flight bag. The parameter is the percentage of all general-aviation pilots who use one. The survey used a 95% confidence level with a margin of error of about three percentage points. I think 95% is appropriate, although the online sample may not represent every type of pilot.

Reference: https://www.faa.gov/air_traffic/flight_info/aeronav/acf/media/Presentations/2-aopa-survey-results.pdf

Another example is a CDC estimate that 31.7% of U.S. adults had a diagnosed seasonal allergy, eczema, or food allergy. Its 95% confidence interval was 31.1% to 32.4%. The parameter is the actual percentage of U.S. adults with at least one of these conditions. A confidence interval is used because the CDC surveyed a sample instead of every adult. I think 95% is appropriate for this purpose.

Reference: https://www.cdc.gov/nchs/products/databriefs/db545.htm

For hypothesis testing, an FAA study tested whether different unmanned-aircraft lost-link procedures affected controller safety ratings, workload, and other results. The null hypothesis was that the procedures made no difference. The study used about alpha = 0.05, but I would use alpha = 0.01 for a final safety decision because approving an ineffective procedure could be dangerous.

Reference: https://hf.tc.faa.gov/publications/2019-z-25-validation-unmanned-enroute/tc19-25.pdf

The CDC also tested whether seasonal-allergy rates were different for women and men. The null hypothesis was that the rates were equal, and the claim was that they were different. The result was significant at p < 0.05. I think alpha = 0.05 is reasonable because this is a general public-health comparison rather than a direct decision about one person's medical care.

Reference: https://www.cdc.gov/nchs/products/databriefs/db545.htm

## Classmate response 1

I like that your examples show how statistics can be used to prevent real safety problems. For the bridge, the 95% confidence interval gives engineers a reasonable range for its actual load capacity. For the runway, it gives them a reasonable range for the average pavement strength without having to test every section. In the concrete test, rejecting the null hypothesis would warn engineers that the concrete may not meet the required strength. Failing to reject it would mean the results did not show enough evidence of a strength problem.

## Classmate response 2

I like that all of your examples connect statistics to practical safety decisions. For the NASA flight-route study, the 95% confidence interval gives a reasonable range for the true average fuel savings per flight. For the pavement markings, the interval suggests that the actual crash reduction could vary, but the conservative estimate is still about 15.4%. In the aircraft-display study, rejecting the null hypothesis means the experts and nonexperts had significantly different entry times, while failing to reject it would mean there was not enough evidence of a difference. For the rural-road study, rejecting the null hypothesis means the average speeds were significantly different between the two periods, while failing to reject it would mean the observed change could reasonably be due to normal variation.
