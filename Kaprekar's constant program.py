# Python program for visualization of frequency of Kaprekar's routine in a 4-digit number required to yield the Kaprekar's constant -  6174 in a graph

import matplotlib.pyplot as plt

def calculate_frequency_array():
    frequency_array = []
    
    for number in range(1000, 9999 + 1):      
        if (number % 1111 == 0):
            frequency_array.append(-1)
            continue

        else:
            routine_frequency = calculate_Kaprekars_routine_frequency(number)       
            frequency_array.append(routine_frequency)

    return(frequency_array)

def Kaprekars_routine(number):
    if len(str(number)) == 3:
        number_string = str(number).zfill(4)

    else:
        number_string = str(number)

    number_digits = [number_digit for number_digit in number_string if number_string.isdigit()]
    
    min_number = "".join(sorted(number_digits))
    max_number = "".join(sorted(number_digits, reverse = True))

    return (int(max_number) - int(min_number))
   
def calculate_Kaprekars_routine_frequency(number):
    counter = 0

    while True:
        result = Kaprekars_routine(number)

        if (result == 6174):
            counter += 1
            break

        else:
            counter += 1
            number = result
 
    return counter

def calculate_iteration_frequencies(frequency_array):
    frequency_of_iterations = []
    for number in range(-1, 7 + 1):
        frequency_of_iterations.append(frequency_array.count(number))

    return frequency_of_iterations

# Graphs

# Bar Chart
def plot_bar_chart(number_array, frequency_array):
    plt.bar(number_array, frequency_array)

    plt.title("Number of iterations required for each 4-digit number to result in Kaprekar's constant")
    
    plt.show()

# Colored Bar Chart
def plot_colored_bar_chart(number_array, frequency_array):
    colors_array = []
    for frequency in frequency_array:
        """
        Using Tableau colors
        match frequency:
            case -1:
                colors_array.append('tab:gray')
            case 0:
                colors_array.append('tab:cyan')
            case 1:
                colors_array.append('tab:blue')
            case 2:
                colors_array.append('tab:orange')
            case 3:
                colors_array.append('tab:green')
            case 4:
                colors_array.append('tab:red')
            case 5:
                colors_array.append('tab:purple')
            case 6:
                colors_array.append('tab:brown')
            case 7:
                colors_array.append('tab:pink')
             """
        
        match frequency:
            case -1:
                colors_array.append('#003f5c')
            case 0:
                colors_array.append('#2f4b7c')
            case 1:
                colors_array.append('#665191')
            case 2:
                colors_array.append('#a05195')
            case 3:
                colors_array.append('#d45087')
            case 4:
                colors_array.append('#f95d6a')
            case 5:
                colors_array.append('#ff7c43')
            case 6:
                colors_array.append('#ffa600')
            case 7:
                colors_array.append('#ead637')


    plt.bar(number_array, frequency_array, color = colors_array)

    plt.title("Number of iterations required for each 4-digit number to result in Kaprekar's constant")

    plt.show()

# Line Plot
def plot_line_graph(number_array, frequency_array):
    plt.plot(number_array, frequency_array, linewidth = '0.1', marker = 'o', markersize=1)

    plt.xlabel('Number')
    plt.ylabel('Number of iterations')

    plt.title("Number of iterations required for each 4-digit number to result in Kaprekar's constant")

    plt.show()

# Scatter Plot
def plot_scatter_plot(number_array, frequency_array):
    plt.scatter(number_array, frequency_array, label = 'Number of iterations', marker = 'o', s = 0.5)

    plt.xlabel('Number')
    plt.ylabel('Number of iterations')

    plt.title("Number of iterations required for each 4-digit number to result in Kaprekar's constant")

    plt.legend()

    plt.xlim(1000, 9999)
    plt.ylim(-1, 8)

    plt.show()

def plot_graphs(number_array, frequency_array):
    plot_bar_chart(number_array, frequency_array)
    plot_colored_bar_chart(number_array, frequency_array)
    plot_line_graph(number_array, frequency_array)
    plot_scatter_plot(number_array, frequency_array)

def plot_iteration_frequency_graph(iteration_frequency_array):
    number_array = [number for number in range(-1, 7 + 1)]

    colors_array = ['#003f5c', '#2f4b7c', '#665191', '#a05195', '#d45087', '#f95d6a', '#ff7c43', '#ffa600']

    plt.bar(number_array, iteration_frequency_array, color = colors_array)
    
    # Adding labels in each bar
    for i in range(-1, len(iteration_frequency_array)):
        plt.text(i - 1, iteration_frequency_array[i], iteration_frequency_array[i], ha = 'center')

    plt.title("Frequency of iterations required for 4-digit numbers to result in Kaprekar's constant")
    
    plt.xlabel('Number of iterations')
    plt.ylabel('Frequency')

    plt.show()

def main():
    numbers_array = []
    numbers_array = [number for number in range(1000, 9999 + 1)]

    frequency_array = calculate_frequency_array()

    iteration_frequency_array = calculate_iteration_frequencies(frequency_array)

    plot_graphs(numbers_array, frequency_array)

    plot_iteration_frequency_graph(iteration_frequency_array)

if __name__ == "__main__":
    main()