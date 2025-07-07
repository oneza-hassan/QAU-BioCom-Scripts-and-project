# QAU BioComputing Course (Python) 🧬💻

![Biopython](https://img.shields.io/badge/Made%20with-Biopython-blue)
![Python](https://img.shields.io/badge/Python-3.8%2B-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

**Repository by:** [Oneza Hassan Alvi](https://github.com/oneza-hassan/QAU-BioCom-Scripts-and-project.git))  
**Registration #:** 04281913032  
**Made with ❤️ for BioComputing Final Project**

---

## 📌 Project Overview
This repository contains **all lab assignments** and the **final project** from the BioComputing course at QAU. The flagship project is a **protein sequence analysis tool** that predicts helical regions using the Kyte-Doolittle hydrophobicity scale.

---

## 🔍 Final Project: Protein Sequence Analyzer
### **Features**
- Calculates **amino acid composition** (% of each residue).
- Computes **molecular weight** of the protein.
- Predicts **helix regions** using the Kyte-Doolittle scale (window-based approach).
- Saves results to `protein_analysis_results.txt`.

### 🛠️ Code Improvements (From Original)
1. **Error Handling**: Added `try-except` blocks for file reading.
2. **Edge Cases**: Checks for short sequences (<11 residues).
3. **Output Formatting**: Merged overlapping helices for cleaner results.
4. **File Export**: Results now save to a `.txt` file automatically.

### 🚀 How to Run

python protein_analysis.py

Input: Provide a FASTA file when prompted.
Output: Generates protein_analysis_results.txt.


###📂 Repository Structure

BioComputing_Course_FAST-NU/
├── Project/               # Final Project
│   ├── protein_analysis.py
│   └── protein_analysis_results.txt
├── Labs/                  # All lab assignments
│   ├── Lab1.py
│   ├── Lab2.py
│   └── ...
├── Data/                  # Sample FASTA files
├── README.md              # This file

🧪 Key Python Libraries Used
Biopython: For sequence analysis (ProtParam, SeqIO).

Standard Libraries: File I/O, math operations.

📜 License
This project is licensed under the MIT License.
See LICENSE for details.

🙏 Credits
Author: Oneza Hassan Alvi

Institution: QAU, Islamabad

Course: BioComputing

"Biology is the science of life. Coding is the art of making life easier." ✨


