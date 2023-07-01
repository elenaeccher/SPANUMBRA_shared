# Information about all analysis

Please be aware that the results mentioned in this paper represent only a part of the experiments conducted. It took considerable time to create experiments suitable for various populations and to capture implicit measures. For comprehensive information on the experiments conducted and the results for each group, please refer to the folder named All_Analyses. Here is a brief overview of the experiments performed with each group:

| Population | *OrderingCards* | CountingStones | GazeTracking | *Numerosity (VT)* | Squares | Valence | Luminance | Baskets | Numberline |
| --- | --- | --- | --- |--- | --- | --- | --- | --- | --- |
| Himbas 2021 | v | v | v | v |  |  |  | v | v |
| Himbas 2022 | v |  | v | v | v | v | v |  |  |
| Italian Preschoolers | v |  | v | v |   | v |  | v |  |
| Italian Adults |  v |  |  | v |   | v | v | v |  |

The following are the reasons why some experiments are not included in the final analysis:

 - Some experiments had unreliable results due to various factors. For instance, gaze tracking with Himba participants outdoors, under bright lighting conditions, did not provide sufficiently high-quality data to determine the direction of gaze accurately.
 - In certain experiments, there was not enough variation among the participants. For example, nearly all Himba participants were highly successful at counting stones.
 - Certain experiments were still in the developmental or experimental stages, such as the Valence or Luminance experiments. We hope to refine the design of these experiments in the future to make them suitable for further studies. Additionally, these experiments were not conducted with all populations.
 - The "Baskets" experiment, which we initially believed would indicate an implicit number line, actually turned out to reflect an explicit number line. Therefore, we have chosen to present only the results from the cards ordering experiment.
 - In the "Cards ordering" experiment, participants were asked to order both cards with Arabic numbers and dotted cards. However, we noticed that asking them to order cards with digits influenced their tendency to order the dotted cards in a linear manner. As a result, the results for ordering dotted cards linearly were no longer useful for analysis.

Only the "OrderingCards" and "Numerosity" experiments were conducted with all groups. Therefore, we have decided to include only the results from these experiments for publication, as they serve as good indicators of both explicit and implicit measures. We are willing to make the presentation of results as easy as possible, but also to make science as open as possible. Please feel free to let us know if you would like access to other files not provided here.

# Information about the data

Data folder contains the results for all group. These results are then further used to generate the final analysis.

 - file `Correlation_Score_Cards_Task` shows the results for each participant all groups (Himba Adults 2021, Himba Adults 2022, Italian Adults, Italian Preschoolers) for the task where participants have to order dotted rounded cards (with between 1 and 10 dots) the way they want.
 - Also, please note that this file is already preprocessed: correlations in the "cor" columns were obtained by computing **Kendall’s Tau**, yielding a score between -1 and 1. The code used to generated this score is available in `Generate_chanceDistribution.R`: it creates a Rdata file available in this folder name `Permutation_Distr.Rdata`.
 - file `Ordering_Cards_Task` shows the number (column total_count) and percentage (column Percent) of participants to order cards according to a range of different shapes for all groups
 - file `Numerosity_Comparison_Task` shows the mean score for each participants for each condition (Increasing-Congruent, Increasing-Incongruent, Decreasing-Congruent, Decreasing-Incongruent). Mean scores include mean time, mean error, and mean inverse efficiency ("invefi")

Raw data (including result file for each participant) are not presented in this folder to make it simpler to read and access, but feel free to ask elena.eccher-1@unitn.it for more information it (also, pictures of the disposition of cards are available for the experiment with Himbas).

Note that we would be happy to share to code used for generating the experiment if you are interested in replicating or pushing forward the results.

# Information about the code                                                                                                                                                                                                                                                                                                                      
Analysis were obtained using R (write here R version - it is written at first when you open R in your console). Results were printed in an html file (`Analysis_Code.hmtl`).   

The list of packages needed to run the code, also in bibtex format, in the file `Reference_list.bib`.

# Information about the Figures

Figures are automatically generated from the RMarkdown code, and are available in the Figures folder. Please note that for replication, an empty folder called "Figures" needs to be created.
