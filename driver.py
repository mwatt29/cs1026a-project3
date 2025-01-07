import subprocess
import sys

def run_car_program(input_sequence):
    
    process = subprocess.Popen(['python', 'car.py'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    process.stdin.write(input_sequence) 
    process.stdin.flush()
    # Wait for the process to finish and get the output
    output, errors = process.communicate()

    # Print the output and errors
    print("Output:")
    print(output)
    print("\nErrors:")
    print(errors)




if __name__ == "__main__":
    
    input_sequence1 = "3\nAndleeb\n7t0333\n10\n1\nLandRover\n34\nabc123\n2\nJohn Doe\n1234567890\n3\nJohn Doe\nabc123\n10\n5\nsummary1.txt\n6\n"
    
    
    input_sequence2 = "3\nJohn Carl\n7t0333\n10\n3\nAndleeb\n7bc123\n10\n1\nCadillac\ne4\nsts123\n1\nLandRover\n32\nabc123\n2\nJohn Doe\n1234567890\n3\nJohn Doe\nabc123\n10\n5\nsummary2.txt\n6\n"
    
    
    input_sequence3 = "2\nAndrew Sagan\n7uj123\n1\nFiat\n44\nsts123\n1\nBMW\n32\nsts123\n2\nJohn Doe\n1234567890\n3\nJohn Doe\nsts123\n10\n5\nsummary3.txt\n6\n"
    
    
    input_sequence4 = "3\nAndrew Sagan\n7ts123\n10\n1\nFiat\n12\nabc123\n1\nNisan\n3\nabc123\n1\nBMW\n44\nsts123\n2\nJohn Doe\n1234567890\n2\nMohamed\n1666567890\n3\nMohamed\nabc123\n10\n5\nsummary4.txt\n6\n"

    input_sequence5 = "1\nNisan\n12\nabc123\n1\nToyota\n3\nabc123\n1\nChevrolet\n44\nsts123\n1\nTesla\n144\nst0123\n2\nJohn Doe\n1234567890\n2\nElon Musk\n777767890\n2\nNageub Ola\n1666567890\n3\nJohn Doe\nabc123\n10\n3\nElon Musk\nsts123\n10\n3\nNageub Ola\nst0123\n10\n4\nJohn Doe\nabc123\n4\nElon Musk\nsts123\n4\nNageub Ola\nsts123\n3\nJohn Doe\nst0123\n10\n3\nJohn Doe\nabc123\n10\n3\nJohn Doe\nsts123\n10\n1\nFord\n44\nyu0123\n3\nAndrew Ng\nyu0123\n10\n5\nsummary5.txt\n6\n"
    
    inputs = [input_sequence1, input_sequence2, input_sequence3, input_sequence4, input_sequence5] 

    for input_sequence in inputs : 
        print("Running car.py with the following input sequence: ", input_sequence)
        run_car_program(input_sequence)