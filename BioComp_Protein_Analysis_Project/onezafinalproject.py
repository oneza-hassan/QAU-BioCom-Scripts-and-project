#Oneza Hassan Alvi
#04281913032
#biocomputing project
# Importing Biopython modules

print("ONEZA HASSAN ALVI")
print("REG NUM: 04281913032")
print("BIOCOMPUING FINAL PROJECT")
print("--------------------------------")

from Bio import SeqIO
from Bio.SeqUtils import ProtParam
from Bio.SeqUtils.ProtParamData import kd

# Asking the user for the protein fasta file name and storing it in a variable
file_name = input("Enter the accurate protein fasta file name from the working directory or give the whole path: ")

try:
    protein = SeqIO.read(file_name, "fasta")
except FileNotFoundError:
    print("Error: File not found. Check the filename/path.")
    exit()
except Exception as e:
    print(f"Error reading the file: {e}")
    exit()

# Reading the protein sequence from the file name given by the user
protein = SeqIO.read(file_name, "fasta") # This function reads a single sequence from a fasta file and returns a SeqRecord object

# Calculating the amino acid composition
aa_comp = ProtParam.ProteinAnalysis(str(protein.seq)).get_amino_acids_percent()

# Calculating the molecular weight
mw = ProtParam.ProteinAnalysis(str(protein.seq)).molecular_weight()

# Predicting the secondary structure using Kyte-Doolittle hydrophobicity scale
kd_window = 11 # window size for sliding average
kd_threshold = 1.6 # threshold for assigning helix
kd_helix = [] # list of helix regions
kd_value = [] # list of hydrophobicity values

if len(protein.seq) < kd_window:
    print("Protein sequence too short for window-based analysis.")
    exit()
else:
    #Calculating the mean hydrophobicity for each window
    for i in range(len(protein) - kd_window + 1):
        window = protein[i:i+kd_window] # slicing the window
        value = 0 # initializing the value
        for aa in window: # looping over each amino acid in the window
            value += kd[aa] # adding the hydrophobicity value from the scale
        value /= kd_window # dividing by the window size to get the mean
        kd_value.append(value) # appending to the list of values

# Assigning helix regions based on the threshold
start = None # initializing the start index
for i in range(len(kd_value)): # looping over each value
    if kd_value[i] > kd_threshold: # if the value is above the threshold
        if start == None: # and if we have not started a helix region
            start = i # set the start index to the current index
    else: # if the value is below or equal to the threshold
        if start != None: # and if we have started a helix region
            end = i + kd_window - 1 # set the end index to the current index plus window size minus one
            kd_helix.append((start, end)) # append the start and end indices as a tuple to the list of helix regions
            start = None # reset the start index to None

# Printing the results
print("--------------------------------")

print("Protein sequence:", protein.seq)
print("--------------------------------")

print("kd dictionary that contains the Kyte-Doolittle hydrophobicity scale:")
print(kd)
print("--------------------------------")

print("Amino acid composition in the protein sequence:")
for aa, percent in aa_comp.items():
    print(aa, percent*100)
print("--------------------------------")

print("Molecular weight of the protein:", mw, "Da")
print("--------------------------------")

print("Predicted helix regions using Kyte-Doolittle scale:")
for start, end in kd_helix:
    print("From", start, "to", end)

# Save results to a file
output_filename = "protein_analysis_results.txt"
with open(output_filename, "w") as f:
    f.write("PROTEIN ANALYSIS REPORT\n")
    f.write("--------------------------------\n")
    f.write(f"Protein sequence: {protein}\n")
    f.write("--------------------------------\n")
    f.write("Amino acid composition (%):\n")
    for aa, percent in aa_comp.items():
        f.write(f"{aa}: {percent * 100:.2f}%\n")
    f.write("--------------------------------\n")
    f.write(f"Molecular weight: {mw:.2f} Da\n")
    f.write("--------------------------------\n")
    f.write("Predicted helix regions (Kyte-Doolittle):\n")
    if not kd_helix:
        f.write("No helices predicted.\n")
    else:
        for start, end in kd_helix:
            f.write(f"From {start} to {end} (Length: {end - start + 1} residues)\n")

print(f"\nResults saved to {output_filename}!")