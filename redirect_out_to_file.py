import sys

# Store the original stdout
original_stdout = sys.stdout

with open('redirected_output.txt', 'w') as f:
    sys.stdout = f  # Redirect stdout to the file
    print("This will go to the file.")
    print("So will this.")

# Restore original stdout
sys.stdout = original_stdout
print("This will print to the console again.")