# Kaprekar-s-constant-visualization (Kaprekar's constant visualization)
Repository for data visualization of the number of iterations of Kaprekar's routine required for a 4-digit number to result in Kaprekar's constant (6174)

## Kaprekar's constant:
Kaprekar constant, or 6174, is a constant that arises when we take a 4-digit integer, form the largest and smallest numbers from its digits, and then subtract these two numbers. Continuing with this process of forming and subtracting, we will always arrive at the number 6174 in at most 7 iterations.
Once 6174 is reached, the process will continue yielding 7641 – 1467 = 6174.

The only four-digit numbers for which Kaprekar's routine does not reach 6174 are repdigits such as 1111, which give the result 0000 after a single iteration. All other four-digit numbers eventually reach 6174 if leading zeros are used to keep the number of digits at 4. For numbers with three identical digits and a fourth digit that is one higher or lower (such as 2111), it is essential to treat 3-digit numbers with a leading zero; for example: 2111 – 1112 = 0999; 9990 – 999 = 8991; 9981 – 1899 = 8082; 8820 – 288 = 8532; 8532 – 2358 = 6174.

An illustration:

Take a 4-digit number like 3215. Rearranging to form the largest and smallest with these digits, we get 5321 and 1235. Now, subtract them: 5321-1235 = 4086. Continue with the process of rearranging and subtracting:

8640 − 0468 = 8172

8721 − 1278 = 7443

7443 − 3447 = 3996

9963 − 3699 = 6264

6642 − 2466 = 4176

7641 − 1467 = 6174.
​

References:

[Kaprekar's Constant - Brilliant](https://brilliant.org/wiki/kaprekars-constant/#:~:text=Kaprekar%20constant%2C%20or%206174%2C%20is,then%20subtract%20these%20two%20numbers.)

[6174 - Wikipedia](https://en.wikipedia.org/wiki/6174)

[Kaprekar's Constant - Prime Newtons - Youtube](https://youtu.be/xtyNuOikdE4?si=PKPpSbdQjZZckDyt)

## Project Dependencies

- Matplotlib
- Python 3.10 or above (for the use of match case statements)

## Data visualization project

This project aims to help visualize some data relating to Kaprekar's constant.

Data represented or visualized in this project includes:
- Number of iterations required for each 4-digit number to result in Kaprekar's constant - 6174 (excluding repeating digits such as 1111.)
  ### Data represented using:
  - Bar plot
  - Colored bar plot
  - Line graph
  - Scatter plot
- Frequency of iterations required for 4-digit numbers to result in Kaprekar's constant
  ### Data represented using:
    - Bar plot

 **Note: Number of iterations for repeating 4-digit numbers such as 1111,2222, etc. and frequency of iterations for such numbers has been denoted by '-1'.**

## Images preview:

- Figure 1: Bar chart - 4-digit number vs Number of iterations to result in Kaprekar's constant (6174)

![Figure 1 - Bar chart!](/Images/Figure_1-Bar-chart.png "Figure 1: Bar chart - 4-digit number vs Number of iterations to result in Kaprekar's constant (6174)")

- Figure 2: Colored bar chart - 4-digit number vs Number of iterations to result in Kaprekar's constant (6174)

![Figure 2 - Colored bar chart!](/Images/Figure_2-Colored-Bar-chart.png "Figure 2: Colored bar chart - 4-digit number vs Number of iterations to result in Kaprekar's constant (6174)")

- Figure 3: Line graph - 4-digit number vs Number of iterations to result in Kaprekar's constant (6174)

![Figure 3 - Line graph!](/Images/Figure_3-Line-graph.png "Figure 3: Line graph - 4-digit number vs Number of iterations to result in Kaprekar's constant (6174)")

- Figure 4: Scatter plot - 4-digit number vs Number of iterations to result in Kaprekar's constant (6174)

![Figure 4 - Scatter plot!](/Images/Figure_4-Scatter-plot.png "Figure 4: Scatter plot - 4-digit number vs Number of iterations to result in Kaprekar's constant (6174)")

- Figure 5: Frequency of iterations required for 4-digit numbers to result in Kaprekar's number

![Figure 5 - Bar chart!](https://github.com/SumitRTamrakar/Kaprekar-s-constant-visualization/blob/main/Images/Figure_5-Frequency-Bar-chart.png "Figure 5: Frequency of iterations required for 4-digit numbers to result in Kaprekar's number")


 This was a personal project undertaken for fun and learning purposes. Any suggestions and constructive feedback for improvement are welcome.
