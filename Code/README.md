# Information about the data

Data folder contains the results for all group. These results are then further used to generate the final analysis.

 - file `Correlation_Score_Cards_Task` shows the results for each participant all groups (Himba Adults 2021, Himba Adults 2022, Italian Adults, Italian Preschoolers) for the task where participants have to order dotted rounded cards (with between 1 and 10 dots) the way they want.
 - Also, please note that this file is already preprocessed: correlations in the "cor" columns were obtained by computing **Kendall’s Tau**, yielding a score between -1 and 1. The code used to generated this is available in the `Code` folder and is called `Generate_chanceDistribution.R`. It creates a Rdata file available in this folder name `Permutation_Distr.Rdata`.
 - file `Ordering_Cards_Task` shows the number (column total_count) and percentage (column Percent) of participants to order cards according to a range of different shapes for all groups
 - file `Numerosity_Comparison_Task` shows the mean score for each participants for each condition (Increasing-Congruent, Increasing-Incongruent, Decreasing-Congruent, Decreasing-Incongruent). Mean scores include mean time, mean error, and mean inverse efficiency ("invefi")

Raw data (including result file for each participant) are not presented in this folder to make it simpler to read and access, but feel free to ask elena.eccher-1@unitn.it for more information it (also, pictures of the disposition of cards are available for the experiment with Himbas).

Note that we would be happy to share to code used for generating the experiment if you are interested in replicating or pushing forward the results.

# Information about the code                                                                                                                                                                                                                                                                                                                      
Analysis were obtained using R (write here R version - it is written at first when you open R in your console). Results were printed in an html file (`Analysis_Code.hmtl`).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
