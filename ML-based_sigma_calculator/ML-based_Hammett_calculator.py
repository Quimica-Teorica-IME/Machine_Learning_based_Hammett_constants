import PySimpleGUI as psg

# Hirshfeld charge of the carbon atoms in the unsubstituted benzoic acid.
q1H = -0.031845
q2H = -0.021461
q3H = -0.017574
q4H = -0.014437
q5H = -0.023121
q6H = -0.033286

# Function to clear the GUI.
def clear_input(window, values):
    for key in values:
        window[key]('')
    return None

# Function to calculate the ML-based Hammett's constants.
def calculate(values):

    # Hirshfeld charge of the carbon atoms in the meta-substituted benzoic acid.
    q1m = float(values['C1m'])
    q2m = float(values['C2m'])
    q3m = float(values['C3m'])
    q4m = float(values['C4m'])
    q5m = float(values['C5m'])
    q6m = float(values['C6m'])

    # Hirshfeld charge of the carbon atoms in the para-substituted benzoic acid.
    q1p = float(values['C1p'])
    q2p = float(values['C2p'])
    q3p = float(values['C3p'])
    q4p = float(values['C4p'])
    q5p = float(values['C5p'])
    q6p = float(values['C6p'])

    # GUI column names.
    col_1_name = psg.Text('meta-substituted benzoic acid derivative:')
    col_2_name = psg.Text('para-substituted benzoic acid derivative:')

    # GUI input columns.
    col_1 = [[col_1_name], [q1m], [q2m], [q3m], [q4m], [q5m], [q6m]]
    col_2 = [[col_2_name], [q1p], [q2p], [q3p], [q4p], [q5p], [q6p]]

    # Equations to calculated ML-based Hammett's constants.
    sigP = (0.0559984291979229
        + 0 * (q1p - q1H)
        + 1.54155373 * (q2p - q2H)
        + 7.83018588 * (q3p - q3H)
        + 35.51048349 * (q4p - q4H)
        + 6.46471909 * (q5p - q5H)
        + 0 * (q6p - q6H))
    
    sigM = (0.034107489897652
        + 1.77057768 * (q1m - q1H)
        + 4.40217901 * (q2m - q2H)
        + 4.54859702 * (q3m - q3H)
        + 29.88114411 * (q4m - q4H)
        + 3.2522296 * (q5m - q5H)
        + 8.09429935 * (q6m - q6H))
    
    sigPplus = (-0.0927636385210438
        + 0 * (q1p - q1H)
        + 2.79832233 * (q2p - q2H)
        + 0 * (q3p - q3H)
        + 74.77928254 * (q4p - q4H)
        - 17.36669707 * (q5p - q5H)
        - 6.46769884 * (q6p - q6H))
    
    sigPminus = (0.254946516927649
        + 0 * (q1p - q1H)
        + 0 * (q2p - q2H)
        + 0 * (q3p - q3H)
        + 38.57534345 * (q4p - q4H)
        + 17.57092666 * (q5p - q5H)
        + 2.79074655 * (q6p - q6H))
    
    sigM0 = (0.0486361244731998
        + 1.2715913 * (q1m - q1H)
        + 6.34354536 * (q2m - q2H)
        + 3.38799611 * (q3m - q3H)
        + 35.6908435 * (q4m - q4H)
        + 0.54967969 * (q5m - q5H)
        + 8.93687531 * (q6m - q6H))
    
    sigP0 = (0.0622831539306458
        + 0 * (q1p - q1H)
        + 0 * (q2p - q2H)
        + 0 * (q3p - q3H)
        + 19.44701496 * (q4p - q4H)
        + 39.52624845 * (q5p - q5H)
        + 1.77911122 * (q6p - q6H))
    
    sigI = (0.0727326665394382
        + 1.13392176 * (q1m - q1H)
        + 5.88705143 * (q2m - q2H)
        + 0 * (q3m - q3H)
        + 44.84098773 * (q4m - q4H)
        - 6.0773907 * (q5m - q5H)
        + 7.7039257 * (q6m - q6H))
    
    sigR = sigP - sigI

    return sigP, sigM, sigPplus, sigPminus, sigM0, sigP0, sigI, sigR 

# Function to validate the input values (Hirshfeld charges).
def validate_inputs(values):
    
    # Creating a list of keys to be used in the validate_inputs function.
    input_fields = ['C1m', 'C2m', 'C3m', 'C4m', 'C5m', 'C6m', 'C1p', 'C2p', 'C3p', 'C4p', 'C5p', 'C6p']
    
    # Creating a list of errors if any of the keys above is empty.
    errors = []
    
    for field in input_fields:
        if not values[field]:
            errors.append(f" Error: carbon atom charges must not be left empty! ")

    return errors

# GUI theme and font.
psg.theme('DarkGreen1')
psg.set_options(font=('Helvetica', 12))

# Setting the GUI layout.
layout = [
    [psg.Text('Insert all of the Hirshfeld atomic charges (q) of the carbon atoms as indicated by the image provided with this program.\nCalculations must be performed at the CAM-B3LYP/Def2-TZVP//B3LYP/Def2-TZVP level.\n')],
    [psg.Text('meta-substituted benzoic acid derivative\n')] + [psg.Text('para-substituted benzoic acid derivative\n')],
    [psg.Text('Carbon 1:', size=12), psg.InputText(size=12, key='C1m')] + [psg.Text('', size=12), psg.InputText(size=12, key='C1p')],
    [psg.Text('Carbon 2:', size=12), psg.InputText(size=12, key='C2m')] + [psg.Text('', size=12), psg.InputText(size=12, key='C2p')],
    [psg.Text('Carbon 3:', size=12), psg.InputText(size=12, key='C3m')] + [psg.Text('', size=12), psg.InputText(size=12, key='C3p')],
    [psg.Text('Carbon 4:', size=12), psg.InputText(size=12, key='C4m')] + [psg.Text('', size=12), psg.InputText(size=12, key='C4p')],
    [psg.Text('Carbon 5:', size=12), psg.InputText(size=12, key='C5m')] + [psg.Text('', size=12), psg.InputText(size=12, key='C5p')],
    [psg.Text('Carbon 6:', size=12), psg.InputText(size=12, key='C6m')] + [psg.Text('', size=12), psg.InputText(size=12, key='C6p')],
    [psg.Text('Result:'), psg.Text(key='Output')],
    [psg.Push(), psg.Button('Reset'), psg.Button('Calculate')],
    [psg.Text('\nFor more information, please see the article:\nMonteiro-de-Castro, G.; Duarte, J. C.; Borges Jr., I. J. Org. Chem., 2023, 88 (14), 9791-9802.\nDOI: 10.1021/acs.joc.3c00410.')]
    ]

# GUI's title.
window = psg.Window("ML-based Hammett's constants calculator", layout, resizable=True)

while True:

    event, values = window.read()

    if event == psg.WIN_CLOSED:
        break

    elif event == 'Calculate':
        validation_errors = validate_inputs(values)
        if validation_errors:
            psg.popup_error('\n'.join(validation_errors), title='ERROR')
        else:
            sigP, sigM, sigPplus, sigPminus, sigM0, sigP0, sigI, sigR = calculate(values)
            result = f" \u03C3p:\t{sigP} \n \u03C3m:\t{sigM} \n \u03C3p+:\t{sigPplus} \n \u03C3p-:\t{sigPminus} \n \u03C3m0:\t{sigM0} \n \u03C3p0:\t{sigP0} \n \u03C3I:\t{sigI} \n \u03C3R:\t{sigR}"
            window['Output'].update(result)

    elif event == 'Reset':
        clear_input(window, values)
    
window.close()
