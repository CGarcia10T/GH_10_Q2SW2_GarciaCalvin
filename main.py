from pyscript import document

def calculate(e):
    output_summary = document.getElementById("output")
    output_summary.innerHTML = ""
    
    firstName = document.getElementById("fName").value
    lastName = document.getElementById("lName").value
    
    subject1 = int(document.getElementById("subject1").value)
    subject2 = int(document.getElementById("subject2").value)
    subject3 = int(document.getElementById("subject3").value)
    subject4 = int(document.getElementById("subject4").value)
    subject5 = int(document.getElementById("subject5").value)
    subject6 = int(document.getElementById("subject6").value)
    
    units = [5, 5, 2, 5, 5, 1] # Units for each subject
    Sci, Eng, ICT_unit, Math, Fil, PE_unit = units # Unpacking units
    
    GWA = ((subject1 * Sci) + (subject2 * Eng) + (subject3 * ICT_unit) + (subject4 * Math) + (subject5 * Fil) + (subject6 * PE_unit))/(Sci + Eng + ICT_unit + Math + Fil + PE_unit)
    
    final_message = f"""Hello, {firstName} {lastName}\n
    Science: {subject1}\n
    English: {subject2}\n
    ICT: {subject3}\n
    Math: {subject4}\n
    Filipino: {subject5}\n
    PE: {subject6}\n
    Your General Weighted Average (GWA) is: {round(GWA, 2)}"""
    
    output_summary.innerText = final_message
    