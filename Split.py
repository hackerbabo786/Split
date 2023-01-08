import os
import sys

def show_input_path():
  # Get the input file path from the user
  input_path = input("Enter the path of the file to remove duplicates from: ")

  # Check if the file exists
  if not os.path.exists(input_path):
    print("The file does not exist. Please enter a valid file path.")
    return
  
  return input_path

def remove_duplicate_lines(input_path):
  # Read all lines from the file
  with open(input_path, "r") as f:
    lines = f.readlines()
  
  # Remove duplicates
  lines = list(set(lines))

  return lines

def split_file(lines):
  # Ask the user how many parts they want to split the file into
  num_parts = int(input("How many parts do you want to split the file into? "))

  # Calculate the size of each part
  part_size = len(lines) // num_parts
  print("Each part will be {} lines long.".format(part_size))

  # Split the lines into the specified number of parts
  parts = [lines[i:i + part_size] for i in range(0, len(lines), part_size)]
  
  return parts

def show_output_path():
  # Get the output file path from the user
  output_path = input("Enter the path where the output files should be saved: ")

  # Create the output directory if it doesn't exist
  if not os.path.exists(output_path):
    os.makedirs(output_path)
  
  return output_path

def save_parts(parts, output_path):
  # Save each part to a separate file
  for i, part in enumerate(parts):
    with open(os.path.join(output_path, "part{}.txt".format(i + 1)), "w") as f:
      f.writelines(part)

def show_options():
  print("1. Split a file into multiple parts")
  print("2. Watch a video on how to use this script")
  print("3. Quit")

def main():
  while True:
    show_options()
    option = input("Enter an option: ")
    
    if option == "1":
      input_path = show_input_path()
      lines = remove_duplicate_lines(input_path)
      parts = split_file(lines)
      output_path = show_output_path()
      save_parts(parts, output_path)
      print("Done!")
    elif option == "2":
      # Open the video in the default web browser
      os.system('xdg-open https://youtube.com/shorts/6J6hEe1BAs8')
    elif option == "3":
      sys.exit()
    else:
      print("Invalid option. Please try again.")

if __name__ == "__main__":
  main()