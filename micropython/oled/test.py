import sys
import time 

# Print a line with multiple words
sentence = "Test...."
sentence2 = "RUNNING"

print(sentence, end="", flush=True)
print(sentence2, end="", flush=True)

# Erase the last word
time.sleep(1)

# Move the cursor back to the start of the last word
""" sys.stdout.write("\033[F")  # Move cursor up one line
sys.stdout.write("\033[K")  # Move cursor to the end of the current line """

sys.stdout.write("\b" * len(sentence2))
sys.stdout.write(" " * len(sentence2))
sys.stdout.write("\b" * len(sentence2))


print("DONE")
