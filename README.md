In this repository, you will find the optimized geometries of 90 meta-, 90 para-substituted benzoic acid derivatives and 90 substituted benzene derivatives, and two Excel files (ML-HammettConstants-ORCA.xlsx and ChelpG-Gaussian09.xlsx) containing the atomic charges of the carbon atoms in the core structure (the benzene ring) of the aforementioned systems.

These carbon charges were calculated by single-point calculations at the CAM-B3LYP/Def2-TZVP level upon B3LYP/Def2-TZVP-optimized structures and considered the Mulliken, Loewdin, Hirshfeld, and ChelpG models. All quantum chemical calculations were performed with the ORCA 5.0.3 and Gaussian 09 software package. You will also find our inputs here. ORCA showed some curious ChelpG values that we observed to be due to the van der Waals radii used as the default setting. Therefore we also calculated the ChelpG charges with Gaussian 09 (see file ChelpG-Gaussian09.xlsx).

The variations of the carbon charges were obtained by subtracting the charge of a carbon atom in an unsubstituted benzoic acid (or benzene) system from the respective carbon atom in the substituted derivatives listed above.

The variations of the carbon charges were then used in our Machine-Learning (ML)-based procedure to calculate Hammett’s constants. The ML algorithm considered in the aforementioned Excel file is the Lasso Lars IC. The Leave-One-Out Cross Validation was also considered. The results seemed to favor the Hirshfeld model of atomic charges, thus, all ML-calculated Hammett's constants (see the ML-HammettConstants-ORCA.xlsx file) are based on this model.

The Python scripts used to carry out these analysis are also present in this directory (ML-python-scripts.zip)

For more information, see the published paper of our work in the following link: https://doi.org/10.1021/acs.joc.3c00410

We hope our work will help you in any way possible and feel free to contact us.

From the Theoretical Chemistry Group at the Military Institute of Engineering (Rio de Janeiro, Brazil), we wish you all the best.

Cheers!
