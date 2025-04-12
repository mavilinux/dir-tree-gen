# Directory Tree Generator

## Overview

The **Directory Tree Generator** is a Python application that allows users to generate and save the directory structure of a specified folder. It uses a graphical user interface (GUI) built with **Tkinter** and provides options to save the generated directory tree in either **Text** or **PDF** format. The program offers a simple and intuitive way to browse directories, generate the tree structure, and save it for later use.

## Features

- Browse for a folder and generate its directory structure.
- Display the directory structure in a scrollable text area.
- Save the directory tree in either **Text** (.txt) or **PDF** (.pdf) format.
- User-friendly interface built using **Tkinter**.

## Installation

To use the Directory Tree Generator, follow the steps below:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/mavilinux/dir_tree_gen.git
   cd dir_tree_gen
   ```

2. **Install required dependencies**:
   You need to have Python 3.x installed, along with the following libraries:
   - **Tkinter** (comes pre-installed with Python)
   - **ReportLab** (used for generating PDF)

   You can install the required dependencies using pip:
   ```bash
   pip install reportlab
   ```

## Usage

### Running the Application

Once you have installed the necessary dependencies, run the `dir_tree_gen.py` script to launch the GUI application:

```bash
python dir_tree_gen.py
```

### Using the Application

1. **Select a Folder**: 
   - Click the "Browse" button to choose the folder you want to generate a directory tree for.

2. **Generate Tree Structure**: 
   - The directory structure will be displayed in the scrollable text box on the interface.

3. **Save the Tree Structure**:
   - Choose the desired format (Text or PDF) from the "Choose Format" dropdown.
   - Click "Save Tree" to save the directory tree in your preferred format.
   
4. **Exit the Application**:
   - Click "Exit" to close the application.

## Functions

### `get_tree_structure(startpath)`
- **Description**: Recursively generates the directory tree structure starting from the given path.
- **Parameters**: 
  - `startpath`: The root directory from which the tree structure will be generated.
- **Returns**: A string representing the directory tree structure.

### `save_as_txt(tree, filepath)`
- **Description**: Saves the directory tree to a text file.
- **Parameters**:
  - `tree`: The generated directory tree as a string.
  - `filepath`: The location where the text file should be saved.

### `save_as_pdf(tree, filepath)`
- **Description**: Saves the directory tree to a PDF file.
- **Parameters**:
  - `tree`: The generated directory tree as a string.
  - `filepath`: The location where the PDF file should be saved.

### `browse_folder()`
- **Description**: Opens a file dialog to browse and select a folder for generating the directory tree.

### `save_file()`
- **Description**: Saves the directory tree structure in the selected file format (TXT or PDF).

### `exit_program()`
- **Description**: Exits the application.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---